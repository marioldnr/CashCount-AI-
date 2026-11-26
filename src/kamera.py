import cv2

HANDY = 1     # Nummer aus kamera_finden.py
WEBCAM = 0


def oeffne_kamera():
    """Nimmt das Handy, wenn angeschlossen, sonst die Webcam."""
    for nummer, name in [(HANDY, "Handy"), (WEBCAM, "Webcam")]:
        cap = cv2.VideoCapture(nummer)
        if cap.isOpened():
            ok, _ = cap.read()
            if ok:
                print(f"Kamera: {name} (Nummer {nummer})")
                return cap
        cap.release()

    raise RuntimeError("Keine Kamera gefunden.")