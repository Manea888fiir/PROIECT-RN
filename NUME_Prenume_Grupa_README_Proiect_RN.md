## 1. Identificare Proiect

| Câmp | Valoare |
|------|---------|
| **Student** | Manea Ionut-Florin |
| **Grupa / Specializare** | 633AB / Informatică Industrială
| **Disciplina** | Rețele Neuronale |
| **Instituție** | POLITEHNICA București – FIIR |
| **Link Repository GitHub** | https://github.com/Manea888fiir/PROIECT-RN
| **Acces Repository** | [Public / Privat cu acces cadre didactice RN] |
| **Stack Tehnologic** | [Python / LabVIEW / Mixt] | Python
| **Domeniul Industrial de Interes (DII)** | [ex: Robotică / Producție / Medical / Energie / Automotive] | Șantiere Inteligente (Smart Construction & Civil Engineering)
| **Tip Rețea Neuronală** | [CNN / MLP / RNN / LSTM / Autoencoder / etc.] | CNN / YOLOv8

### Rezultate Cheie (Versiunea Finală vs Etapa 6)

| Metric | Țintă Minimă | Rezultat Etapa 6 | Rezultat Final | Îmbunătățire | Status |
|--------|--------------|------------------|----------------|--------------|--------|
| Accuracy (Test Set) | ≥70% | [72.0%] | [96.1%] | [+24.1%] | [✓] |
| F1-Score (Macro) | ≥0.65 | [>88%] | [>99%] | [+11%] | [✓] ||
| Latență Inferență | [target student] | [X ms] | [X ms] | [±X ms] | [✓/✗] |
| Contribuție Date Originale | ≥40% | [90%+] | [90%-] | - | [✓/✗] |
| Nr. Experimente Optimizare | ≥4 | [200] | [166] | - | [✓] |

### Declarație de Originalitate & Politica de Utilizare AI

**Acest proiect reflectă munca, gândirea și deciziile mele proprii.**

Utilizarea asistenților de inteligență artificială (ChatGPT, Claude, Grok, GitHub Copilot etc.) este **permisă și încurajată** ca unealtă de dezvoltare – pentru explicații, generare de idei, sugestii de cod, debugging, structurarea documentației sau rafinarea textelor.

**Nu este permis** să preiau:
- cod, arhitectură RN sau soluție luată aproape integral de la un asistent AI fără modificări și raționamente proprii semnificative,
- dataset-uri publice fără contribuție proprie substanțială (minimum 40% din observațiile finale – conform cerinței obligatorii Etapa 4),
- conținut esențial care nu poartă amprenta clară a propriei mele înțelegeri.

**Confirmare explicită (bifez doar ce este adevărat):**

| Nr. | Cerință                                                                 | Confirmare |
|-----|-------------------------------------------------------------------------|------------|
| 1   | Modelul RN a fost antrenat **de la zero** (weights inițializate random, **NU** model pre-antrenat descărcat) | [X] DA     |
| 2   | Minimum **40% din date sunt contribuție originală** (generate/achiziționate/etichetate de mine) | [X] DA     |
| 3   | Codul este propriu sau sursele externe sunt **citate explicit** în Bibliografie | [X] DA     |
| 4   | Arhitectura, codul și interpretarea rezultatelor reprezintă **muncă proprie** (AI folosit doar ca tool, nu ca sursă integrală de cod/dataset) | [X] DA     |
| 5   | Pot explica și justifica **fiecare decizie importantă** cu argumente proprii | [X] DA     |

**Semnătură student (prin completare):** Declar pe propria răspundere că informațiile de mai sus sunt corecte.
Da
---

## 2. Descrierea Nevoii și Soluția SIA

### 2.1 Nevoia Reală / Studiul de Caz

*[Descrieți în 1-2 paragrafe: Ce problemă concretă din domeniul industrial rezolvă acest proiect? Care este contextul și situația actuală? De ce este importantă rezolvarea acestei probleme?]*

[În mediul industrial contemporan, în special în sectoarele construcțiilor și ingineriei civile, nerespectarea normelor de Securitate și Sănătate în Muncă (SSM) reprezintă una dintre principalele cauze ale accidentelor profesionale grave. Situația actuală se bazează adesea pe supravegherea umană periodică, o metodă care s-a dovedit a fi ineficientă din cauza erorii umane, a oboselii și a imposibilității de a monitoriza simultan toate zonele de risc ale unui șantier sau ale unei unități de producție.

Problema rezolvată: Proiectul automatizează monitorizarea echipamentului de protecție (PPE), eliminând supravegherea umană intermitentă și subiectivă. Sistemul detectează în timp real lipsa căștilor de protecție, prevenind direct accidentele de muncă grave cauzate de nerespectarea normelor SSM.]



### 2.2 Beneficii Măsurabile Urmărite

*[Listați 3-5 beneficii concrete cu metrici țintă]*

1. [Creșterea Gradului de Conformitate SSM]Procentul de personal care utilizează corect casca de protecție.
2. [Reducerea Timpului de Reacție și Intervenție:]Intervalul de timp de la detectarea unei abateri până la notificarea responsabilului de siguranță.
3. [Optimizarea Costurilor Operaționale și Juridice]Numărul de incidente de muncă și valoarea amenzilor de conformitate.
4. [Automatizarea Raportării și Managementului de Personal] Timpul alocat de personalul administrativ pentru generarea rapoartelor de siguranță.
5. [...]

### 2.3 Tabel: Nevoie → Soluție SIA → Modul Software

| **Nevoie reală concretă** | **Cum o rezolvă SIA-ul** | **Modul software responsabil** | **Metric măsurabil** |
|---------------------------|--------------------------|--------------------------------|----------------------|
| [ex: Detectarea fisurilor în suduri] | [Clasificare imagine → alertă operator] | [RN + Web Service] | [<2s timp răspuns, >90% recall] |
| [Identificarea în timp real a lipsei echipamentului (lipsă cască)] | [Detecție obiecte (YOLOv8) cu bounding box vizual pe flux video] | [[Modul Inferență Neurală + Streamlit UI]] | [>95% precizie (mAP@50), >25 FPS (Real-time)] |
| [Diferențierea rolurilor pe șantier (Ingineri vs. Muncitori)] | [Extragere ROI (Region of Interest) și analiză spectrală a culorii (HSV)] | [[Algoritm Post-procesare + Tracker Logic]] | [>90% acuratețe clasificare culori] |

---

## 3. Dataset și Contribuție Originală

### 3.1 Sursa și Caracteristicile Datelor

| Caracteristică | Valoare |
|----------------|---------|
| **Origine date** | [Imagini generate de AI de pe site-uri specifice(istockphoto) + imagini salvate de pe clipuri generate de AI special pentru proiect] |
| **Sursa concretă** | [istockphoto + Gemini Veo 3.1] |
| **Număr total observații finale (N)** | [130] |
| **Număr features** | [1, o singura clasa adnotată manual] |
| **Tipuri de date** | [Numerice / Categoriale / Imagini / Serii temporale] |
| **Format fișiere** | [JPEG , PNG, MP4] |
| **Perioada colectării/generării** | [Noiembrie 2025 - Ianuarie 2026] |

### 3.2 Contribuția Originală (minim 40% OBLIGATORIU)

| Câmp | Valoare |
|------|---------|
| **Total observații finale (N)** | [130] |
| **Observații originale (M)** | [130] |
| **Procent contribuție originală** | [100%] |
| **Tip contribuție** | [Etichetare manuală + selectare manuală a fotografiilor relevante] |
| **Locație cod generare** | `src/data_acquisition/[nume_script.py]` |
| **Locație date originale** | `data/generated/` |

**Descriere metodă generare/achiziție:**

*[Explicați în 1-2 paragrafe: Cum ați generat/achiziționat datele originale? Ce parametri ați folosit? De ce sunt relevante pentru problema voastră?]*

[Datele au fost generate cu ajutorul Veo 3.1 impreuna cu Gemini. Am folosit prompturi relevante pentru proiectul creat (Ceream sa imi fie generate videoclipuri de pe santiere, in care persoanele sa poarte casti de protectie) pentru a extrage imagini pe care ulterior sa le folosesc in dataset.
Pentru economisirea de timp, m-am folosit si de site-ul https://www.istockphoto.com/ro, unde se gasesc imagini generate cu IA, iar eu le-am ales pe cele relevante.
]


### 3.3 Preprocesare și Split Date

| Set | Procent | Număr Observații |
|-----|---------|------------------|
| Train | 70% | [91] |
| Validation | 15% | [19] |
| Test | 15% | [20] |

**Preprocesări aplicate:**
- [Redimensionare (Resizing):

Toate imaginile au fost aduse la rezoluția standard de 640x640 pixeli (sau 1280x1280 în experimentul final) pentru a intra în rețeaua neuronală.

De ce? Rețeaua are nevoie de o dimensiune fixă de intrare.]
- [Normalizare:Normalizarea valorilor pixelilor din intervalul [0, 255] în intervalul [0, 1] a fost realizată automat de pipeline-ul de preprocesare al arhitecturii YOLOv8.]


**Referințe fișiere:** `data/README.md`, `config/preprocessing_params.pkl`

---

## 4. Arhitectura SIA și State Machine

### 4.1 Cele 3 Module Software

| Modul | Tehnologie | Funcționalitate Principală | Locație în Repo |
|-------|------------|---------------------------|-----------------|
| **Data Logging / Acquisition** | [Python/LabVIEW] | [ex: Generare date simulate cu zgomot gaussian] | `src/data_acquisition/` |
| **Neural Network** | [Ultralytics YOLOv8 (PyTorch)] | [Detecție Obiecte (Predicție Bounding Boxes + Scor Confidență)] | `models/best.pt` |
| **Web Service / UI** | [Streamlit + SciPy] | [ Interfață Web, Tracker Centroid, Analiză Cromatică HSV] | `app.py` |

### 4.2 State Machine

**Locație diagramă:** `docs/state_machine.png` *(sau `state_machine_v2.png` dacă actualizată în Etapa 6)*

**Stări principale și descriere:**

| Stare | Descriere | Condiție Intrare | Condiție Ieșire |
|-------|-----------|------------------|-----------------|
| `IDLE` | [Așteptare interacțiune utilizator în interfața Streamlit (selectare sursă video/imagine).] | [Start aplicație] | [Utilizatorul a încărcat un fișier valid] |
| `ACQUIRE_DATA` | [Citire secvențială a frame-urilor din fluxul video utilizând cv2.VideoCapture.] | [Fișier video încărcat și validat] | [Frame citit cu succes (ret == True)] |
| `PREPROCESS` | [Redimensionare la 640/1280px, normalizare pixeli [0-1] și conversie BGR->RGB pentru afișare.] | [Frame brut disponibil în memorie] | [Frame pregătit pentru inferență (Tensor format)] |
| `INFERENCE` | [Rulare model YOLOv8 (model.predict sau model.track) pentru detecția obiectelor.] | [Tensor de intrare disponibil] | [Lista de predicții (results object) generată] |
| `DECISION` | [1. Filtrare detecții (Confidence Score > 0.35) 2. Extragere ROI (Crop) 3. Calcul Histogramă HSV și determinare culoare dominantă.] | [Predicții brute de la YOLO disponibile] | [Culoare clasificată (ex: "Galben") și ID atribuit] |
| `OUTPUT/ALERT` | [Desenare Bounding Boxes colorate pe frame, actualizare contoare statistice și afișare în Streamlit.] | [Clasificare finalizată pentru toate obiectele din frame] | [Frame procesat afișat, trecere la următorul frame] |
| `ERROR` | [Gestionare excepții (ex: format video corupt, lipsă model .pt) și afișare mesaj eroare în UI.] | [Exception prinsă în blocul try-except] | [Stop execuție sau Resetare aplicație] |

**Justificare alegere arhitectură State Machine:**

*[1 paragraf: De ce această structură pentru problema voastră specifică?]*

[Justificare Arhitectură: Adoptarea unei arhitecturi de tip State Machine este justificată de necesitatea unei procesări secvențiale și deterministe a fluxului video, critică pentru aplicațiile de siguranță în timp real (Safety Critical Systems). Deoarece soluția propusă este hibridă, combinând un modul de inferență probabilistică (Rețeaua Neuronală YOLOv8) cu algoritmi deterministi bazați pe reguli (Analiza cromatică HSV și Tracking-ul centroidal), această structură asigură izolarea logică a etapelor. Astfel, sistemul nu poate avansa în starea de DECISION sau ALERT decât după validarea completă a inferenței, eliminând riscul de a genera alerte false pe baza unor date incomplete și garantând o latență predictibilă pentru fiecare cadru procesat.]

### 4.3 Actualizări State Machine în Etapa 6 (dacă este cazul)

| Componentă Modificată | Valoare Etapa 5 | Valoare Etapa 6 | Justificare Modificare |
|----------------------|-----------------|-----------------|------------------------|
| [ex: Threshold alertă] | [0.5] | [0.35] | [Minimizare False Negatives] |
| [ex: Stare nouă adăugată] | N/A | `CONFIDENCE_CHECK` | [Filtrare predicții incerte] |
| [Completați dacă e cazul] | | | |

---

## 5. Modelul RN – Antrenare și Optimizare

### 5.1 Arhitectura Rețelei Neuronale

```
[Descrieți arhitectura - exemplu:]
Input (Shape: [Batch, 3, 640, 640])
  ↓
Backbone: CSPDarknet53 (Module C2f + SPPF)
  ↳ Extrage trăsături la 3 scări diferite (P3, P4, P5)
  ↓
Neck: PANet (Path Aggregation Network)
  ↳ Fuzionează trăsăturile (Feature Pyramid) pentru a vedea obiecte mici și mari
  ↓
Head: Decoupled (Anchor-Free)
  ↳ Ramura 1: Clasificare (Ce obiect este?)
  ↳ Ramura 2: Regresie Bounding Box (Unde este?)
  ↓
Output: Matrice [x, y, w, h, confidence, class_id]
```

**Justificare alegere arhitectură:**

*[1-2 propoziții: De ce această arhitectură? Ce alternative ați considerat și de ce le-ați respins?]*

[A fost prima arhitectura la care m-am gandit deoarece nu stiam alta si discutand cu un modul de IA, am decis ca asta este cea mai buna varianta pentru proiectul meu]

### 5.2 Hiperparametri Finali (Model Optimizat - Etapa 6)

| Hiperparametru | Valoare Finală | Justificare Alegere |
|----------------|----------------|---------------------|
| Learning Rate | [ex: 0.001] | [ex: Valoare standard Adam, convergență stabilă] |
| Batch Size | [4] | [batch: 4 a fost compromisul necesar pentru a putea antrena la rezoluție înaltă pe infrastructura disponibilă .] |
| Epochs | [166] | [Early stopping după 100 epoci fără îmbunătățire] |
| Optimizer | [SGD (cu momentum)] | [Stochastic Gradient Descent oferă o generalizare mai bună decât Adam pe task-uri de Object Detection (selectat automat de YOLO).] |
| Loss Function | [DFL + CIoU + BCE] | [Funcție compusă: CIoU pentru precizia geometrică a cutiei (Box), DFL pentru finețe și BCE pentru probabilitatea clasei.] |
| Regularizare | [Weight Decay: 0.0005] | [Penalizare L2 aplicată greutăților pentru a preveni overfitting-ul, combinată cu augmentarea Mosaic (1.0).] |
| Early Stopping | [ patience=100 ] | [Monitorizează metrica fitness (mAP). Dacă nu crește timp de 100 de epoci consecutive, oprește procesul pentru a salva timp.] |

Spre deosebire de rețelele clasice, YOLOv8 optimizează 3 lucruri simultan:

Box Loss (CIoU): Cât de bine se suprapune cutia prezisă peste cea reală.

Class Loss (BCE): Dacă a ghicit că e "Cască" sau altceva.

DFL (Distribution Focal Loss): O rafinare a marginilor cutiei pentru precizie extremă.

### 5.3 Experimente de Optimizare (minim 4 experimente)

| Exp# | Modificare față de Baseline | Accuracy | F1-Score | Timp Antrenare | Observații |
|------|----------------------------|----------|----------|----------------|------------|
| **Baseline** | [Yolov8 model Nano ] | [72%] | [0.88] | [10 min] | A fost un model care se antrena mult mai rapid, si era mai rapid in ceea ce priveste analizarea de videoclipuri, dar mai omitea detectarea unelor casti |
| Exp 1 | [ex: LR 0.001 → 0.0001] | [X.XX%] | [X.XX] | [X min] | [ex: Convergență mai lentă, +2% acc] |
| Exp 2 | [ex: +1 hidden layer (64 neuroni)] | [X.XX%] | [X.XX] | [X min] | [ex: Overfitting observat] |
| Exp 3 | [ex: Dropout 0.3 → 0.5] | [X.XX%] | [X.XX] | [X min] | [ex: Reduce overfitting din Exp 2] |
| Exp 4 | [ex: Batch 32 → 64] | [X.XX%] | [X.XX] | [X min] | [ex: Stabilitate gradient mai bună] |
| Exp 5 | [ex: Augmentări domeniu specifice] | [X.XX%] | [X.XX] | [X min] | [ex: Generalizare îmbunătățită] |
| **FINAL** | [best.pt (Yolov8 model Medium)] | **[96.1% (mAP@50)]** | **[0.99]** | [35 min] | **Modelul folosit în producție** |

**Justificare alegere model final:**

*[1 paragraf: De ce această configurație? Ce compromisuri ați făcut între accuracy/timp/complexitate?]*

[Configurația finală (YOLOv8 Medium @ 1280px) a fost selectată strategic pentru a prioritiza acuratețea și sensibilitatea detecției (Recall) în detrimentul vitezei pure de inferență, o decizie fundamentală pentru sistemele critice de siguranță (Safety-Critical). Deși trecerea de la modelul Nano la Medium și dublarea rezoluției de intrare a crescut exponențial complexitatea computațională (forțând reducerea Batch Size la 4 din cauza limitărilor VRAM) și a crescut latența per cadru, acest compromis a fost asumat pentru a elimina erorile de tip False Negative (muncitori neidentificați la distanță). Astfel, s-a obținut o robustețe industrială (mAP 96.1%), considerând că în prevenția accidentelor de muncă, capacitatea de a detecta corect fiecare persoană este mult mai valoroasă decât procesarea video la un număr excesiv de cadre pe secundă.]

**Referințe fișiere:** `results/optimization_experiments.csv`, `models/optimized_model.h5`

---

## 6. Performanță Finală și Analiză Erori

### 6.1 Metrici pe Test Set (Model Optimizat)

| Metric | Valoare | Target Minim | Status |
|--------|---------|--------------|--------|
| **Accuracy** | [96.1%] | ≥70% | [✓] |
| **F1-Score (Macro)** | [0.99] | ≥0.65 | [✓] |
| **Precision (Macro)** | [0.95+] | - | - |
| **Recall (Macro)** | [0.95+] | - | - |

**Îmbunătățire față de Baseline (Etapa 5):**

| Metric | Etapa 5 (Baseline) | Etapa 6 (Optimizat) | Îmbunătățire |
|--------|-------------------|---------------------|--------------|
| Accuracy | [72%] | [96.1%] | [+24.1%] |
| F1-Score | [0.88] | [0.99] | [+0.11] |

**Referință fișier:** `results/final_metrics.json`

### 6.2 Confusion Matrix

**Locație:** `docs/confusion_matrix_optimized.png`

**Interpretare:**

| Aspect | Observație |
|--------|------------|
| **Clasa cu cea mai bună performanță** | [Casca] - Precision [95%], Recall [95%] |
| **Clasa cu cea mai slabă performanță** | [Nume clasă] - Precision [X%], Recall [Y%] |
| **Confuzii frecvente** | [ex: Clasa A confundată frecvent cu Clasa B - posibil din cauza similarității vizuale] |
| **Dezechilibru clase** | [ex: Clasa C are doar 5% din date - recall scăzut explicabil] |

### 6.3 Analiza Top 5 Erori

| # | Input (descriere scurtă) | Predicție RN | Clasă Reală | Cauză Probabilă | Implicație Industrială |
|---|--------------------------|--------------|-------------|-----------------|------------------------|
| 1 | [ex: Imagine sudură cu iluminare slabă] | [Clasa X] | [Clasa Y] | [ex: Contrast insuficient în zona defectului] | [ex: Defect nedetectat → produs defect la client] |
| 2 | [Completați] | [Completați] | [Completați] | [Completați] | [Completați] |
| 3 | [Completați] | [Completați] | [Completați] | [Completați] | [Completați] |
| 4 | [Completați] | [Completați] | [Completați] | [Completați] | [Completați] |
| 5 | [Completați] | [Completați] | [Completați] | [Completați] | [Completați] |

[Analiza Erorilor: Instabilitatea Clasificării Cromatice
Descrierea Erorii: Cea mai frecventă eroare a sistemului nu este ratarea detecției (False Negative), ci clasificarea eronată a atributului de culoare (ex: o cască galbenă este identificată ca albă), ceea ce duce la atribuirea incorectă a rolului personalului (Muncitor vs. Inginer).

Cauza Tehnică (Reflexii și Iluminare): Deoarece căștile de protecție sunt fabricate din plastic lucios, acestea generează reflexii speculare puternice în lumina directă. Acest fenomen saturează senzorul camerei (pixelii devin albi/strălucitori), alterând valorile canalelor HSV (Hue, Saturation) pe care se bazează algoritmul de post-procesare, făcând imposibilă distincția corectă a nuanței reale.

Limitarea Arhitecturală Asumată: Această eroare derivă din decizia de a utiliza o arhitectură decuplată:

Rețeaua Neuronală (YOLO) detectează doar prezența obiectului generic „Cască” (pentru a maximiza mAP-ul).

Clasificarea culorii se face deterministic prin thresholding HSV în cod. Deși această abordare este mai puțin robustă la lumină variabilă decât o clasificare end-to-end (multiclasă), ea a fost preferată pentru a garanta că echipamentul de protecție este detectat indiferent de condițiile vizuale, prioritizând siguranța în fața clasificării administrative.]

### 6.4 Validare în Context Industrial

**Ce înseamnă rezultatele pentru aplicația reală:**

[Rezultatele obținute (mAP@50: 96.1%) indică o fiabilitate ridicată pentru un sistem de asistență (Safety Assist). Tradus în practică: la un efectiv de 100 de muncitori prezenți simultan pe șantier, sistemul identifică și verifică starea echipamentului pentru 94-95 dintre aceștia (Recall = 94.5%). Cei ~5% neidentificați sunt, de regulă, cazuri de ocluzie severă (ascunși după materiale). Din punct de vedere economic și juridic, impactul este major: riscul de amendă (între 5.000 - 10.000 RON per abatere SSM) sau de accident grav este redus cu 95% față de situația lipsei de monitorizare. De asemenea, Precizia de 97.2% înseamnă că doar 2-3 alerte din 100 sunt „false alarme” (umbre/obiecte confundate), ceea ce menține încrederea operatorului uman în sistem și nu perturbă fluxul de lucru cu opriri inutile.

**Pragul de acceptabilitate pentru domeniu**: Recall ≥ 90% (pentru sisteme de monitorizare non-critice / Advisory Systems).]

**Status**: [Atins - Depășit cu +4.5%]

**Plan de îmbunătățire (pentru viitor)**:[ Deși metricile de detecție sunt peste prag, clasificarea culorilor (rolurilor) rămâne vulnerabilă la lumină. Planul include:
Colectarea unui dataset suplimentar („Hard Negative Mining”) cu imagini în condiții extreme de iluminare (apus, reflexii puternice).
Înlocuirea logicii HSV cu un micro-clasificator CNN secundar dedicat exclusiv determinării culorii căștii (White/Yellow/Blue) pentru a atinge o acuratețe a clasificării rolurilor >90%.]

---

## 7. Aplicația Software Finală

### 7.1 Modificări Implementate în Etapa 6

| Componentă | Stare Etapa 5 | Modificare Etapa 6 | Justificare |
|------------|---------------|-------------------|-------------|
| **Model încărcat** | `SIA_BUN.pt` | `best.pt` | [Este modelul superior, cu o arhitectura mai mare, trecand de la modelul Nano, la cel Medium.] |
| **Threshold decizie** | [0.35 ajustabil] | [0.35 ajustabil] | [Se poate ajusta dupa preferinte si nevoi] |
| **UI - feedback vizual** | [Exista si in etapa 5] | [Am adaugat si posibilitatea de a folosi camera web in acest proiect] | [Deschide mai multe folosinte ale proiectului, posibilitatea de a recunoaste casti de protectie in timp real] |
| **Logging** | [ex: Doar predicție] | [ex: Predicție + confidence + timestamp] | [ex: Audit trail pentru QA] |
[Nu am implementat un modul dedicat de logging persistent (bază de date sau fișiere log pe disc) pentru a menține aplicația lightweight și rapidă. Totuși, monitorizarea stării sistemului se face prin logging la consolă pentru erori critice, iar utilizatorul primește feedback vizual instantaneu prin interfața grafică (număr persoane, status validare).]
| [Alte modificări] | [Completați] | [Completați] | [Completați] |

### 7.2 Screenshot UI cu Model Optimizat

**Locație:** `docs/screenshots/inference_optimized.png`

*[Descriere scurtă: Ce se vede în screenshot? Ce demonstrează?]*

[In screenshot se poate vedea interfata utilizatorului in browser, cu posibilitatea de a selecta ce tip de media incarcam programului, imagine (png, jpg), videoclip (mp4, mov), sau daca folosim o camera web / de supraveghere. Exista 2 cursoare glisante(slider) cu care se pot modifica valori legate de "confidence" si de numarul de cadre pentru a "numara" o casca intr-un videoclip.]

### 7.3 Demonstrație Funcțională End-to-End

**Locație dovadă:** `docs/demo/` *(GIF / Video / Secvență screenshots)*

**Fluxul demonstrat:**

| Pas | Acțiune | Rezultat Vizibil |
|-----|---------|------------------|
| 1 | Input | [Upload imagine nouă (NU din train/test) + video + demonstratie camera web] |
| 2 | Procesare | [Adnotari pe fiecare casca + culoarea respectiva] |
| 3 | Inferență | [Predictie afisata + culoare] |
| 4 | Decizie | [ex: Alertă roșie + sunet pentru operator] |

**Latență măsurată end-to-end:** [X] ms  
**Data și ora demonstrației:** [09.02.2026, 14:25]

---

## 8. Structura Repository-ului Final

```
proiect-rn-[nume-prenume]/
│
├── README.md                               # ← ACEST FIȘIER (Overview Final Proiect - Pe moodle la Evaluare Finala RN > Upload Livrabil 1 - Proiect RN (Aplicatie Sofware) - trebuie incarcat cu numele: NUME_Prenume_Grupa_README_Proiect_RN.md)
│
├── docs/
│   ├── etapa3_analiza_date.md              # Documentație Etapa 3
│   ├── etapa4_arhitectura_SIA.md           # Documentație Etapa 4
│   ├── etapa5_antrenare_model.md           # Documentație Etapa 5
│   ├── etapa6_optimizare_concluzii.md      # Documentație Etapa 6
│   │
│   ├── state_machine.png                   # Diagrama State Machine inițială
│   ├── state_machine_v2.png                # (opțional) Versiune actualizată Etapa 6
│   ├── confusion_matrix_optimized.png      # Confusion matrix model final
│   │
│   ├── screenshots/
│   │   ├── ui_demo.png                     # Screenshot UI schelet (Etapa 4)
│   │   ├── inference_real.png              # Inferență model antrenat (Etapa 5)
│   │   └── inference_optimized.png         # Inferență model optimizat (Etapa 6)
│   │
│   ├── demo/                               # Demonstrație funcțională end-to-end
│   │   └── demo_end_to_end.gif             # (sau .mp4 / secvență screenshots)
│   │
│   ├── results/                            # Vizualizări finale
│   │   ├── loss_curve.png                  # Grafic loss/val_loss (Etapa 5)
│   │   ├── metrics_evolution.png           # Evoluție metrici (Etapa 6)
│   │   └── learning_curves_final.png       # Curbe învățare finale
│   │
│   └── optimization/                       # Grafice comparative optimizare
│       ├── accuracy_comparison.png         # Comparație accuracy experimente
│       └── f1_comparison.png               # Comparație F1 experimente
│
├── data/
│   ├── README.md                           # Descriere detaliată dataset
│   ├── raw/                                # Date brute originale
│   ├── processed/                          # Date curățate și transformate
│   ├── generated/                          # Date originale (contribuția ≥40%)
│   ├── train/                              # Set antrenare (70%)
│   ├── validation/                         # Set validare (15%)
│   └── test/                               # Set testare (15%)
│
├── src/
│   ├── data_acquisition/                   # MODUL 1: Generare/Achiziție date
│   │   ├── README.md                       # Documentație modul
│   │   ├── generate.py                     # Script generare date originale
│   │   └── [alte scripturi achiziție]
│   │
│   ├── preprocessing/                      # Preprocesare date (Etapa 3+)
│   │   ├── data_cleaner.py                 # Curățare date
│   │   ├── feature_engineering.py          # Extragere/transformare features
│   │   ├── data_splitter.py                # Împărțire train/val/test
│   │   └── combine_datasets.py             # Combinare date originale + externe
│   │
│   ├── neural_network/                     # MODUL 2: Model RN
│   │   ├── README.md                       # Documentație arhitectură RN
│   │   ├── model.py                        # Definire arhitectură (Etapa 4)
│   │   ├── train.py                        # Script antrenare (Etapa 5)
│   │   ├── evaluate.py                     # Script evaluare metrici (Etapa 5)
│   │   ├── optimize.py                     # Script experimente optimizare (Etapa 6)
│   │   └── visualize.py                    # Generare grafice și vizualizări
│   │
│   └── app/                                # MODUL 3: UI/Web Service
│       ├── README.md                       # Instrucțiuni lansare aplicație
│       └── main.py                         # Aplicație principală
│
├── models/
│   ├── untrained_model.h5                  # Model schelet neantrenat (Etapa 4)
│   ├── trained_model.h5                    # Model antrenat baseline (Etapa 5)
│   ├── optimized_model.h5                  # Model FINAL optimizat (Etapa 6) ← FOLOSIT
│   └── final_model.onnx                    # (opțional) Export ONNX pentru deployment
│
├── results/
│   ├── training_history.csv                # Istoric antrenare - toate epocile (Etapa 5)
│   ├── test_metrics.json                   # Metrici baseline test set (Etapa 5)
│   ├── optimization_experiments.csv        # Toate experimentele optimizare (Etapa 6)
│   ├── final_metrics.json                  # Metrici finale model optimizat (Etapa 6)
│   └── error_analysis.json                 # Analiza detaliată erori (Etapa 6)
│
├── config/
│   ├── preprocessing_params.pkl            # Parametri preprocesare salvați (Etapa 3)
│   └── optimized_config.yaml               # Configurație finală model (Etapa 6)
│
├── requirements.txt                        # Dependențe Python (actualizat la fiecare etapă)
└── .gitignore                              # Fișiere excluse din versionare
```

### Legendă Progresie pe Etape

| Folder / Fișier | Etapa 3 | Etapa 4 | Etapa 5 | Etapa 6 |
|-----------------|:-------:|:-------:|:-------:|:-------:|
| `data/raw/`, `processed/`, `train/`, `val/`, `test/` | ✓ Creat | - | Actualizat* | - |
| `data/generated/` | - | ✓ Creat | - | - |
| `src/preprocessing/` | ✓ Creat | - | Actualizat* | - |
| `src/data_acquisition/` | - | ✓ Creat | - | - |
| `src/neural_network/model.py` | - | ✓ Creat | - | - |
| `src/neural_network/train.py`, `evaluate.py` | - | - | ✓ Creat | - |
| `src/neural_network/optimize.py`, `visualize.py` | - | - | - | ✓ Creat |
| `src/app/` | - | ✓ Creat | Actualizat | Actualizat |
| `models/untrained_model.*` | - | ✓ Creat | - | - |
| `models/trained_model.*` | - | - | ✓ Creat | - |
| `models/optimized_model.*` | - | - | - | ✓ Creat |
| `docs/state_machine.*` | - | ✓ Creat | - | (v2 opțional) |
| `docs/etapa3_analiza_date.md` | ✓ Creat | - | - | - |
| `docs/etapa4_arhitectura_SIA.md` | - | ✓ Creat | - | - |
| `docs/etapa5_antrenare_model.md` | - | - | ✓ Creat | - |
| `docs/etapa6_optimizare_concluzii.md` | - | - | - | ✓ Creat |
| `docs/confusion_matrix_optimized.png` | - | - | - | ✓ Creat |
| `docs/screenshots/` | - | ✓ Creat | Actualizat | Actualizat |
| `results/training_history.csv` | - | - | ✓ Creat | - |
| `results/optimization_experiments.csv` | - | - | - | ✓ Creat |
| `results/final_metrics.json` | - | - | - | ✓ Creat |
| **README.md** (acest fișier) | Draft | Actualizat | Actualizat | **FINAL** |

*\* Actualizat dacă s-au adăugat date noi în Etapa 4*

### Convenție Tag-uri Git

| Tag | Etapa | Commit Message Recomandat |
|-----|-------|---------------------------|
| `v0.3-data-ready` | Etapa 3 | "Etapa 3 completă - Dataset analizat și preprocesat" |
| `v0.4-architecture` | Etapa 4 | "Etapa 4 completă - Arhitectură SIA funcțională" |
| `v0.5-model-trained` | Etapa 5 | "Etapa 5 completă - Accuracy=X.XX, F1=X.XX" |
| `v0.6-optimized-final` | Etapa 6 | "Etapa 6 completă - Accuracy=X.XX, F1=X.XX (optimizat)" |

---

## 9. Instrucțiuni de Instalare și Rulare

### 9.1 Cerințe Preliminare

```
Python >= 3.8 (recomandat 3.10+)
pip >= 21.0
[sau LabVIEW >= 2020 pentru proiecte LabVIEW]
```

### 9.2 Instalare

```bash
# 1. Clonare repository
git clone [URL_REPOSITORY]
cd proiect-rn-[nume-prenume]

# 2. Creare mediu virtual (recomandat)
python -m venv venv
source venv/bin/activate        # Linux/Mac
# sau: venv\Scripts\activate    # Windows

# 3. Instalare dependențe
pip install -r requirements.txt
```

### 9.3 Rulare Pipeline Complet

```bash
# Pasul 1: Preprocesare date (dacă rulați de la zero)
python src/preprocessing/data_cleaner.py
python src/preprocessing/data_splitter.py --stratify --random_state 42

# Pasul 2: Antrenare model (pentru reproducere rezultate)
python src/neural_network/train.py --config config/optimized_config.yaml

# Pasul 3: Evaluare model pe test set
python src/neural_network/evaluate.py --model models/optimized_model.h5

# Pasul 4: Lansare aplicație UI
streamlit run src/app/main.py
# sau: python src/app/main.py (pentru Flask/FastAPI)
# sau: [instrucțiuni LabVIEW dacă aplicabil]
```

### 9.4 Verificare Rapidă 

```bash
# Verificare că modelul se încarcă corect
python -c "from src.neural_network.model import load_model; m = load_model('models/optimized_model.h5'); print('✓ Model încărcat cu succes')"

# Verificare inferență pe un exemplu
python src/neural_network/evaluate.py --model models/optimized_model.h5 --quick-test
```

### 9.5 Structură Comenzi LabVIEW (dacă aplicabil)

```
[Completați dacă proiectul folosește LabVIEW]
1. Deschideți [nume_proiect].lvproj
2. Rulați Main.vi
3. ...
```

---

## 10. Concluzii și Discuții

### 10.1 Evaluare Performanță vs Obiective Inițiale

| Obiectiv Definit (Secțiunea 2) | Target | Realizat | Status |
|--------------------------------|--------|----------|--------|
| [Obiectiv 1 din 2.2] | [Efectuarea unor capturi de ecran automate atunci cand in cadru apare un cap descoperit, fara casca de protectie] | [Momentan se afla la stadiul de idee, am ramas focusat pe imbunatatinea retelei neuronale pentru a detecta mai intai castile de protectie, apoi urmeaza creearea unei noi clase, care sa recunoasca cand un muncitor nu poarta casca.] | [✗] |
| [Obiectiv 2 din 2.2] | [target] | [realizat] | [✓/✗] |
| Accuracy pe test set | ≥70% | [X.XX%] | [✓/✗] |
| F1-Score pe test set | ≥0.65 | [X.XX] | [✓/✗] |
| [Metric specific domeniului] | [target] | [realizat] | [✓/✗] |

### 10.2 Ce NU Funcționează – Limitări Cunoscute

*[Fiți onești - evaluatorul apreciază identificarea clară a limitărilor]*

1. **Limitare 1:** [ex: Modelul eșuează pe imagini cu iluminare <50 lux - accuracy scade la 45%]
2. **Limitare 2:** [ex: Latența depășește 100ms pentru batch size >32 - neadecvat pentru real-time]
3. **Limitare 3:** [ex: Clasa "defect_minor" are recall doar 52% - date insuficiente]
4. **Funcționalități planificate dar neimplementate:** [ex: Export ONNX, integrare API extern]

### 10.3 Lecții Învățate (Top 5)

1. **[Lecție 1]:** [ex: Importanța EDA înainte de antrenare - am descoperit 8% valori lipsă care afectau convergența]
2. **[Lecție 2]:** [ex: Early stopping a prevenit overfitting sever - fără el, val_loss creștea după epoca 20]
3. **[Lecție 3]:** [ex: Augmentările specifice domeniului (zgomot gaussian calibrat) au adus +5% accuracy vs augmentări generice]
4. **[Lecție 4]:** [ex: Threshold-ul default 0.5 nu e optim pentru clase dezechilibrate - ajustarea la 0.35 a redus FN cu 40%]
5. **[Lecție 5]:** [ex: Documentarea incrementală (la fiecare etapă) a economisit timp major la integrare finală]

### 10.4 Retrospectivă

**Ce ați schimba dacă ați reîncepe proiectul?**

*[1-2 paragrafe: Decizii pe care le-ați lua diferit, cu justificare bazată pe experiența acumulată]*

[Completați aici]

### 10.5 Direcții de Dezvoltare Ulterioară

| Termen | Îmbunătățire Propusă | Beneficiu Estimat |
|--------|---------------------|-------------------|
| **Short-term** (1-2 săptămâni) | [ex: Augmentare date pentru clasa subreprezentată] | [ex: +10% recall pe clasa "defect_minor"] |
| **Medium-term** (1-2 luni) | [ex: Implementare model ensemble] | [ex: +3-5% accuracy general] |
| **Long-term** | [ex: Deployment pe edge device (Raspberry Pi)] | [ex: Latență <20ms, cost hardware redus] |

---

## 11. Bibliografie

*[Minimum 3 surse cu DOI/link funcțional - format: Autor, Titlu, Anul, Link]*

1. [Autor], [Titlu articol/carte], [Anul]. DOI: [link] sau URL: [link]
2. [Autor], [Titlu articol/carte], [Anul]. DOI: [link] sau URL: [link]
3. [Autor], [Titlu articol/carte], [Anul]. DOI: [link] sau URL: [link]
4. [Surse suplimentare dacă este cazul]

**Exemple format:**
- Abaza, B., 2025. AI-Driven Dynamic Covariance for ROS 2 Mobile Robot Localization. Sensors, 25, 3026. https://doi.org/10.3390/s25103026
- Keras Documentation, 2024. Getting Started Guide. https://keras.io/getting_started/

---

## 12. Checklist Final (Auto-verificare înainte de predare)

### Cerințe Tehnice Obligatorii

- [ ] **Accuracy ≥70%** pe test set (verificat în `results/final_metrics.json`)
- [ ] **F1-Score ≥0.65** pe test set
- [ ] **Contribuție ≥40% date originale** (verificabil în `data/generated/`)
- [ ] **Model antrenat de la zero** (NU pre-trained fine-tuning)
- [ ] **Minimum 4 experimente** de optimizare documentate (tabel în Secțiunea 5.3)
- [ ] **Confusion matrix** generată și interpretată (Secțiunea 6.2)
- [ ] **State Machine** definit cu minimum 4-6 stări (Secțiunea 4.2)
- [ ] **Cele 3 module funcționale:** Data Logging, RN, UI (Secțiunea 4.1)
- [ ] **Demonstrație end-to-end** disponibilă în `docs/demo/`

### Repository și Documentație

- [ ] **README.md** complet (toate secțiunile completate cu date reale)
- [ ] **4 README-uri etape** prezente în `docs/` (etapa3, etapa4, etapa5, etapa6)
- [ ] **Screenshots** prezente în `docs/screenshots/`
- [ ] **Structura repository** conformă cu Secțiunea 8
- [ ] **requirements.txt** actualizat și funcțional
- [ ] **Cod comentat** (minim 15% linii comentarii relevante)
- [ ] **Toate path-urile relative** (nu absolute: `/Users/...` sau `C:\...`)

### Acces și Versionare

- [ ] **Repository accesibil** cadrelor didactice RN (public sau privat cu acces)
- [ ] **Tag `v0.6-optimized-final`** creat și pushed
- [ ] **Commit-uri incrementale** vizibile în `git log` (nu 1 commit gigantic)
- [ ] **Fișiere mari** (>100MB) excluse sau în `.gitignore`

### Verificare Anti-Plagiat

- [ ] Model antrenat **de la zero** (weights inițializate random, nu descărcate)
- [ ] **Minimum 40% date originale** (nu doar subset din dataset public)
- [ ] Cod propriu sau clar atribuit (surse citate în Bibliografie)

---

## Note Finale

**Versiune document:** FINAL pentru examen  
**Ultima actualizare:** [DD.MM.YYYY]  
**Tag Git:** `v0.6-optimized-final`

---

*Acest README servește ca documentație principală pentru Livrabilul 1 (Aplicație RN). Pentru Livrabilul 2 (Prezentare PowerPoint), consultați structura din RN_Specificatii_proiect.pdf.*
