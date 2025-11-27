# 1. Ne asigurăm că avem biblioteca YOLO instalată
!pip install ultralytics

from ultralytics import YOLO

# 2. Încărcăm modelul "gol" (varianta nano - n, care e cea mai rapidă)
model = YOLO('yolov8n.pt')

# 3. CONECTAREA: Aici facem legătura cu datele descărcate de tine mai sus.
# Variabila 'dataset.location' știe exact unde a pus Roboflow pozele în Google Colab.
path_catre_fisierul_yaml = f"{dataset.location}/data.yaml"

# 4. START ANTRENARE
# epochs=25 -> va trece de 25 de ori prin toate pozele (poți pune 50 sau 100 pentru rezultate mai bune, dar durează mai mult)
# imgsz=640 -> rezoluția la care se uită la poze
results = model.train(data=path_catre_fisierul_yaml, epochs=25, imgsz=640)