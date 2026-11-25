# CashCount AI

KI-gestützte Erkennung und Zählung von Euro-Banknoten mit YOLO (Ultralytics, Nano).

## Struktur

```
data.yaml                 Datensatz-Konfiguration (Klassen eur5 … eur200)
train.py                  Training
evaluate.py               Auswertung auf dem Testdatensatz (mAP50)
count.py                  Erkennen und Zählen auf Bild oder Webcam
cashcount/                gemeinsamer Code (Einstellungen, Zähllogik)
scripts/setup_datenordner.py   legt den Cloud-Datenordner an
datasets/                 lokale Kopie des Roboflow-Exports (nicht im Git)
runs/                     Trainingsergebnisse (nicht im Git)
```

## Ablauf

```
pip install -r requirements.txt
python scripts/setup_datenordner.py "<Cloud-Ordner>"
# Roboflow-Export nach datasets/v1/ kopieren
python train.py --epochs 100
python evaluate.py runs/train/weights/best.pt
python count.py runs/train/weights/best.pt --quelle 0
```

Bilder und Modelle gehören nicht ins Repository.
