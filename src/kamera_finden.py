import cv2

for i in range(4):
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        ok, _ = cap.read()
        print(f"Kamera {i}: {'funktioniert' if ok else 'geöffnet, aber kein Bild'}")
        cap.release()
    else:
        print(f"Kamera {i}: nicht vorhanden")