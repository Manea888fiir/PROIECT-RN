import os
import shutil
import random

# Configurare cai
FOLDER_SURSA = "data/raw"             # Unde sunt pozele originale
FOLDER_DESTINATIE = "data/processed"  # Unde le mutam impartite

def split_dataset(train_ratio=0.7, val_ratio=0.2):
    # Creare foldere
    for tip in ['train', 'val', 'test']:
        os.makedirs(f"{FOLDER_DESTINATIE}/{tip}/images", exist_ok=True)
        os.makedirs(f"{FOLDER_DESTINATIE}/{tip}/labels", exist_ok=True)

    # Citire fisiere
    if not os.path.exists(FOLDER_SURSA):
        print("Folderul sursa nu exista. Acest script este demonstrativ.")
        return

    fisiere = [f for f in os.listdir(FOLDER_SURSA) if f.endswith('.jpg')]
    random.shuffle(fisiere)

    # Calcul indecsi
    total = len(fisiere)
    train_end = int(total * train_ratio)
    val_end = train_end + int(total * val_ratio)

    # Impartire
    dataset = {
        'train': fisiere[:train_end],
        'val': fisiere[train_end:val_end],
        'test': fisiere[val_end:]
    }

    print(f"Impartire: Train={len(dataset['train'])}, Val={len(dataset['val'])}, Test={len(dataset['test'])}")

    # Simulare mutare (sau mutare reala daca ai fisierele)
    for tip, lista_poze in dataset.items():
        for poza in lista_poze:
            # Aici s-ar face copy/move
            pass 

    print("Structura de date a fost creata cu succes!")

if __name__ == "__main__":
    split_dataset()