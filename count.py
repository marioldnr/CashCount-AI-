"""Scheine auf einem Bild oder live über die Webcam erkennen und zählen.
Beispiele:
    python count.py runs/train/weights/best.pt --quelle bild.jpg
    python count.py runs/train/weights/best.pt --quelle 0      (Webcam)
"""
import argparse

import cv2
from ultralytics import YOLO

from cashcount.counting import zaehle

p = argparse.ArgumentParser()
p.add_argument("weights")
p.add_argument("--quelle", default="0", help="Bildpfad oder Kameranummer")
p.add_argument("--conf", type=float, default=0.5)
a = p.parse_args()

model = YOLO(a.weights)
quelle = int(a.quelle) if a.quelle.isdigit() else a.quelle

for ergebnis in model.predict(quelle, conf=a.conf, stream=True):
    anzahl, summe = zaehle(ergebnis, a.conf)
    bild = ergebnis.plot()
    cv2.putText(bild, f"Summe: {summe} EUR", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
    print(dict(sorted(anzahl.items())), f"= {summe} EUR")
    cv2.imshow("CashCount AI", bild)
    if cv2.waitKey(0 if isinstance(quelle, str) else 1) & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()
