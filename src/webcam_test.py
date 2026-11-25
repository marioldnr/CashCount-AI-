from ultralytics import YOLO
import cv2
import sys

# Fertiges Modell (erkennt Alltagsgegenstände). Wird beim ersten Start automatisch heruntergeladen.
model = YOLO("yolov8n.pt")

# 0 = eingebaute Webcam. Bei externer Kamera evtl. 1 probieren.
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Kamera konnte nicht geöffnet werden.")
    sys.exit()

while True:
    ok, frame = cap.read()        # ein Bild von der Kamera holen
    if not ok:
        break

    result = model(frame, verbose=False)[0]   # KI auf das Bild anwenden
    bild_mit_rahmen = result.plot()           # Rahmen + Beschriftung einzeichnen

    cv2.imshow("CashCount Test - Beenden mit q", bild_mit_rahmen)

    if cv2.waitKey(1) & 0xFF == ord("q"):     # Taste q beendet
        break

cap.release()
cv2.destroyAllWindows()