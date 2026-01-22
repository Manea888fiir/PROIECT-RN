import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
import tempfile
from collections import Counter

# --- CONFIGURARE PAGINĂ ---
st.set_page_config(page_title="PPE Smart Tracker Pro", page_icon="👷", layout="wide")

# --- 1. LOGICA DE CULOARE ---
def get_color_category(hsv_img):
    colors = {
        "Galben (Muncitor)": [((20, 100, 100), (40, 255, 255))],
        "Albastru (Tehnic)": [((90, 50, 50), (130, 255, 255))], # Albastru extins
        "Alb (Inginer)":     [((0, 0, 180), (180, 50, 255))],
        "Rosu (Pompier)":    [((0, 70, 50), (10, 255, 255)), ((170, 70, 50), (180, 255, 255))]
    }
    
    max_pixels = 0
    detected_color = None

    for color_name, ranges in colors.items():
        mask_total = None
        for (lower, upper) in ranges:
            lower_np = np.array(lower, dtype="uint8")
            upper_np = np.array(upper, dtype="uint8")
            mask = cv2.inRange(hsv_img, lower_np, upper_np)
            if mask_total is None: mask_total = mask
            else: mask_total = cv2.add(mask_total, mask)
        
        count = cv2.countNonZero(mask_total)
        if count > max_pixels:
            max_pixels = count
            detected_color = color_name
            
    total_pixels = hsv_img.shape[0] * hsv_img.shape[1]
    # Filtru 5% suprafata minima
    if max_pixels < (0.05 * total_pixels):
        return None
        
    return detected_color

# --- 2. INTERFAȚA ---
st.title("👷 Sistem Urmărire Șantier (Cu Filtru de Erori)")

# --- SIDEBAR CU SETĂRI NOI ---
st.sidebar.header("🔧 Setări Calibrare")
conf_threshold = st.sidebar.slider("Precizie Detecție (Confidence)", 0.0, 1.0, 0.35)
min_frames_filter = st.sidebar.slider("Filtru Stabilitate (Frame-uri minime)", 5, 120, 30, 
    help="Un ID trebuie să apară cel puțin atâtea cadre ca să fie numărat. Crește valoarea dacă ai dubluri!")

model_path = "best.pt"
try:
    model = YOLO(model_path)
except:
    st.error("⚠️ Nu găsesc 'best.pt'!")
    st.stop()

option = st.radio("Sursă:", ("Imagine", "Video"), horizontal=True)

# Memoria globală
object_votes = {} 
snapshot_taken = False

if option == "Video":
    uploaded_video = st.file_uploader("Încarcă video", type=['mp4', 'avi'])
    
    if uploaded_video:
        tfile = tempfile.NamedTemporaryFile(delete=False) 
        tfile.write(uploaded_video.read())
        vf = cv2.VideoCapture(tfile.name)

        col1, col2 = st.columns([3, 1])
        with col1:
            st_frame = st.empty()
        with col2:
            st.markdown("### Statistici Live")
            st_info = st.empty()
            
        st_snap = st.sidebar.empty()

        while vf.isOpened():
            ret, frame = vf.read()
            if not ret: break
            
            # TRACKING ACTIVAT
            # tracker="bytetrack.yaml" este standard și bun
            # Adaugam imgsz=640 pentru a creste viteza (FPS)
            results = model.track(frame, persist=True, conf=conf_threshold, imgsz=640, verbose=False)
            
            current_ids_colors = {} 

            for r in results:
                boxes = r.boxes
                for box in boxes:
                    obj_id = int(box.id[0]) if box.id is not None else None
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    
                    color_label = ""
                    box_color = (0, 255, 0) # Verde default
                    
                    if obj_id is not None:
                        roi = frame[y1:y2, x1:x2]
                        if roi.size > 0:
                            hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
                            c_detected = get_color_category(hsv)
                            
                            if c_detected:
                                if obj_id not in object_votes:
                                    object_votes[obj_id] = []
                                object_votes[obj_id].append(c_detected)
                                
                                # Afișăm culoarea curentă
                                short_color = c_detected.split(' ')[0]
                                
                                # Verificăm dacă ID-ul este "validat" (a trecut de filtru)
                                is_validated = len(object_votes[obj_id]) > min_frames_filter
                                status_icon = "✅" if is_validated else "⏳"
                                
                                color_label = f" ID:{obj_id} {status_icon} | {short_color}"
                                current_ids_colors[obj_id] = short_color

                                # Logică culori cutii
                                if "Rosu" in c_detected: box_color = (0, 0, 255)
                                elif "Galben" in c_detected: box_color = (0, 255, 255)
                                elif "Albastru" in c_detected: box_color = (255, 0, 0)
                                elif "Alb" in c_detected: box_color = (0, 255, 0)

                    cv2.rectangle(frame, (x1, y1), (x2, y2), box_color, 2)
                    cv2.putText(frame, f"Casca{color_label}", (x1, y1-10), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, box_color, 2)

            # Snapshot Logic
            if len(current_ids_colors) > 0 and not snapshot_taken:
                snapshot_taken = True
                frame_rgb_snap = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                st_snap.image(frame_rgb_snap, caption="📸 Captură Automată", use_container_width=True)

            # Afișare Frame
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            st_frame.image(frame_rgb, use_container_width=True)
            
            # Afișare Info Live
            if current_ids_colors:
                st_info.info(f"Frame curent: {len(current_ids_colors)} detectii")

        vf.release()

        # --- RAPORT FINAL FILTRAT ---
        st.success("✅ Analiză finalizată!")
        st.markdown("### 📝 Rezultate Finale Validate")
        st.markdown(f"*(Se afișează doar persoanele detectate în cel puțin {min_frames_filter} cadre)*")
        
        final_results = {}
        ignored_count = 0

        if object_votes:
            for obj_id, votes in object_votes.items():
                # --- AICI ESTE FILTRUL MAGIC ---
                if len(votes) < min_frames_filter:
                    ignored_count += 1
                    continue # Sărim peste acest ID, e zgomot
                
                most_common_color = Counter(votes).most_common(1)[0][0]
                
                if most_common_color not in final_results:
                    final_results[most_common_color] = 0
                final_results[most_common_color] += 1
            
            # Afișare Coloane
            if final_results:
                cols = st.columns(len(final_results))
                idx = 0
                for color_name, count in final_results.items():
                    with cols[idx]:
                        st.metric(label="Categorie", value=color_name, delta=f"{count} persoane reale")
                    idx += 1
            else:
                st.warning("Nicio persoană nu a stat în cadru suficient timp pentru validare.")
            
            if ignored_count > 0:
                st.caption(f"⚠️ Am eliminat {ignored_count} detecții false/scurte (zgomot).")
        else:
            st.warning("Nu s-au detectat culori.")

elif option == "Imagine":
    # Imaginea nu are nevoie de tracking temporal
    uploaded_file = st.file_uploader("Încarcă imagine", type=['jpg', 'png'])
    if uploaded_file:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        results = model(img, conf=conf_threshold)
        found_colors = set()
        for r in results:
            for box in r.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                roi = img[y1:y2, x1:x2]
                if roi.size > 0:
                    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
                    c = get_color_category(hsv)
                    if c:
                        found_colors.add(c)
                        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        cv2.putText(img, c.split(' ')[0], (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)
        st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption="Rezultat")