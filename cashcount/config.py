"""Gemeinsame Einstellungen für CashCount AI."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_YAML = ROOT / "data.yaml"
RUNS_DIR = ROOT / "runs"

BASE_MODEL = "yolo11n.pt"  # YOLO-Nano laut Drehbuch
IMG_SIZE = 640

# Klassennummer -> Wert in Euro (Reihenfolge wie in data.yaml)
EURO_WERTE = {0: 5, 1: 10, 2: 20, 3: 50, 4: 100, 5: 200}
