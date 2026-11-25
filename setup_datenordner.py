"""Legt die Ordnerstruktur für den gemeinsamen Datenordner CashCountAI_Daten an.

Aufruf:
    python setup_datenordner.py <Zielpfad> [--export v1_2026-12-01]

Bestehende Ordner und ein vorhandenes Aufnahmeprotokoll bleiben unverändert.
"""
import argparse
from pathlib import Path

from openpyxl import Workbook

# Sessions laut Drehbuch (Aufnahmeplan)
SESSIONS = [
    "S01_weiss_tageslicht",
    "S02_weiss_deckenlampe",
    "S03_holz_seitenlicht",
    "S04_schwarz_led",
    "S05_weiss_diffus",
    "S06_holz_hand",
    "S07_schwarz_dunkel",
    "S08_gemischt_stoerobjekte",
    "S09_negativ",
    "S10_test",
    "Aussortiert",
]
SPLITS = ["train", "valid", "test"]
PROTOKOLL_SPALTEN = ["Session", "Datum", "Person", "Scheine", "Anzahl"]


def anlegen(ziel: Path, export: str) -> None:
    basis = ziel / "CashCountAI_Daten"

    for s in SESSIONS:
        (basis / "01_Rohbilder" / s).mkdir(parents=True, exist_ok=True)

    export_dir = basis / "02_Roboflow_Export" / export
    for split in SPLITS:
        for sub in ("images", "labels"):
            (export_dir / split / sub).mkdir(parents=True, exist_ok=True)

    (basis / "03_Modelle").mkdir(parents=True, exist_ok=True)

    protokoll = basis / "Aufnahmeprotokoll.xlsx"
    if not protokoll.exists():
        wb = Workbook()
        ws = wb.active
        ws.title = "Aufnahmen"
        ws.append(PROTOKOLL_SPALTEN)
        wb.save(protokoll)

    print(f"Struktur angelegt in: {basis}")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("ziel", type=Path, help="Ordner, in dem CashCountAI_Daten entstehen soll")
    p.add_argument("--export", default="v1_2026-12-01", help="Name des Roboflow-Export-Ordners")
    a = p.parse_args()
    anlegen(a.ziel, a.export)
