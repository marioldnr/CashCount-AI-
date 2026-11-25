"""Modell auf dem Testdatensatz auswerten (mAP50, Konfusionsmatrix).
Beispiel: python evaluate.py runs/train/weights/best.pt
"""
import argparse

from ultralytics import YOLO

from cashcount.config import DATA_YAML, IMG_SIZE, RUNS_DIR

p = argparse.ArgumentParser()
p.add_argument("weights")
a = p.parse_args()

metrics = YOLO(a.weights).val(
    data=str(DATA_YAML), split="test", imgsz=IMG_SIZE, project=str(RUNS_DIR), name="test"
)
print(f"mAP50: {metrics.box.map50:.3f}  (Ziel: >= 0.90)")
