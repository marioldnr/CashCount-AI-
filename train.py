"""YOLO-Modell trainieren.  Beispiel: python train.py --epochs 100"""
import argparse

from ultralytics import YOLO

from cashcount.config import BASE_MODEL, DATA_YAML, IMG_SIZE, RUNS_DIR

p = argparse.ArgumentParser()
p.add_argument("--epochs", type=int, default=100)
p.add_argument("--batch", type=int, default=16)
p.add_argument("--name", default="train")
p.add_argument("--device", default=None, help="z. B. 0 für GPU oder cpu")
a = p.parse_args()

model = YOLO(BASE_MODEL)
model.train(
    data=str(DATA_YAML),
    epochs=a.epochs,
    imgsz=IMG_SIZE,
    batch=a.batch,
    project=str(RUNS_DIR),
    name=a.name,
    device=a.device,
)
