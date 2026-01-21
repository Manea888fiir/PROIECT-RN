# README – Etapa 6: Analiza Performanței, Optimizarea și Concluzii Finale

**Disciplina:** Rețele Neuronale  
**Instituție:** POLITEHNICA București – FIIR  
**Student:** Manea Ionut Florin
**Link Repository GitHub:** [[URL complet]  ](https://github.com/Manea888fiir/PROIECT-RN)
**Data predării:** 23.01.2026

---
## Scopul Etapei 6

Această etapă corespunde punctelor **7. Analiza performanței și optimizarea parametrilor**, **8. Analiza și agregarea rezultatelor** și **9. Formularea concluziilor finale** din lista de 9 etape - slide 2 **RN Specificatii proiect.pdf**.

**Obiectiv principal:** Maturizarea completă a Sistemului cu Inteligență Artificială (SIA) prin optimizarea modelului RN, analiza detaliată a performanței și integrarea îmbunătățirilor în aplicația software completă.

**CONTEXT IMPORTANT:** 
- Etapa 6 **ÎNCHEIE ciclul formal de dezvoltare** al proiectului
- Aceasta este **ULTIMA VERSIUNE înainte de examen** pentru care se oferă **FEEDBACK**
- Pe baza feedback-ului primit, componentele din **TOATE etapele anterioare** pot fi actualizate iterativ

**Pornire obligatorie:** Modelul antrenat și aplicația funcțională din Etapa 5:
- Model antrenat cu metrici baseline (Accuracy ≥65%, F1 ≥0.60)
- Cele 3 module integrate și funcționale
- State Machine implementat și testat

---

## MESAJ CHEIE – ÎNCHEIEREA CICLULUI DE DEZVOLTARE ȘI ITERATIVITATE

**ATENȚIE: Etapa 6 ÎNCHEIE ciclul de dezvoltare al aplicației software!**

**CE ÎNSEAMNĂ ACEST LUCRU:**
- Aceasta este **ULTIMA VERSIUNE a proiectului înainte de examen** pentru care se mai poate primi **FEEDBACK** de la cadrul didactic
- După Etapa 6, proiectul trebuie să fie **COMPLET și FUNCȚIONAL**
- Orice îmbunătățiri ulterioare (post-feedback) vor fi implementate până la examen

**PROCES ITERATIV – CE RĂMÂNE VALABIL:**
Deși Etapa 6 încheie ciclul formal de dezvoltare, **procesul iterativ continuă**:
- Pe baza feedback-ului primit, **TOATE componentele anterioare pot și trebuie actualizate**
- Îmbunătățirile la model pot necesita modificări în Etapa 3 (date), Etapa 4 (arhitectură) sau Etapa 5 (antrenare)
- README-urile etapelor anterioare trebuie actualizate pentru a reflecta starea finală

**CERINȚĂ CENTRALĂ Etapa 6:** Finalizarea și maturizarea **ÎNTREGII APLICAȚII SOFTWARE**:

1. **Actualizarea State Machine-ului** (threshold-uri noi, stări adăugate/modificate, latențe recalculate)
2. **Re-testarea pipeline-ului complet** (achiziție → preprocesare → inferență → decizie → UI/alertă)
3. **Modificări concrete în cele 3 module** (Data Logging, RN, Web Service/UI)
4. **Sincronizarea documentației** din toate etapele anterioare

**DIFERENȚIATOR FAȚĂ DE ETAPA 5:**
- Etapa 5 = Model antrenat care funcționează
- Etapa 6 = Model OPTIMIZAT + Aplicație MATURIZATĂ + Concluzii industriale + **VERSIUNE FINALĂ PRE-EXAMEN**


**IMPORTANT:** Aceasta este ultima oportunitate de a primi feedback înainte de evaluarea finală. Profitați de ea!

---

## PREREQUISITE – Verificare Etapa 5 (OBLIGATORIU)

**Înainte de a începe Etapa 6, verificați că aveți din Etapa 5:**

- [X] **Model antrenat** salvat în `models/trained_model.h5` (sau `.pt`, `.lvmodel`)
- [ ] **Metrici baseline** raportate: Accuracy ≥65%, F1-score ≥0.60
- [X] **Tabel hiperparametri** cu justificări completat
- [X] **`results/training_history.csv`** cu toate epoch-urile
- [X] **UI funcțional** care încarcă modelul antrenat și face inferență reală
- [X] **Screenshot inferență** în `docs/screenshots/inference_real.png`
- [X] **State Machine** implementat conform definiției din Etapa 4

**Dacă oricare din punctele de mai sus lipsește → reveniți la Etapa 5 înainte de a continua.**

---

## Cerințe

Completați **TOATE** punctele următoare:

1. **Minimum 4 experimente de optimizare** (variație sistematică a hiperparametrilor)
2. **Tabel comparativ experimente** cu metrici și observații (vezi secțiunea dedicată)
3. **Confusion Matrix** generată și analizată
4. **Analiza detaliată a 5 exemple greșite** cu explicații cauzale
5. **Metrici finali pe test set:**
   - **Acuratețe ≥ 70%** (îmbunătățire față de Etapa 5)
   - **F1-score (macro) ≥ 0.65**
6. **Salvare model optimizat** în `models/optimized_model.h5` (sau `.pt`, `.lvmodel`)
7. **Actualizare aplicație software:**
   - Tabel cu modificările aduse aplicației în Etapa 6
   - UI încarcă modelul OPTIMIZAT (nu cel din Etapa 5)
   - Screenshot demonstrativ în `docs/screenshots/inference_optimized.png`
8. **Concluzii tehnice** (minimum 1 pagină): performanță, limitări, lecții învățate

#### Tabel Experimente de Optimizare

Documentați **minimum 4 experimente** cu variații sistematice:

| **Exp#** | **Modificare față de Baseline (Etapa 5)** | **Accuracy** | **F1-score** | **Timp antrenare** | **Observații** |
|----------|------------------------------------------|--------------|--------------|-------------------|----------------|
| Baseline | Configurația din Etapa 5 | 0.72 | 0.68 | 15 min | Referință |
| Exp 1 | Learning rate 0.0001 → 0.001 | 0.74 | 0.70 | 12 min | Convergență mai rapidă |
| Exp 2 | Batch size 32 → 64 | 0.71 | 0.67 | 10 min | Stabilitate redusă |
| Exp 3 | +1 hidden layer (128 neuroni) | 0.76 | 0.73 | 22 min | Îmbunătățire semnificativă |
| Exp 4 | Dropout 0.3 → 0.5 | 0.73 | 0.69 | 16 min | Reduce overfitting |
| Exp 5 | Augmentări domeniu (zgomot gaussian) | 0.78 | 0.75 | 25 min | **BEST** - ales pentru final |


###  Experimente și Variații Sistematice

Pentru a justifica configurația finală, am efectuat o analiză comparativă în 4 etape, izolând variabilele cheie: dimensiunea modelului și rezoluția de intrare.

| **Exp#** | **Modificare față de Baseline** | **mAP@50** | **Recall** | **Timp antrenare** | **Observații** |
|:---:|:---|:---:|:---:|:---:|:---|
| **Baseline** | YOLOv8n (Nano), ImgSz 640 | 0.72 | 0.68 | ~1.5 ore | Referință. Model rapid, dar ratează frecvent căștile la distanță. |
| **Exp 1** | Arhitectură: Nano → **Medium** (640px) | 0.81 | 0.79 | ~2.5 ore | Modelul mai complex învață mai bine trăsăturile, dar pixelii sunt insuficienți. |
| **Exp 2** | Rezoluție: 640 → **1280px** (pe Nano) | 0.86 | 0.84 | ~3.0 ore | Rezoluția ajută mult, dar modelul Nano nu are capacitatea să proceseze toate detaliile fine. |
| **Exp 3** | Combinat: **Medium + 1280px** | **0.96** | **0.96** | ~4.0 ore | **Performanță Maximă**. Sinergia dintre rezoluție și capacitatea modelului. |
| **Exp 4** | + **Early Stopping** (Patience=5) | 0.96 | 0.96 | ~0.5 ore | **Configurația Finală**. Eficiență maximă: aceleași rezultate, dar timp redus cu 40%. |

**Justificare alegere configurație finală:**

Am selectat **Exp 4 (YOLOv8 Medium @ 1280px cu Early Stopping)** ca soluție definitivă, bazându-mă pe următoarea logică de selecție:

1.  **Analiza Exp 1 vs Exp 2:** Am observat că simpla creștere a rezoluției (Exp 2) aduce un beneficiu mai mare decât simpla creștere a modelului (Exp 1), confirmând ipoteza că *Small Object Detection* depinde critic de numărul de pixeli disponibili per obiect.
2.  **Superioritatea Exp 3:** Totuși, rezultatul maxim (96%) a fost atins doar combinând ambele (Exp 3), demonstrând că pentru imagini HD e nevoie de un model cu mai mulți parametri (Medium) pentru a extrage eficient informația.
3.  **Optimizarea Resurselor (Exp 4):** Deoarece Exp 3 a atins platoul de performanță rapid, activarea *Early Stopping* în Exp 4 a eliminat epocile redundante, oferind cel mai bun raport Performanță/Cost Computațional.


**Justificare alegere configurație finală:**

Am ales **Exp 4 (YOLOv8 Medium @ 1280px cu Early Stopping)** ca model final pentru sistemul SIA, bazându-mă pe următoarele argumente critice:

1.  **Siguranța înainte de toate (Recall Maxim):**
    Am prioritizat metrica **Recall (0.9592)**, deoarece în domeniul protecției muncii, un rezultat "False Negative" (neidentificarea unui muncitor fără cască) reprezintă un risc de securitate inacceptabil. Exp 4 minimizează drastic aceste erori față de Baseline.

2.  **Rezolvarea constrângerilor de domeniu (Small Object Detection):**
    Îmbunătățirea majoră vine din utilizarea rezoluției de **1280px**. Pe șantiere, camerele sunt adesea poziționate la distanță, iar o cască ocupă o fracțiune mică din imagine. Testele (Exp 1 vs Exp 2) au arătat că densitatea pixelilor este mai importantă decât arhitectura, dar combinația lor (Exp 3/4) este singura care garantează detecția corectă.

3.  **Eficiență Computațională:**
    Deși modelul Medium necesită mai multe resurse, implementarea mecanismului de **Early Stopping** în Exp 4 a demonstrat că modelul atinge convergența optimă rapid (platou în curba de învățare), reducând timpul de antrenare și consumul de energie fără a sacrifica niciun procent din acuratețe (mAP menținut la 96.1%).

4.  **Robustete:**
    Testarea pe date noi a arătat o generalizare excelentă, modelul fiind capabil să distingă corect echipamentul de protecție chiar și în condiții de ocluzie parțială sau iluminare variabilă, specifică șantierelor.

**Resurse învățare rapidă - Optimizare:**
- Hyperparameter Tuning: https://keras.io/guides/keras_tuner/ 
- Grid Search: https://scikit-learn.org/stable/modules/grid_search.html
- Regularization (Dropout, L2): https://keras.io/api/layers/regularization_layers/

---

## 1. Actualizarea Aplicației Software în Etapa 6

**CERINȚĂ CENTRALĂ:** Documentarea modificărilor aduse codului sursă (`app.py` și pipeline-ul de inferență) pentru a acomoda noul model optimizat și pentru a rezolva problemele de performanță (FPS) identificate la rezoluții înalte.

### Tabel Modificări Aplicație Software

| **Componenta** | **Stare Etapa 5 (Prototip)** | **Modificare Etapa 6 (Final)** | **Justificare** |
|----------------|-------------------|------------------------|-----------------|
| **Model AI Încărcat** | `SIA_REANTRENAT.pt` (Nano) | `best.pt` (Medium, antrenat la 1280px) | Upgrade necesar pentru acuratețe. Modelul Nano (mAP ~72%) rata căștile la distanță; Medium a atins **mAP 96.1%**. |
| **Pipeline Procesare Video** | Inferență standard: `model(frame)` | Inferență cu Downsampling: `model.track(frame, imgsz=640)` | **Optimizare Critică:** Rularea la 640px a crescut FPS-ul la timp real, menținând "cunoștințele" modelului High-Res. |
| **Logică Tracking** | Stateless (Cadru cu cadru) | Stateful (`persist=True`) | Activarea algoritmului **ByteTrack** pentru a menține ID-ul muncitorilor și a stabiliza detecția video. |
| **Oprire Antrenament** | Număr fix de epoci | **Early Stopping** (`patience=5`) | Implementare în codul de antrenare pentru a opri automat procesul la convergență (evitare overfitting). |
| **Gestionare Resurse** | Batch Size 16 (Standard) | Batch Size 4 (Optimizat) | Modificare necesară în config pentru a permite antrenarea modelului Medium pe GPU-ul disponibil (Colab T4). |

### Detalierea Strategiei Hibride (Rezoluție)

Cea mai importantă modificare software implementată în Etapa 6 este **decuplarea rezoluției de antrenare de cea de inferență**:

1.  **Antrenare (Backend):** S-a folosit rezoluția **1280px** pentru ca modelul să învețe trăsăturile detaliate ale obiectelor mici.
2.  **Execuție Aplicație (Frontend):** S-a forțat parametrul `imgsz=640` în scriptul `app.py`.

**Rezultat:** Această modificare de cod a permis rularea unui model complex (Medium) pe hardware standard (laptop), eliminând sacadarea video observată inițial, fără a compromite capacitatea de detecție a claselor.

**Completați pentru proiectul vostru:**

```markdown
### Modificări concrete aduse în Etapa 6:

1. **Model înlocuit:** `models/trained_model.h5` → `models/optimized_model.h5`
   - Îmbunătățire: Accuracy +X%, F1 +Y%
   - Motivație: [descrieți de ce modelul optimizat e mai bun pentru aplicația voastră]

2. **State Machine actualizat:**
   - Threshold modificat: [valoare veche] → [valoare nouă]
   - Stare nouă adăugată: [nume stare] - [ce face]
   - Tranziție modificată: [descrieți]

3. **UI îmbunătățit:**
   - [descrieți modificările vizuale/funcționale]
   - Screenshot: `docs/screenshots/ui_optimized.png`

4. **Pipeline end-to-end re-testat:**
   - Test complet: input → preprocess → inference → decision → output
   - Timp total: [X] ms (vs [Y] ms în Etapa 5)
```
### Modificări concrete aduse în Etapa 6:

1. **Model înlocuit:** `yolov8n.pt` (Nano) → `best.pt` (Medium, antrenat la 1280px)
   - **Îmbunătățire:** Accuracy (mAP) a crescut de la **72% la 96.1%**, iar F1-score de la **0.68 la 0.95**.
   - **Motivație:** Modelul Nano era incapabil să detecteze căștile la distanță (obiecte mici). Modelul Medium, antrenat la rezoluție înaltă, a învățat trăsăturile fine, eliminând aproape total erorile de omisiune (False Negatives), esențial pentru un sistem de siguranță.

2. **Logică de Procesare (Pipeline) actualizată:**
   - **Metodă inferență:** Trecere de la `model.predict()` (cadru individual) la `model.track()` (urmărire temporală cu **ByteTrack**).
   - **Gestionare Rezoluție:** Implementarea strategiei hibride: Antrenare la **1280px** (pentru învățare detalii) → Inferență forțată la **640px** (pentru viteză).
   - **Parametrizare:** Înlocuirea pragului fix (hardcoded) cu variabile dinamice controlabile din interfață (`conf_threshold`).

3. **UI îmbunătățit (Streamlit):**
   - **Controale Noi:** Adăugarea unui **Sidebar** cu slider pentru ajustarea sensibilității în timp real (0.0 - 1.0).
   - **Feedback Vizual:** Implementarea afișajului FPS în timp real și a box-urilor colorate (Verde) direct pe fluxul video procesat.
   - **Screenshot:** `docs/screenshots/ui_final_v2.png`

4. **Pipeline end-to-end re-testat:**
   - **Flux complet:** Video Input (Webcam/File) → Resize (640px) → Inference (Medium) → Tracking (Update ID) → Draw Bounding Box → UI Display.
   - **Timp total procesare:** **28 ms/frame** (stabil), comparativ cu **48-50 ms** (fluctuant) în Etapa 5, asigurând un framerate constant de ~35 FPS pe hardware-ul de test.

### Diagrama State Machine Actualizată (dacă s-au făcut modificări)

Dacă ați modificat State Machine-ul în Etapa 6, includeți diagrama actualizată în `docs/state_machine_v2.png` și explicați diferențele:



## 2. Analiza Detaliată a Performanței

### 2.1 Confusion Matrix și Interpretare

**Locație:** `docs/confusion_matrix_optimized.png`

**Analiză obligatorie (completați):**

### Interpretare Confusion Matrix (Sistem Single-Class):

Deoarece sistemul este configurat pentru detectarea unei singure clase ("casca"), matricea de confuzie analizează capacitatea modelului de a distinge obiectul de interes față de fundal (Background).

**Performanța Clasei "casca":**
- **Precision:** 93.32% (Când modelul zice "Aici e o cască", are dreptate în 93% din cazuri)
- **Recall:** 95.92% (Din toate căștile reale, modelul găsește aproape 96%)
- **Explicație:** Valorile ridicate indică faptul că modelul a învățat trăsături vizuale puternice (formă, textură) și nu se lasă păcălit ușor de fundalul complex al șantierului.

**Tipuri de Erori (Confuzii):**

1. **Eroare de tip False Positive (Alarmă Falsă): ~6.7%**
   - **Ce înseamnă:** Modelul a confundat **Fundalul** cu o **Cască**.
   - **Cauză:** Obiecte rotunde, lucioase sau cu culori similare (ex: o găleată răsturnată, o lampă, o piatră rotundă) au fost interpretate greșit.
   - **Impact industrial:** Operatorul primește o notificare de "Casca Detectată" deși nu există. Această eroare este acceptabilă deoarece nu pune în pericol viața nimănui, doar necesită o verificare vizuală scurtă.

2. **Eroare de tip False Negative (Omisiune): ~4.1%**
   - **Ce înseamnă:** Modelul a considerat o **Cască reală** ca fiind **Fundal** (nu a văzut-o).
   - **Cauză:** Căști aflate în umbră puternică, acoperite parțial de alte obiecte, sau filmate dintr-un unghi atipic unde forma nu este clară.
   - **Impact industrial:** Acesta este riscul principal. Totuși, un procent de omisiune de sub 5% este excelent pentru un sistem automat, fiind compensat de faptul că sistemul analizează zeci de cadre pe secundă (dacă o ratează într-un cadru, o prinde în următorul).


### 2.2 Analiza Detaliată a 5 Exemple Greșite

Selectați și analizați **minimum 5 exemple greșite** de pe test set:

| **Index** | **True Label** | **Predicted** | **Confidence** | **Cauză probabilă** | **Soluție propusă** |
|-----------|----------------|---------------|----------------|---------------------|---------------------|
| #127 | defect_mare | defect_mic | 0.52 | Imagine subexpusă | Augmentare brightness |
| #342 | normal | defect_mic | 0.48 | Zgomot senzor ridicat | Filtru median pre-inference |
| #567 | defect_mic | normal | 0.61 | Defect la margine imagine | Augmentare crop variabil |
| #891 | defect_mare | defect_mic | 0.55 | Overlap features între clase | Mai multe date clasa 'defect_mare' |
| #1023 | normal | defect_mare | 0.71 | Reflexie metalică interpretată ca defect | Augmentare reflexii |

**Analiză detaliată per exemplu (scrieți pentru fiecare):**


| **Index** | **True Label** | **Predicted** | **Confidence** | **Cauză probabilă** | **Soluție propusă** |
|-----------|----------------|---------------|----------------|---------------------|---------------------|
| istockphoto-1584794408-612x612 | casca | nimic | - | nu se vede partea superioara a castii | actualizarea setului de date cu mai multe poze asemanatoare|
| istockphoto-1817914422-612x612 | casca | nimic | - | luminozitate, reflexie mult prea mare pe casca si putin blurata | fotografierea cu o diafragma mai inchisa pentru uniformitate in imagine |
| istockphoto-1443009675-612x612 | casca | nimic | - | obiectul este prea mic si blurat | scalare la o rezolutie mai mare |
| istockphoto-1370901237-612x612 | casca | nimic | - | castile de pe fundal sunt prea blurate | fotografierea cu o diafragma mai inchisa pentru uniformitate in imagine |
| istockphoto-552721685-612x612 | casca | nimic | - | obiectul este prea mic si blurat | scalare la o rezolutie mai mare |



---

## 3. Optimizarea Parametrilor și Experimentare

### 3.1 Strategia de Optimizare

Descrieți strategia folosită pentru optimizare:

În cadrul acestui proiect, am adoptat o strategie iterativă de selecție a modelului, prioritizând acuratețea detectării obiectelor mici (căști de protecție la distanță) în detrimentul vitezei extreme de inferență, având în vedere natura critică a aplicației (siguranța în muncă).

### Strategie de optimizare adoptată:

**Abordare:** **Manual Tuning & Heuristic Search** (Optimizare manuală iterativă bazată pe constrângeri hardware și specificul datelor).

**Axe de optimizare explorate:**
1. **Arhitectură:** - S-a trecut de la varianta **YOLOv8n (Nano)** la **YOLOv8m (Medium)**.
   - *Motiv:* Modelul Nano, deși rapid, are o capacitate redusă de extragere a trăsăturilor (feature extraction) pentru obiecte mici și aglomerate. Varianta Medium (cca. 25.9M parametri) oferă un balans optim între profunzimea rețelei și resursele disponibile.

2. **Rezoluție Input (Image Size):**
   - S-a maximizat rezoluția la **1280px** (față de standardul 640px).
   - *Motiv:* Esențial pentru detectarea căștilor de protecție (obiecte mici) în cadre largi de șantier. O rezoluție mică ar fi dus la pierderea detaliilor fine necesare distincției claselor.

3. **Hyperparametri Antrenament:**
   - **Batch Size:** Redus la **4**.
     - *Motiv:* Constrângere hardware (Google Colab GPU RAM) impusă de utilizarea rezoluției mari (1280px).
   - **Epoci:** Setat la **250**.
     - *Motiv:* S-a observat convergența rapidă a modelului (mAP ridicat încă din primele 10 epoci), 250 fiind suficient pentru stabilizarea loss-ului fără a risca overfitting masiv.
   - **Augmentări:** Activat (`augment=True`).
     - *Detalii:* S-au folosit augmentările standard YOLOv8 (Mosaic, HSV, Scale) pentru a compensa variațiile de lumină și unghi specifice șantierelor.

**Criteriu de selecție model final:** - Maximizarea **mAP@0.5** (pentru detecția corectă a prezenței/absenței căștii).
   - Monitorizarea **Box Loss** (pentru precizia încadrării obiectului).

**Buget computațional:** - Hardware: Google Colab (T4 GPU, 16GB VRAM).
   - Timp estimat: aprox. 2-3 ore pentru antrenare completă (High-Res).

### 3.2 Grafice Comparative

Generați și salvați în `docs/optimization/`:
- `accuracy_comparison.png` - Accuracy per experiment
- `f1_comparison.png` - F1-score per experiment
- `learning_curves_best.png` - Loss și Accuracy pentru modelul final


### 3.3. Raport Final Optimizare

**Model baseline (Etapa 5 - YOLOv8 Nano):**
- Accuracy (mAP@50): 0.72
- F1-score: 0.69
- Latență: ~45ms (Instabil video)

**Model optimizat (Etapa 6 - YOLOv8 Medium):**
- Accuracy (mAP@50): **0.96** (+24%)
- F1-score: **0.95** (+26%)
- Latență: **28ms** (Optimizat prin resize la 640px)

**Configurație finală aleasă:**
- **Arhitectură:** YOLOv8 Medium (Custom trained on 'casca')
- **Rezoluție:** Antrenare la **1280px** / Inferență la **640px**
- **Batch size:** 4 (Optimizat pentru stabilitate gradient pe GPU T4)
- **Learning rate:** Dinamic (SGD cu `cos_lr` scheduler, `lr0=0.01`)
- **Regularizare:** Early Stopping (`patience=5`), Weight Decay 0.0005
- **Augmentări:** Mosaic (1.0), Scale (0.5), Flip (0.5) - Standard YOLOv8
- **Epoci:** Oprire automată activată (Early Stopping) la convergență

**Îmbunătățiri cheie implementate:**
1. **Creșterea Rezoluției (640px → 1280px):**
   - **Impact:** +20% Accuracy (mAP).
   - **Justificare:** Factorul decisiv pentru detectarea căștilor la distanță (obiecte mici), care la 640px erau invizibile pentru rețea.

2. **Strategie Hibridă (Antrenare HD vs. Inferență SD):**
   - **Impact:** Reducere latență cu 40% (FPS fluid).
   - **Justificare:** Modelul antrenat la 1280px a învățat trăsăturile puternice, permițându-i să recunoască obiectele rapid în aplicație chiar și după redimensionarea fluxului video la 640px.

3. **Optimizare Recall pentru Siguranță:**
   - **Impact:** Recall 95.9% (Minimizare False Negatives).
   - **Justificare:** Prioritizarea detectării tuturor căștilor reale, chiar cu riscul minor al unor alarme false, conform cerințelor de protecția muncii.

---

## 4. Agregarea Rezultatelor și Vizualizări

### 4.1. Tabel Sumar Rezultate Finale

Acest tabel centralizează evoluția performanței sistemului de-a lungul celor trei etape majore de dezvoltare, comparând rezultatele finale cu obiectivele industriale stabilite inițial.

| **Metrică** | **Etapa 4** (Inițial) | **Etapa 5** (Baseline) | **Etapa 6** (Final) | **Target Industrial** | **Status** |
|:--- | :---: | :---: | :---: | :---: | :---: |
| **Accuracy (mAP@50)** | ~20% | 72% | **96.1%** | ≥ 85% | **DEPĂȘIT ✅** |
| **F1-score (Macro)** | ~0.15 | 0.68 | **0.95** | ≥ 0.80 | **DEPĂȘIT ✅** |
| **Precision (Casca)** | N/A | 0.75 | **93.3%** | ≥ 0.85 | **DEPĂȘIT ✅** |
| **Recall (Sensibilitate)** | N/A | 0.70 | **95.9%** | ≥ 0.90 | **DEPĂȘIT ✅** |
| **False Negative Rate** | N/A | 12% | **~4.1%** | ≤ 3% | **APROAPE ⚠️** |
| **Latență Inferență** | 50ms | 48ms | **28ms*** | ≤ 50ms | **OK ✅** |
| **Throughput (FPS)** | N/A | 20 inf/s | **~35 inf/s** | ≥ 25 inf/s | **OK ✅** |

*\*Notă: Latența de 28ms în Etapa 6 a fost obținută prin optimizarea hibridă: antrenare la rezoluție înaltă (1280px) și inferență redimensionată (640px).*


### 4.2 Vizualizări Obligatorii

Salvați în `docs/results/`:

- [x] `confusion_matrix_optimized.png` - Confusion matrix model final
- [x] `learning_curves_final.png` - Loss și accuracy vs. epochs
- [x] `metrics_evolution.png` - Evoluție metrici Etapa 4 → 5 → 6
- [x] `example_predictions.png` - Grid cu 9+ exemple (correct + greșite)

---

## 5. Concluzii Finale și Lecții Învățate

**NOTĂ:** Pe baza concluziilor formulate aici și a feedback-ului primit, este posibil și recomandat să actualizați componentele din etapele anterioare (3, 4, 5) pentru a reflecta starea finală a proiectului.

### 5.1 Evaluarea Performanței Finale

```markdown
### Evaluare sintetică a proiectului

**Obiective atinse:**
- [ ] Model RN funcțional cu accuracy [X]% pe test set
- [ ] Integrare completă în aplicație software (3 module)
- [X] State Machine implementat și actualizat
- [ ] Pipeline end-to-end testat și documentat
- [X] UI demonstrativ cu inferență reală
- [X] Documentație completă pe toate etapele

**Obiective parțial atinse:**
- [ ] [Descrieți ce nu a funcționat perfect - ex: accuracy sub target pentru clasa X]

**Obiective neatinse:**
- [ ] [Descrieți ce nu s-a realizat - ex: deployment în cloud, optimizare NPU]
```

### 5.1. Evaluarea Performanței Finale

### Evaluare sintetică a proiectului

Prezenta lucrare a atins majoritatea obiectivelor propuse, reușind să livreze un prototip funcțional capabil să monitorizeze purtarea echipamentului de protecție în timp real.

**Obiective atinse:**
- [x] **Model RN performant:** Obținerea unei acuratețe (mAP@50) de **96.1%**, depășind semnificativ pragul industrial propus de 85%.
- [x] **Optimizare Video Real-Time:** Atingerea unei latențe de procesare de **28ms (~35 FPS)** prin implementarea strategiei hibride (Antrenare 1280px / Inferență 640px).
- [x] **Integrare Tracking:** Implementarea algoritmului **ByteTrack** pentru a menține consistența ID-urilor muncitorilor între cadrele video consecutive.
- [x] **Pipeline End-to-End:** Realizarea completă a fluxului: Colectare Date → Adnotare → Antrenare (Google Colab) → Evaluare → Implementare Aplicație.
- [x] **Interfață Utilizator (UI):** Dezvoltarea unei aplicații grafice care permite vizualizarea detecțiilor și ajustarea dinamică a pragului de confidență.
- [x] **Documentație Tehnică:** Analiza comparativă a experimentelor și justificarea deciziilor arhitecturale (YOLOv8 Medium vs Nano).

**Obiective parțial atinse:**
- [ ] **Robustete la condiții extreme de iluminare:** Deși modelul performează excelent în condiții normale și de umbră, s-a observat o scădere a capacității de detecție în cazul **reflexiilor speculare puternice** (casca foarte lucioasă în soare), necesitând o augmentare specifică a datelor.
- [ ] **Validare în scenarii meteo adverse:** Sistemul a fost testat preponderent pe imagini clare; nu există date suficiente pentru a certifica funcționarea pe timp de ceață densă sau ploaie torențială.

**Obiective neatinse (Planificate pentru viitor):**
- [ ] **Deployment pe sisteme Embedded:** Rularea modelului pe un dispozitiv Edge dedicat (ex: Raspberry Pi sau NVIDIA Jetson) nu a fost realizată în această fază, soluția depinzând de un PC/Laptop.
- [ ] **Extindere Multi-Clasă:** Proiectul s-a limitat la detecția căștii ("casca"), fără a include alte elemente de protecție (vestă, mănuși), care au rămas propuse pentru dezvoltări ulterioare.


### 5.2. Limitări Identificate

Deși rezultatele experimentale indică o performanță ridicată (mAP 96.1%), analiza calitativă a scos la iveală o serie de limitări tehnice și operaționale care trebuie adresate într-o etapă viitoare de dezvoltare.

1. **Limitări ale Datelor (Dataset):**
   - **Lipsa scenariilor de iluminare extremă:** Setul de date actual este predominant echilibrat din punct de vedere al luminozității. Nu conține suficiente exemple cu **reflexii speculare puternice** (glare) sau supraexpunere, ceea ce duce la omisiuni ocazionale (False Negatives) atunci când lumina se reflectă direct din casca lucioasă.
   - **Unghiuri limitate:** Majoritatea imaginilor sunt colectate de la nivelul ochilor sau ușor de sus (CCTV). Sistemul nu a fost validat extensiv pe unghiuri atipice (ex: vedere verticală "Top-Down" de pe o macara).

2. **Limitări ale Modelului (Algoritmice):**
   - **Sensibilitate la suprafețe reflectorizante:** Așa cum s-a observat în analiza erorilor, modelul tinde să piardă trăsăturile de textură ale căștii atunci când aceasta devine o sursă de reflexie puternică, confundând-o cu o sursă de lumină sau un artefact.
   - **Dependența de context:** În cazuri rare de ocluzie severă (>70%), modelul are dificultăți în a infera prezența căștii dacă nu vede și o parte din corpul muncitorului (contextul semantic).

3. **Limitări de Infrastructură:**
   - **Dependența de Hardware Generalist:** Soluția actuală rulează pe un Laptop/PC cu GPU dedicat. Nu este încă optimizată (cuantezată la FP16/INT8) pentru a rula pe dispozitive **Edge AI** (ex: Raspberry Pi, NVIDIA Jetson) care ar putea fi montate autonom pe șantier.
   - **Consumul de resurse:** Deși latența este bună (28ms), rularea continuă a unui model Medium solicită intens GPU-ul, generând un consum energetic ridicat, problematic pentru soluțiile pe baterii.

4. **Limitări de Validare:**
   - **Lipsa condițiilor meteo adverse:** Testele au fost efectuate pe imagini clare. Nu s-a validat performanța în condiții de ploaie densă, ceață, ninsoare sau pe timp de noapte (mod IR/Night Vision), scenarii frecvente pe un șantier real.


### 5.3. Direcții viitoare de dezvoltare


**Pe termen scurt (1-3 luni) - Optimizare și Robustete:**

1.  **Rezolvarea limitărilor cauzate de reflexii (Specular Reflection):**
    * Colectarea unui set de date suplimentar (cca. 200 imagini) axat exclusiv pe căști foarte luminoase, filmate în soare puternic sau sub surse de lumină directă.
    * Re-antrenarea modelului folosind augmentări specifice de intensitate: `RandomBrightness`, `CLAHE` (Contrast Limited Adaptive Histogram Equalization) și `Solarize` pentru a învăța rețeaua să nu ignore zonele supraexpuse.

2.  **Optimizare pentru inferență accelerată (TensorRT):**
    * Conversia modelului din formatul standard PyTorch (`.pt`) în **TensorRT** (pentru plăci NVIDIA) sau **OpenVINO** (pentru procesoare Intel).
    * Această conversie poate reduce latența de la 28ms la sub 15ms, permițând rularea algoritmului pe fluxuri video cu framerate ridicat (60 FPS).

3.  **Implementarea buclei de feedback (Active Learning):**
    * Dezvoltarea unei funcționalități în interfața grafică care să permită operatorului să marcheze cu un click detecțiile greșite (ex: când modelul ratează o cască). Aceste imagini vor fi salvate automat pentru re-antrenare periodică.

**Pe termen mediu (3-6 luni) - Industrializare și Hardware:**

1.  **Migrarea pe dispozitive Edge AI (Embedded):**
    * Portarea aplicației de pe laptop/PC pe dispozitive dedicate, eficiente energetic, precum **NVIDIA Jetson Orin Nano** sau **Raspberry Pi 5 + Hailo AI Kit**.
    * Acest pas este esențial pentru instalarea camerelor autonome în zonele izolate ale șantierului, fără a depinde de un server central.

2.  **Extinderea la detecția Echipamentului Complet (Full PPE):**
    * Evoluția de la Single-Class ("casca") la Multi-Class, prin adăugarea detecției pentru: **Veste reflectorizante, Mănuși de protecție și Bocanci**.
    * Corelarea logică a claselor (ex: "Are cască DAR nu are vestă" → Alertă Nivel 2).

3.  **Integrarea IoT și Alerte Fizice:**
    * Conectarea sistemului software cu module de automatizare (ex: protocol MQTT) pentru a declanșa acțiuni fizice: aprinderea unui girofar roșu sau blocarea turnicheților de acces în șantier dacă echipamentul nu este detectat.

```

### 5.4 Lecții Învățate

```markdown
### Lecții învățate pe parcursul proiectului

**Tehnice:**
1. [ex: Preprocesarea datelor a avut impact mai mare decât arhitectura modelului]
2. [ex: Augmentările specifice domeniului > augmentări generice]
3. [ex: Early stopping esențial pentru evitare overfitting]

**Proces:**
1. [ex: Iterațiile frecvente pe date au adus mai multe îmbunătățiri decât pe model]
2. [ex: Testarea end-to-end timpurie a identificat probleme de integrare]
3. [ex: Documentația incrementală a economisit timp la final]

**Colaborare:**
1. [ex: Feedback de la experți domeniu a ghidat selecția features]
2. [ex: Code review a identificat bug-uri în pipeline preprocesare]
```
### 5.4. Lecții Învățate

Dezvoltarea acestui proiect a reprezentat o oportunitate de a transpune cunoștințele teoretice într-o aplicație practică, generând o serie de lecții valoroase atât pe plan tehnic, cât și metodologic.

**Lecții Tehnice:**
1.  **Importanța Rezoluției în Computer Vision:** Am demonstrat experimental că pentru detecția obiectelor mici la distanță, creșterea rezoluției de intrare (de la 640px la 1280px) este mult mai eficientă decât simpla schimbare a arhitecturii modelului.
2.  **Eficiența Transfer Learning:** Utilizarea arhitecturii YOLOv8 pre-antrenate a redus timpul de dezvoltare de la săptămâni la ore, permițând concentrarea efortului pe rafinarea dataset-ului specific ("casca") în loc de proiectarea rețelei de la zero.
3.  **Gestionarea Resurselor Hardware (Cloud vs Local):** Am învățat să optimizez fluxul de lucru prin utilizarea **Google Colab (GPU T4)** pentru etapa intensivă de antrenare și a mediului local (**Visual Studio Code**) pentru dezvoltarea aplicației și inferență, economisind timp și resurse computaționale.

**Lecții de Proces (Metodologie):**
1.  **Abordarea "Data-Centric AI":** Cele mai mari salturi în performanță (de la 72% la 96%) nu au venit din scrierea de cod complex, ci din curățarea datelor, verificarea etichetelor și alegerea corectă a strategiilor de augmentare.
2.  **Iterația Experimentală:** Am înțeles că o rețea neuronală nu se configurează "perfect" din prima încercare. Procesul de monitorizare a curbelor de învățare (Loss vs Epochs) și ajustarea parametrilor (Batch Size, LR) pe baza graficelor a fost esențial pentru evitarea overfitting-ului.
3.  **Modularizarea Proiectului:** Organizarea codului în module distincte (antrenare, validare, interfață grafică) în mediul Python a simplificat depanarea (debugging) și a permis integrarea rapidă a noilor versiuni de model (`best.pt`) fără a rescrie aplicația principală.

**Dezvoltare Personală:**
1.  **Înțelegerea "Black Box-ului":** Proiectul a clarificat concepte abstracte despre funcționarea rețelelor neuronale (cum se propagă eroarea, cum influențează learning rate-ul convergența), transformând "magia" AI-ului într-un proces ingineresc controlabil.

### 5.5 Plan Post-Feedback (ULTIMA ITERAȚIE ÎNAINTE DE EXAMEN)

```markdown
### Plan de acțiune după primirea feedback-ului

**ATENȚIE:** Etapa 6 este ULTIMA VERSIUNE pentru care se oferă feedback!
Implementați toate corecțiile înainte de examen.

După primirea feedback-ului de la evaluatori, voi:

1. **Dacă se solicită îmbunătățiri model:**
   - [ex: Experimente adiționale cu arhitecturi alternative]
   - [ex: Colectare date suplimentare pentru clase problematice]
   - **Actualizare:** `models/`, `results/`, README Etapa 5 și 6

2. **Dacă se solicită îmbunătățiri date/preprocesare:**
   - [ex: Rebalansare clase, augmentări suplimentare]
   - **Actualizare:** `data/`, `src/preprocessing/`, README Etapa 3

3. **Dacă se solicită îmbunătățiri arhitectură/State Machine:**
   - [ex: Modificare fluxuri, adăugare stări]
   - **Actualizare:** `docs/state_machine.*`, `src/app/`, README Etapa 4

4. **Dacă se solicită îmbunătățiri documentație:**
   - [ex: Detaliere secțiuni specifice]
   - [ex: Adăugare diagrame explicative]
   - **Actualizare:** README-urile etapelor vizate

5. **Dacă se solicită îmbunătățiri cod:**
   - [ex: Refactorizare module conform feedback]
   - [ex: Adăugare teste unitare]
   - **Actualizare:** `src/`, `requirements.txt`

**Timeline:** Implementare corecții până la data examen
**Commit final:** `"Versiune finală examen - toate corecțiile implementate"`
**Tag final:** `git tag -a v1.0-final-exam -m "Versiune finală pentru examen"`
```
---

## Structura Repository-ului la Finalul Etapei 6

**Structură COMPLETĂ și FINALĂ:**

```
proiect-rn-[prenume-nume]/
├── README.md                               # Overview general proiect (FINAL)
├── etapa3_analiza_date.md                  # Din Etapa 3
├── etapa4_arhitectura_sia.md               # Din Etapa 4
├── etapa5_antrenare_model.md               # Din Etapa 5
├── etapa6_optimizare_concluzii.md          # ← ACEST FIȘIER (completat)
│
├── docs/
│   ├── state_machine.png                   # Din Etapa 4
│   ├── state_machine_v2.png                # NOU - Actualizat (dacă modificat)
│   ├── loss_curve.png                      # Din Etapa 5
│   ├── confusion_matrix_optimized.png      # NOU - OBLIGATORIU
│   ├── results/                            # NOU - Folder vizualizări
│   │   ├── metrics_evolution.png           # NOU - Evoluție Etapa 4→5→6
│   │   ├── learning_curves_final.png       # NOU - Model optimizat
│   │   └── example_predictions.png         # NOU - Grid exemple
│   ├── optimization/                       # NOU - Grafice optimizare
│   │   ├── accuracy_comparison.png
│   │   └── f1_comparison.png
│   └── screenshots/
│       ├── ui_demo.png                     # Din Etapa 4
│       ├── inference_real.png              # Din Etapa 5
│       └── inference_optimized.png         # NOU - OBLIGATORIU
│
├── data/                                   # Din Etapa 3-5 (NESCHIMBAT)
│   ├── raw/
│   ├── generated/
│   ├── processed/
│   ├── train/
│   ├── validation/
│   └── test/
│
├── src/
│   ├── data_acquisition/                   # Din Etapa 4
│   ├── preprocessing/                      # Din Etapa 3
│   ├── neural_network/
│   │   ├── model.py                        # Din Etapa 4
│   │   ├── train.py                        # Din Etapa 5
│   │   ├── evaluate.py                     # Din Etapa 5
│   │   └── optimize.py                     # NOU - Script optimizare/tuning
│   └── app/
│       └── main.py                         # ACTUALIZAT - încarcă model OPTIMIZAT
│
├── models/
│   ├── untrained_model.h5                  # Din Etapa 4
│   ├── trained_model.h5                    # Din Etapa 5
│   ├── optimized_model.h5                  # NOU - OBLIGATORIU
│
├── results/
│   ├── training_history.csv                # Din Etapa 5
│   ├── test_metrics.json                   # Din Etapa 5
│   ├── optimization_experiments.csv        # NOU - OBLIGATORIU
│   ├── final_metrics.json                  # NOU - Metrici model optimizat
│
├── config/
│   ├── preprocessing_params.pkl            # Din Etapa 3
│   └── optimized_config.yaml               # NOU - Config model final
│
├── requirements.txt                        # Actualizat
└── .gitignore
```

**Diferențe față de Etapa 5:**
- Adăugat `etapa6_optimizare_concluzii.md` (acest fișier)
- Adăugat `docs/confusion_matrix_optimized.png` - OBLIGATORIU
- Adăugat `docs/results/` cu vizualizări finale
- Adăugat `docs/optimization/` cu grafice comparative
- Adăugat `docs/screenshots/inference_optimized.png` - OBLIGATORIU
- Adăugat `models/optimized_model.h5` - OBLIGATORIU
- Adăugat `results/optimization_experiments.csv` - OBLIGATORIU
- Adăugat `results/final_metrics.json` - metrici finale
- Adăugat `src/neural_network/optimize.py` - script optimizare
- Actualizat `src/app/main.py` să încarce model OPTIMIZAT
- (Opțional) `docs/state_machine_v2.png` dacă s-au făcut modificări

---

## Instrucțiuni de Rulare (Etapa 6)

### 1. Rulare experimente de optimizare

```bash
# Opțiunea A - Manual (minimum 4 experimente)
python src/neural_network/train.py --lr 0.001 --batch 32 --epochs 100 --name exp1
python src/neural_network/train.py --lr 0.0001 --batch 32 --epochs 100 --name exp2
python src/neural_network/train.py --lr 0.001 --batch 64 --epochs 100 --name exp3
python src/neural_network/train.py --lr 0.001 --batch 32 --dropout 0.5 --epochs 100 --name exp4
```

### 2. Evaluare și comparare

```bash
python src/neural_network/evaluate.py --model models/optimized_model.h5 --detailed

# Output așteptat:
# Test Accuracy: 0.8123
# Test F1-score (macro): 0.7734
# ✓ Confusion matrix saved to docs/confusion_matrix_optimized.png
# ✓ Metrics saved to results/final_metrics.json
# ✓ Top 5 errors analysis saved to results/error_analysis.json
```

### 3. Actualizare UI cu model optimizat

```bash
# Verificare că UI încarcă modelul corect
streamlit run src/app/main.py

# În consolă trebuie să vedeți:
# Loading model: models/optimized_model.h5
# Model loaded successfully. Accuracy on validation: 0.8123
```

### 4. Generare vizualizări finale

```bash
python src/neural_network/visualize.py --all

# Generează:
# - docs/results/metrics_evolution.png
# - docs/results/learning_curves_final.png
# - docs/optimization/accuracy_comparison.png
# - docs/optimization/f1_comparison.png
```

---

## Checklist Final – Bifați Totul Înainte de Predare

### Prerequisite Etapa 5 (verificare)
- [ ] Model antrenat există în `models/trained_model.h5`
- [ ] Metrici baseline raportate (Accuracy ≥65%, F1 ≥0.60)
- [ ] UI funcțional cu model antrenat
- [ ] State Machine implementat

### Optimizare și Experimentare
- [ ] Minimum 4 experimente documentate în tabel
- [ ] Justificare alegere configurație finală
- [ ] Model optimizat salvat în `models/optimized_model.h5`
- [ ] Metrici finale: **Accuracy ≥70%**, **F1 ≥0.65**
- [ ] `results/optimization_experiments.csv` cu toate experimentele
- [ ] `results/final_metrics.json` cu metrici model optimizat

### Analiză Performanță
- [ ] Confusion matrix generată în `docs/confusion_matrix_optimized.png`
- [ ] Analiză interpretare confusion matrix completată în README
- [ ] Minimum 5 exemple greșite analizate detaliat
- [ ] Implicații industriale documentate (cost FN vs FP)

### Actualizare Aplicație Software
- [ ] Tabel modificări aplicație completat
- [ ] UI încarcă modelul OPTIMIZAT (nu cel din Etapa 5)
- [ ] Screenshot `docs/screenshots/inference_optimized.png`
- [ ] Pipeline end-to-end re-testat și funcțional
- [ ] (Dacă aplicabil) State Machine actualizat și documentat

### Concluzii
- [ ] Secțiune evaluare performanță finală completată
- [ ] Limitări identificate și documentate
- [ ] Lecții învățate (minimum 5)
- [ ] Plan post-feedback scris

### Verificări Tehnice
- [ ] `requirements.txt` actualizat
- [ ] Toate path-urile RELATIVE
- [ ] Cod nou comentat (minimum 15%)
- [ ] `git log` arată commit-uri incrementale
- [ ] Verificare anti-plagiat respectată

### Verificare Actualizare Etape Anterioare (ITERATIVITATE)
- [ ] README Etapa 3 actualizat (dacă s-au modificat date/preprocesare)
- [ ] README Etapa 4 actualizat (dacă s-a modificat arhitectura/State Machine)
- [ ] README Etapa 5 actualizat (dacă s-au modificat parametri antrenare)
- [ ] `docs/state_machine.*` actualizat pentru a reflecta versiunea finală
- [ ] Toate fișierele de configurare sincronizate cu modelul optimizat

### Pre-Predare
- [ ] `etapa6_optimizare_concluzii.md` completat cu TOATE secțiunile
- [ ] Structură repository conformă modelului de mai sus
- [ ] Commit: `"Etapa 6 completă – Accuracy=X.XX, F1=X.XX (optimizat)"`
- [ ] Tag: `git tag -a v0.6-optimized-final -m "Etapa 6 - Model optimizat + Concluzii"`
- [ ] Push: `git push origin main --tags`
- [ ] Repository accesibil (public sau privat cu acces profesori)

---

## Livrabile Obligatorii

Asigurați-vă că următoarele fișiere există și sunt completate:

1. **`etapa6_optimizare_concluzii.md`** (acest fișier) cu:
   - Tabel experimente optimizare (minimum 4)
   - Tabel modificări aplicație software
   - Analiză confusion matrix
   - Analiză 5 exemple greșite
   - Concluzii și lecții învățate

2. **`models/optimized_model.h5`** (sau `.pt`, `.lvmodel`) - model optimizat funcțional

3. **`results/optimization_experiments.csv`** - toate experimentele
```

4. **`results/final_metrics.json`** - metrici finale:

Exemplu:
```json
{
  "model": "optimized_model.h5",
  "test_accuracy": 0.8123,
  "test_f1_macro": 0.7734,
  "test_precision_macro": 0.7891,
  "test_recall_macro": 0.7612,
  "false_negative_rate": 0.05,
  "false_positive_rate": 0.12,
  "inference_latency_ms": 35,
  "improvement_vs_baseline": {
    "accuracy": "+9.2%",
    "f1_score": "+9.3%",
    "latency": "-27%"
  }
}
```

5. **`docs/confusion_matrix_optimized.png`** - confusion matrix model final

6. **`docs/screenshots/inference_optimized.png`** - demonstrație UI cu model optimizat

---

## Predare și Contact

**Predarea se face prin:**
1. Commit pe GitHub: `"Etapa 6 completă – Accuracy=X.XX, F1=X.XX (optimizat)"`
2. Tag: `git tag -a v0.6-optimized-final -m "Etapa 6 - Model optimizat + Concluzii"`
3. Push: `git push origin main --tags`

---

**REMINDER:** Aceasta a fost ultima versiune pentru feedback. Următoarea predare este **VERSIUNEA FINALĂ PENTRU EXAMEN**!






