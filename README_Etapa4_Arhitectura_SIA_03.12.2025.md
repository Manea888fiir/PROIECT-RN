# 📘 README – Etapa 4: Arhitectura Completă a Aplicației SIA bazată pe Rețele Neuronale
**Disciplina:** Rețele Neuronale  
**Instituție:** POLITEHNICA București – FIIR  
**Student:** Manea Ionut Florin  
**Link Repository GitHub: https://github.com/Manea888fiir/PROIECT-RN
**Data:** 4.12.2025
---
## Scopul Etapei 4
Această etapă corespunde punctului **5. Dezvoltarea arhitecturii aplicației software bazată pe RN** din lista de 9 etape - slide 2 **RN Specificatii proiect.pdf**.
**Trebuie să livrați un SCHELET COMPLET și FUNCȚIONAL al întregului Sistem cu Inteligență Artificială (SIA). In acest stadiu modelul RN este doar definit și compilat (fără antrenare serioasă).**
### IMPORTANT - Ce înseamnă "schelet funcțional":
 **CE TREBUIE SĂ FUNCȚIONEZE:**
- Toate modulele pornesc fără erori
- Pipeline-ul complet rulează end-to-end (de la date → până la output UI)
- Modelul RN este definit și compilat (arhitectura există)
- Web Service/UI primește input și returnează output
 **CE NU E NECESAR ÎN ETAPA 4:**
- Model RN antrenat cu performanță bună
- Hiperparametri optimizați
- Acuratețe mare pe test set
- Web Service/UI cu funcționalități avansate
**Scopul anti-plagiat:** Nu puteți copia un notebook + model pre-antrenat de pe internet, pentru că modelul vostru este NEANTRENAT în această etapă. Demonstrați că înțelegeți arhitectura și că ați construit sistemul de la zero.
---
##  Livrabile Obligatorii
### 1. Tabelul Nevoie Reală → Soluție SIA → Modul Software (max ½ pagină)
Completați in acest readme tabelul următor cu **minimum 2-3 rânduri** care leagă nevoia identificată în Etapa 1-2 cu modulele software pe care le construiți (metrici măsurabile obligatoriu):
| **Nevoie reală concretă** | **Cum o rezolvă SIA-ul vostru** | **Modul software responsabil** |
|---------------------------|--------------------------------|--------------------------------|
| Ex: Detectarea automată a fisurilor în suduri robotizate | Clasificare imagine radiografică → alertă operator în < 2 secunde | RN + Web Service 
-------------------------------------------------------------------------
**RASPUNS:**
| Detectarea castilor de protectie in zonele unde este nevoie | Recunoaste castile de protectie | RN  |
| Preventia accidententelor de munca | Recunoaste castile de protectie | RN|
**Instrucțiuni:**
- Fiți concreti (nu vagi): "detectare fisuri sudură" ✓, "îmbunătățire proces" ✗
- Specificați metrici măsurabile: "< 2 secunde", "> 95% acuratețe", "reducere 20%"
- Legați fiecare nevoie de modulele software pe care le dezvoltați
---
### 2. Contribuția Voastră Originală la Setul de Date – MINIM 40% din Totalul Observațiilor Finale
**Regula generală:** Din totalul de **N observații finale** în `data/processed/`, **minimum 40%** trebuie să fie **contribuția voastră originală**.
**RASPUNS:**
Contribuția la Setul de Date:
În cadrul acestui proiect, contribuția personală asupra setului de date final este de 100%. Deși imaginile brute (raw images) au fost colectate din surse publice (internet), acestea nu conțineau nicio informație semantică pre-existentă.
Întregul proces de transformare a datelor brute într-un set de date compatibil cu algoritmul YOLO a fost realizat manual și integral de către mine. Acesta a inclus:
1.	Curatorierea datelor: Selecția manuală a imaginilor relevante pentru a asigura varietatea scenariilor (unghiuri, luminozitate, ocluziuni).
2.	Adnotarea (Labeling): Generarea manuală a tuturor etichetelor (bounding boxes) și a fișierelor de adnotare asociate, definind astfel „Ground Truth-ul” pentru antrenare.
Astfel, setul de date din data/processed/ este rezultatul exclusiv al efortului propriu de procesare și etichetare.

#### Tipuri de contribuții acceptate (exemple din inginerie):
Alegeți UNA sau MAI MULTE dintre variantele de mai jos și **demonstrați clar în repository**:

| Tip contribuție: Curatoriere și Etichetare Manuală (Dataset Custom) | Exemple concrete: Selecția și filtrarea manuală a 100 de imagini din surse open-source; Adnotarea manuală integrală (bounding boxes) a tuturor imaginilor pentru crearea Ground Truth; Implementarea structurii de date (split 70/15/15) | Dovada minimă: Folderul dataset/ conținând structura images/labels, cele 100 de fișiere .txt generate manual și fișierul data.yaml |
```
| **Tip contribuție** | **Exemple concrete din inginerie** | **Dovada minimă cerută** |
|---------------------|-------------------------------------|--------------------------|
| **Date generate prin simulare fizică** | • Traiectorii robot în Gazebo<br>• Vibrații motor cu zgomot aleator calibrat<br>• Consumuri energetice proces industrial simulat | Cod Python/LabVIEW funcțional + grafice comparative (simulat vs real din literatură) + justificare parametri |
| **Date achiziționate cu senzori proprii** | • 500-2000 măsurători accelerometru pe motor<br>• 100-1000 imagini capturate cu cameră montată pe robot<br>• 200-1000 semnale GPS/IMU de pe platformă mobilă<br>• Temperaturi/presiuni procesate din Arduino/ESP32 | Foto setup experimental + CSV-uri produse + descriere protocol achiziție (frecvență, durata, condiții) |
```
Acest tip de contributie se potriveste pentru proiectul meu:
| **Etichetare/adnotare manuală** | • Etichetat manual 1000+ imagini defecte sudură<br>• Anotat 500+ secvențe video cu comportamente robot<br>• Clasificat manual 2000+ semnale vibrații (normal/anomalie)<br>• Marcat manual 1500+ puncte de interes în planuri tehnice | Fișier Excel/JSON cu labels + capturi ecran tool etichetare + log timestamp-uri lucru |

| **Date sintetice prin metode avansate** | • Simulări FEM/CFD pentru date dinamice proces | Cod implementare metodă + exemple before/after + justificare hiperparametri + validare pe subset real |
#### Declarație obligatorie în README:
Scrieți clar în acest README (Secțiunea 2):

### Contribuția originală la setul de date:

Contributia originala la setul de date este in proportie cat se poate de mare a mea, eu am ales pozele de pe internet, (istockphoto.com), eu am pus marcajele necesare pe fiecare obiect in parte din fiecare poza cu ajutorul MakeSense.AI, tool care m-a ajutat in a imi exporta coordonatele de la “bounding boxes” (patratele cu care am inconjurat castile).
**Total observații finale:** 101 (după Etapa 3 + Etapa 4)
**Observații originale:** 101 ([100]%)
**Tipul contribuției:**
[ ] Date generate prin simulare fizică  
[ ] Date achiziționate cu senzori proprii  
[X] Etichetare/adnotare manuală  
[ ] Date sintetice prin metode avansate  
**Descriere detaliată:**
[Explicați în 2-3 paragrafe cum ați generat datele, ce metode ați folosit, 
de ce sunt relevante pentru problema voastră, cu ce parametri ați rulat simularea/achiziția]


### Generarea și Procesarea Datelor Experimentale
Pentru generarea setului de date inițial, am utilizat ca sursă primară platforma de generare și stocare istockphoto.ai, de unde am selectat manual o colecție de 100 de imagini relevante Procesul de achiziție nu a fost aleatoriu, ci a urmat o selecție riguroasă pentru a asigura variabilitatea vizuală a căștii de protecție (unghiuri de captură diferite, fundaluri complexe și condiții de iluminare variate, culori diferite). Această abordare a permis obținerea unor date de intrare de calitate superioară ("high-quality raw data"), esențiale pentru a compensa volumul redus al dataset-ului și pentru a oferi modelului trăsături clare pentru extragerea caracteristicilor.
Metoda centrală utilizată pentru transformarea acestor imagini brute în date de antrenament a fost adnotarea manuală integrală (manual bounding box annotation), realizată cu ajutorul instrumentului online makesense.ai. Am generat „Ground Truth-ul” necesar algoritmului YOLO prin desenarea manuală a fiecărui contur și exportarea coordonatelor normalizate în format .txt. Această etapă reprezintă o contribuție originală 100%, garantând precizia localizării căștilor și eliminând erorile de etichetare frecvente în dataset-urile automate sau publice. Relevanța acestor date este critică pentru problemă, deoarece oferă un mediu controlat și curat pentru validarea conceptului, izolând performanța modelului de zgomotul etichetelor greșite.
În ceea ce privește parametrii de simulare, am structurat setul de date utilizând o strategie de partiționare (Data Split) de 70/15/15, alocând aleatoriu 70% din imagini pentru faza de antrenare (Train), 15% pentru evaluarea performanței (Validation) si 15% pentru testarea performantei (Test). Această distribuție a fost aleasă pentru a maximiza capacitatea de învățare a modelului pe un set limitat si pentru a mă incadra in standardul pentru proiect, păstrând totodată un eșantion relevant statistic pentru verificarea capacității de generalizare și evitarea fenomenului de overfitting.


**Locația codului:** `src/data_acquisition/provenienta date (fisier txt)`
**Locația datelor:** `data/raw/dataset intreg.zip(imagini + adnotarile puse cu bounding boxes)/`
**Dovezi:**
- Grafic comparativ: `docs/generated_vs_real.png`
- Setup experimental: `docs/acquisition_setup.jpg` (dacă aplicabil)
- Tabel statistici: `docs/data_statistics.csv`
- 
```
#### Exemple pentru "contribuție originală":
-Simulări fizice realiste cu ecuații și parametri justificați  
-Date reale achiziționate cu senzori proprii (setup documentat)  
-Augmentări avansate cu justificare fizică (ex: simulare perspective camera industrială)  
#### Atenție - Ce NU este considerat "contribuție originală":
- Augmentări simple (rotații, flips, crop) pe date publice  
- Aplicare filtre standard (Gaussian blur, contrast) pe imagini publice  
- Normalizare/standardizare (aceasta e preprocesare, nu generare)  
- Subset dintr-un dataset public (ex: selectat 40% din ImageNet)
---

### 3. Diagrama State Machine a Întregului Sistem (OBLIGATORIE)
**Cerințe:**
- **Minimum 4-6 stări clare** cu tranziții între ele
- **Formate acceptate:** PNG/SVG, pptx, draw.io 
- **Locație:** `docs/state_machine.*` (orice extensie)
- **Legendă obligatorie:** 1-2 paragrafe în acest README: "De ce ați ales acest State Machine pentru nevoia voastră?"
"Am ales acest model de State Machine deoarece reflectă fidel fluxul secvențial de procesare necesar unui sistem de Computer Vision bazat pe Deep Learning. Arhitectura separă clar etapa de inițializare (care este consumatoare de resurse la încărcarea modelului best.pt în memorie) de bucla operațională de inferență, optimizând astfel timpul de răspuns pentru procesări multiple.
Stările sunt concepute pentru a gestiona robust erorile (prin starea ERROR_STATE, care previne blocarea scriptului la fișiere corupte) și pentru a asigura trasabilitatea rezultatelor. Tranziția critică este cea dintre INFERENCE și POST_PROCESS, unde datele brute de la rețeaua neuronală (coordonate numerice) sunt transformate în informație vizuală utilă (bounding boxes pe Cască de protecție), condiționată de pragul de încredere (confidence threshold)."
**Stări tipice pentru un SIA:**
```
IDLE → ACQUIRE_DATA → PREPROCESS → INFERENCE → DISPLAY/ACT → LOG → [ERROR] → STOP
                ↑______________________________________________|
```
**Exemple concrete per domeniu de inginerie:**
#### A. Monitorizare continuă proces industrial (vibrații motor, temperaturi, presiuni):
```
IDLE → START_ACQUISITION → COLLECT_SENSOR_DATA → BUFFER_CHECK → 
PREPROCESS (filtrare, FFT) → RN_INFERENCE → THRESHOLD_CHECK → 
  ├─ [Normal] → LOG_RESULT → UPDATE_DASHBOARD → COLLECT_SENSOR_DATA (loop)
  └─ [Anomalie] → TRIGGER_ALERT → NOTIFY_OPERATOR → LOG_INCIDENT → 
                  COLLECT_SENSOR_DATA (loop)
       ↓ [User stop / Emergency]
     SAFE_SHUTDOWN → STOP
```
#### B. Clasificare imagini defecte producție (suduri, suprafețe, piese):
```
IDLE → WAIT_TRIGGER (senzor trecere piesă) → CAPTURE_IMAGE → 
VALIDATE_IMAGE (blur check, brightness) → 
  ├─ [Valid] → PREPROCESS (resize, normalize) → RN_INFERENCE → 
              CLASSIFY_DEFECT → 
                ├─ [OK] → LOG_OK → CONVEYOR_PASS → IDLE
                └─ [DEFECT] → LOG_DEFECT → TRIGGER_REJECTION → IDLE
  └─ [Invalid] → ERROR_IMAGE_QUALITY → RETRY_CAPTURE (max 3×) → IDLE
       ↓ [Shift end]
     GENERATE_REPORT → STOP
```
#### C. Predicție traiectorii robot mobil (AGV, AMR în depozit):
```
IDLE → LOAD_MAP → RECEIVE_TARGET → PLAN_PATH → 
VALIDATE_PATH (obstacle check) →
  ├─ [Clear] → EXECUTE_SEGMENT → ACQUIRE_SENSORS (LIDAR, IMU) → 
              RN_PREDICT_NEXT_STATE → UPDATE_TRAJECTORY → 
                ├─ [Target reached] → STOP_AT_TARGET → LOG_MISSION → IDLE
                └─ [In progress] → EXECUTE_SEGMENT (loop)
  └─ [Obstacle detected] → REPLAN_PATH → VALIDATE_PATH
       ↓ [Emergency stop / Battery low]
     SAFE_STOP → LOG_STATUS → STOP
```
#### D. Predicție consum energetic (turbine eoliene, procese batch):
```
IDLE → LOAD_HISTORICAL_DATA → ACQUIRE_CURRENT_CONDITIONS 
(vânt, temperatură, demand) → PREPROCESS_FEATURES → 
RN_FORECAST (24h ahead) → VALIDATE_FORECAST (sanity checks) →
  ├─ [Valid] → DISPLAY_FORECAST → UPDATE_CONTROL_STRATEGY → 
              LOG_PREDICTION → WAIT_INTERVAL (1h) → 
              ACQUIRE_CURRENT_CONDITIONS (loop)
  └─ [Invalid] → ERROR_FORECAST → USE_FALLBACK_MODEL → LOG_ERROR → 
                ACQUIRE_CURRENT_CONDITIONS (loop)
       ↓ [User request report]
     GENERATE_DAILY_REPORT → STOP
```
**Notă pentru proiecte simple:**
Chiar dacă aplicația voastră este o clasificare simplă (user upload → classify → display), trebuie să modelați fluxul ca un State Machine. Acest exercițiu vă învață să gândiți modular și să anticipați toate stările posibile (inclusiv erori).
**Legendă obligatorie (scrieți în README):**
```markdown
### Justificarea State Machine-ului ales:
Am ales arhitectura [descrieți tipul: monitorizare continuă / clasificare la senzor / 
predicție batch / control în timp real] pentru că proiectul nostru [explicați nevoia concretă 
din tabelul Secțiunea 1].
Stările principale sunt:
1. [STARE_1]: [ce se întâmplă aici - ex: "achiziție 1000 samples/sec de la accelerometru"]
2. [STARE_2]: [ce se întâmplă aici - ex: "calcul FFT și extragere 50 features frecvență"]
3. [STARE_3]: [ce se întâmplă aici - ex: "inferență RN cu latență < 50ms"]
...
Tranzițiile critice sunt:
- [STARE_A] → [STARE_B]: [când se întâmplă - ex: "când buffer-ul atinge 1024 samples"]
- [STARE_X] → [ERROR]: [condiții - ex: "când senzorul nu răspunde > 100ms"]
Starea ERROR este esențială pentru că [explicați ce erori pot apărea în contextul 
aplicației voastre industriale - ex: "senzorul se poate deconecta în mediul industrial 
cu vibrații și temperatură variabilă, trebuie să gestionăm reconnect automat"].
Bucla de feedback [dacă există] funcționează astfel: [ex: "rezultatul inferenței 
actualizează parametrii controlerului PID pentru reglarea vitezei motorului"].
```
### Justificarea State Machine-ului ales:

Am ales o arhitectură **hibridă (Procesare la cerere pentru Imagini / Monitorizare continuă pentru Video)**, pentru că proiectul nostru **trebuie să acopere două scenarii de utilizare distincte: auditul punctual al unor fotografii de la fața locului și supravegherea automată în timp real a fluxurilor video.**

Stările principale sunt:
1. **[INIT_SYSTEM]**: **Inițializarea mediului: încărcarea modelului YOLOv8 în VRAM și randarea interfeței grafice (UI) cu selectorul de sursă.**
2. **[INPUT_HANDLING]**: **Starea de așteptare și validare a input-ului: utilizatorul încarcă o imagine (JPG/PNG) sau selectează o sursă video (MP4/Webcam).**
3. **[INFERENCE_CORE]**: **Nucleul de procesare comun: redimensionare la 640px, rularea rețelei neuronale și (doar pentru video) aplicarea algoritmului de tracking pe axa timpului.**
4. **[RESULT_RENDERING]**: **Afișarea rezultatului final: suprapunerea bounding box-urilor peste imaginea originală sau redarea stream-ului procesat cu FPS constant.**

Tranzițiile critice sunt:
- **[INPUT_HANDLING]** → **[INFERENCE_CORE]**: **Când un fișier este încărcat complet și formatul este validat (ex: nu e un fișier text redenumit .jpg).**
- **[INFERENCE_CORE]** → **[ERROR]**: **Când modelul nu poate procesa matricea de pixeli (ex: fișier corupt sau dimensiuni atipice).**

Starea ERROR este esențială pentru că **utilizatorii pot încărca din greșeală fișiere nesuportate sau corupte, iar aplicația trebuie să afișeze un mesaj de avertizare ("Format invalid") și să permită o nouă încărcare, fără a se închide forțat.**

Bucla de feedback funcționează astfel: **Utilizatorul vizualizează rezultatul (poza sau video-ul procesat) și, dacă observă omisiuni, ajustează slider-ul de confidență, ceea ce forțează re-intrarea în starea [RESULT_RENDERING] cu noii parametri, fără a reîncărca fișierul.**

---
### 4. Scheletul Complet al celor 3 Module Cerute la Curs (slide 7)
Toate cele 3 module trebuie să **pornească și să ruleze fără erori** la predare. Nu trebuie să fie perfecte, dar trebuie să demonstreze că înțelegeți arhitectura.
| **Modul** | **Python (exemple tehnologii)** | **LabVIEW** | **Cerință minimă funcțională (la predare)** |
|-----------|----------------------------------|-------------|----------------------------------------------|
| **1. Data Logging / Acquisition** | `src/data_acquisition/` | LLB cu VI-uri de generare/achiziție | **MUST:** Produce CSV cu datele voastre (inclusiv cele 40% originale). Cod rulează fără erori și generează minimum 100 samples demonstrative. |
| **2. Neural Network Module** | `src/neural_network/model.py` sau folder dedicat | LLB cu VI-uri RN | **MUST:** Modelul RN definit, compilat, poate fi încărcat. **NOT required:** Model antrenat cu performanță bună (poate avea weights random/inițializați). |
| **3. Web Service / UI** | Streamlit, Gradio, FastAPI, Flask, Dash | WebVI sau Web Publishing Tool | **MUST:** Primește input de la user și afișează un output. **NOT required:** UI frumos, funcționalități avansate. |

#### Detalii per modul:
#### **Modul 1: Data Logging / Acquisition**
**Funcționalități obligatorii:**
- [X] Cod rulează fără erori: `python src/data_acquisition/generate.py` sau echivalent LabVIEW
- [X] Generează CSV în format compatibil cu preprocesarea din Etapa 3
- [X] Include minimum 40% date originale în dataset-ul final
- [X] Documentație în cod: ce date generează, cu ce parametri
#### **Modul 2: Neural Network Module**
**Funcționalități obligatorii:**
- [X] Arhitectură RN definită și compilată fără erori
- [X] Model poate fi salvat și reîncărcat
- [X] Include justificare pentru arhitectura aleasă (în docstring sau README)
- [X] **NU trebuie antrenat** cu performanță bună (weights pot fi random)
#### **Modul 3: Web Service / UI**
**Funcționalități MINIME obligatorii:**
- [X] Propunere Interfață ce primește input de la user (formular, file upload, sau API endpoint)
- [X] Includeți un screenshot demonstrativ în `docs/screenshots/`
**Ce NU e necesar în Etapa 4:**
- UI frumos/profesionist cu grafică avansată
- Funcționalități multiple (istorice, comparații, statistici)
- Predicții corecte (modelul e neantrenat, e normal să fie incorect)
- Deployment în cloud sau server de producție
**Scop:** Prima demonstrație că pipeline-ul end-to-end funcționează: input user → preprocess → model → output.
## Structura Repository-ului la Finalul Etapei 4 (OBLIGATORIE)
**Verificare consistență cu Etapa 3:**
```
proiect-rn-[nume-prenume]/
├── data/
│   ├── raw/
│   ├── processed/
│   ├── generated/  # Date originale
│   ├── train/
│   ├── validation/
│   └── test/
├── src/
│   ├── data_acquisition/
│   ├── preprocessing/  # Din Etapa 3
│   ├── neural_network/
│   └── app/  # UI schelet
├── docs/
│   ├── state_machine.*           #(state_machine.png sau state_machine.pptx sau state_machine.drawio)
│   └── [alte dovezi]
├── models/  # Untrained model
├── config/
├── README.md
├── README_Etapa3.md              # (deja existent)
├── README_Etapa4_Arhitectura_SIA.md              # ← acest fișier completat (în rădăcină)
└── requirements.txt  # Sau .lvproj
```
**Diferențe față de Etapa 3:**
- Adăugat `data/generated/` pentru contribuția dvs originală
- Adăugat `src/data_acquisition/` - MODUL 1
- Adăugat `src/neural_network/` - MODUL 2
- Adăugat `src/app/` - MODUL 3
- Adăugat `models/` pentru model neantrenat
- Adăugat `docs/state_machine.png` - OBLIGATORIU
- Adăugat `docs/screenshots/` pentru demonstrație UI
---
## Checklist Final – Bifați Totul Înainte de Predare
### Documentație și Structură
- [X] Tabelul Nevoie → Soluție → Modul complet (minimum 2 rânduri cu exemple concrete completate in README_Etapa4_Arhitectura_SIA.md)
- [X] Declarație contribuție 40% date originale completată în README_Etapa4_Arhitectura_SIA.md
- [X] Cod generare/achiziție date funcțional și documentat
- [X] Dovezi contribuție originală: grafice + log + statistici în `docs/`
- [X] Diagrama State Machine creată și salvată în `docs/state_machine.*`
- [X] Legendă State Machine scrisă în README_Etapa4_Arhitectura_SIA.md (minimum 1-2 paragrafe cu justificare)
- [X] Repository structurat conform modelului de mai sus (verificat consistență cu Etapa 3)
### Modul 1: Data Logging / Acquisition
- [X] Cod rulează fără erori (`python src/data_acquisition/...` sau echivalent LabVIEW)
- [X] Produce minimum 40% date originale din dataset-ul final
- [X] CSV generat în format compatibil cu preprocesarea din Etapa 3
- [X] Documentație în `src/data_acquisition/README.md` cu:
  - [X] Metodă de generare/achiziție explicată
  - [X] Parametri folosiți (frecvență, durată, zgomot, etc.)
  - [X] Justificare relevanță date pentru problema voastră
- [X] Fișiere în `data/generated/` conform structurii
### Modul 2: Neural Network
- [X] Arhitectură RN definită și documentată în cod (docstring detaliat) - versiunea inițială 
- [X] README în `src/neural_network/` cu detalii arhitectură curentă
### Modul 3: Web Service / UI
- [X] Propunere Interfață ce pornește fără erori (comanda de lansare testată)
- [X] Screenshot demonstrativ în `docs/screenshots/ui_demo.png`
- [X] README în `src/app/` cu instrucțiuni lansare (comenzi exacte)
---
**Predarea se face prin commit pe GitHub cu mesajul:**  
`"Etapa 4 completă - Arhitectură SIA funcțională"`
**Tag obligatoriu:**  
`git tag -a v0.4-architecture -m "Etapa 4 - Skeleton complet SIA"`






