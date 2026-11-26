import cv2
from ultralytics import YOLO

from kamera import oeffne_kamera

model = YOLO("models/best.pt")
werte = {"5_euro": 5, "10_euro": 10, "20_euro": 20, "50_euro": 50,
         "100_euro": 100, "200_euro": 200}

cap = oeffne_kamera()

while True:
    ok, frame = cap.read()
    if not ok:
        break

    result = model(frame, conf=0.5, verbose=False)[0]

    summe = 0
    for box in result.boxes:
        klasse = model.names[int(box.cls)]
        summe += werte.get(klasse, 0)

    bild = result.plot()
    cv2.putText(bild, f"Summe: {summe} EUR", (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)
    cv2.imshow("CashCount AI - Beenden mit q", bild)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()