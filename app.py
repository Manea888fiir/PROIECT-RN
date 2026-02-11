import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
import tempfile
from collections import Counter
from scipy.spatial import distance as dist
import time

# --- CONFIGURARE PAGINĂ ---
st.set_page_config(page_title="PPE Smart Tracker Pro", page_icon="👷", layout="wide")

# --- 1. LOGICA DE CULOARE HSV ---
def get_color_category(hsv_img):
    colors = {
        "Galben (Muncitor)": [((20, 100, 100), (40, 255, 255))],
        "Albastru (Tehnic)": [((90, 50, 50), (130, 255, 255))],
        "Alb (Inginer)":     [((0, 0, 180), (180, 50, 255))],
        "Rosu (Vizitator)":  [((0, 70, 50), (10, 255, 255)), ((170, 70, 50), (180, 255, 255))]
    }
    max_pixels = 0
    detected_color = None
    for color_name, ranges in colors.items():
        mask_total = None
        for (lower, upper) in ranges:
            mask = cv2.inRange(hsv_img, np.array(lower), np.array(upper))
            mask_total = mask if mask_total is None else cv2.add(mask_total, mask)
        count = cv2.countNonZero(mask_total)
        if count > max_pixels:
            max_pixels = count
            detected_color = color_name
    
    # Prag: culoarea trebuie să ocupe măcar 5% din zona detectată
    if detected_color and max_pixels > (0.05 * hsv_img.shape[0] * hsv_img.shape[1]):
        return detected_color
    return None

# --- 2. TRACKER MANUAL ---
class SimpleTracker:
    def __init__(self, maxDisappeared=15):
        self.nextObjectID = 0
        self.objects = {}
        self.disappeared = {}
        self.maxDisappeared = maxDisappeared

    def update(self, rects):
        if len(rects) == 0:
            for objectID in list(self.disappeared.keys()):
                self.disappeared[objectID] += 1
                if self.disappeared[objectID] > self.maxDisappeared:
                    del self.objects[objectID]
                    del self.disappeared[objectID]
            return self.objects

        inputCentroids = np.zeros((len(rects), 2), dtype="int")
        for (i, (startX, startY, endX, endY)) in enumerate(rects):
            inputCentroids[i] = (int((startX + endX) / 2.0), int((startY + endY) / 2.0))

        if len(self.objects) == 0:
            for i in range(0, len(inputCentroids)):
                self.objects[self.nextObjectID] = inputCentroids[i]
                self.disappeared[self.nextObjectID] = 0
                self.nextObjectID += 1
        else:
            objectIDs = list(self.objects.keys())
            objectCentroids = list(self.objects.values())
            D = dist.cdist(np.array(objectCentroids), inputCentroids)
            rows = D.min(axis=1).argsort()
            cols = D.argmin(axis=1)[rows]
            usedRows, usedCols = set(), set()
            for (row, col) in zip(rows, cols):
                if row in usedRows or col in usedCols: continue
                objectID = objectIDs[row]
                self.objects[objectID] = inputCentroids[col]
                self.disappeared[objectID] = 0
                usedRows.add(row)
                usedCols.add(col)
        return self.objects

# --- 3. INTERFAȚĂ STREAMLIT ---
st.title("👷 PPE Smart Tracker - Sistem Monitorizare")

# Meniu Lateral
st.sidebar.header("🔧 Configurare Sistem")
app_mode = st.sidebar.selectbox(
    "Alege Modul de Operare:",
    ["Imagine Statică", "Fișier Video", "Live Camera (Webcam)"]
)

st.sidebar.markdown("---")
conf_threshold = st.sidebar.slider("Confidență Detecție", 0.1, 1.0, 0.35)
min_frames_filter = st.sidebar.slider("Filtru Stabilitate (Cadre)", 5, 120, 15)

# Încărcare Model
@st.cache_resource
def load_model():
    return YOLO("models/best.pt")

try:
    model = load_model()
    st.sidebar.success("✅ Model YOLOv8m Încărcat")
except:
    st.error("❌ Eroare: Fișierul 'models/best.pt' nu a fost găsit.")
    st.stop()

# ==========================================
# MODUL 1: IMAGINE STATICĂ
# ==========================================
if app_mode == "Imagine Statică":
    st.header("🖼️ Analiză Imagine")
    uploaded_file = st.file_uploader("Încarcă o poză", type=['jpg', 'jpeg', 'png'])
    
    if uploaded_file:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        
        # Inferență
        results = model.predict(img, conf=conf_threshold)
        
        # Procesare rezultate
        for r in results:
            for box in r.boxes.xyxy.cpu().numpy().astype(int):
                x1, y1, x2, y2 = box
                roi = img[y1:y2, x1:x2]
                if roi.size > 0:
                    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
                    c_name = get_color_category(hsv)
                    
                    # Logică desenare
                    color_bgr = (0, 255, 0)
                    label = "Casca"
                    if c_name:
                        label = c_name
                        if "Rosu" in c_name: color_bgr = (0, 0, 255)
                        elif "Galben" in c_name: color_bgr = (0, 255, 255)
                        elif "Albastru" in c_name: color_bgr = (255, 0, 0)
                    
                    cv2.rectangle(img, (x1, y1), (x2, y2), color_bgr, 2)
                    cv2.putText(img, label, (x1, y1-10), 0, 0.6, color_bgr, 2)
        
        st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), use_container_width=True)

# ==========================================
# MODUL 2: FIȘIER VIDEO
# ==========================================
elif app_mode == "Fișier Video":
    st.header("🎬 Analiză Fișier Video")
    uploaded_video = st.file_uploader("Încarcă un clip video", type=['mp4', 'avi', 'mov'])
    
    if uploaded_video:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_video.read())
        vf = cv2.VideoCapture(tfile.name)
        
        st_frame = st.empty()
        tracker = SimpleTracker(maxDisappeared=15)
        object_votes = {} 

        while vf.isOpened():
            ret, frame = vf.read()
            if not ret: break
            
            # 1. Detecție
            results = model.predict(frame, conf=conf_threshold, imgsz=640, verbose=False)
            rects = [box for r in results for box in r.boxes.xyxy.cpu().numpy().astype(int)]
            
            # 2. Tracking
            tracked_objects = tracker.update(rects)

            # 3. Logică Culori + Desenare
            for (objID, centroid) in tracked_objects.items():
                for box in rects:
                    x1, y1, x2, y2 = box
                    # Match centroid cu cutie
                    if x1 <= centroid[0] <= x2 and y1 <= centroid[1] <= y2:
                        roi = frame[y1:y2, x1:x2]
                        if roi.size > 0:
                            hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
                            c_detected = get_color_category(hsv)
                            
                            if c_detected:
                                if objID not in object_votes: object_votes[objID] = []
                                object_votes[objID].append(c_detected)
                                
                                # Status validare
                                is_valid = len(object_votes[objID]) > min_frames_filter
                                status_icon = "✅" if is_valid else "⏳"
                                
                                # Alegere culoare cutie
                                bgr_draw = (0, 255, 0)
                                if "Rosu" in c_detected: bgr_draw = (0, 0, 255)
                                elif "Galben" in c_detected: bgr_draw = (0, 255, 255)
                                elif "Albastru" in c_detected: bgr_draw = (255, 0, 0)
                                
                                # Desenare
                                cv2.rectangle(frame, (x1, y1), (x2, y2), bgr_draw, 2)
                                text = f"ID:{objID} {status_icon} {c_detected.split(' ')[0]}"
                                cv2.putText(frame, text, (x1, y1-10), 0, 0.6, bgr_draw, 2)

            st_frame.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        vf.release()

# ==========================================
# MODUL 3: LIVE WEBCAM (NOU)
# ==========================================
elif app_mode == "Live Camera (Webcam)":
    st.header("🔴 Detecție Live pe Camera")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.info("Setări Cameră")
        # Selector Index Cameră
        cam_index = st.number_input("Index Cameră (0=Laptop, 1=USB)", value=0, step=1)
        run_camera = st.checkbox("Pornește Camera", value=False)
    
    with col2:
        # Statistici în timp real
        kpi1, kpi2 = st.columns(2)
        kpi1.metric("Status Sistem", "Așteptare..." if not run_camera else "Activ")
        kpi_fps = kpi2.empty()

    st_frame = st.empty()

    if run_camera:
        cap = cv2.VideoCapture(cam_index)
        
        if not cap.isOpened():
            st.error(f"Nu pot deschide camera {cam_index}. Verifică conexiunea.")
        else:
            # Inițializare Tracker pentru Live
            tracker = SimpleTracker(maxDisappeared=10)
            object_votes = {}
            prev_time = 0

            while run_camera:
                ret, frame = cap.read()
                if not ret:
                    st.warning("Semnal video pierdut.")
                    break
                
                # Calcul FPS
                curr_time = time.time()
                fps = 1 / (curr_time - prev_time) if (curr_time - prev_time) > 0 else 0
                prev_time = curr_time
                kpi_fps.metric("FPS (Real-time)", f"{int(fps)}")

                # Resize opțional pentru viteză (dacă ai lag, decomentează linia de mai jos)
                # frame = cv2.resize(frame, (640, 480))

                # 1. Detecție YOLO
                results = model.predict(frame, conf=conf_threshold, imgsz=640, verbose=False)
                rects = [box for r in results for box in r.boxes.xyxy.cpu().numpy().astype(int)]
                
                # 2. Tracking
                tracked_objects = tracker.update(rects)

                # 3. Logică Culori + Desenare
                for (objID, centroid) in tracked_objects.items():
                    for box in rects:
                        x1, y1, x2, y2 = box
                        if x1 <= centroid[0] <= x2 and y1 <= centroid[1] <= y2:
                            roi = frame[y1:y2, x1:x2]
                            if roi.size > 0:
                                hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
                                c_detected = get_color_category(hsv)
                                
                                if c_detected:
                                    if objID not in object_votes: object_votes[objID] = []
                                    object_votes[objID].append(c_detected)
                                    
                                    # Status
                                    is_valid = len(object_votes[objID]) > min_frames_filter
                                    status_icon = "✅" if is_valid else "⏳"
                                    
                                    # Culori
                                    bgr_draw = (0, 255, 0)
                                    if "Rosu" in c_detected: bgr_draw = (0, 0, 255)
                                    elif "Galben" in c_detected: bgr_draw = (0, 255, 255)
                                    elif "Albastru" in c_detected: bgr_draw = (255, 0, 0)
                                    
                                    cv2.rectangle(frame, (x1, y1), (x2, y2), bgr_draw, 2)
                                    text = f"ID:{objID} {status_icon} {c_detected.split(' ')[0]}"
                                    cv2.putText(frame, text, (x1, y1-10), 0, 0.6, bgr_draw, 2)

                # Afișare Frame
                st_frame.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            
            cap.release()