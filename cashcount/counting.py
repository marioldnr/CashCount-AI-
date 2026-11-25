"""Erkannte Scheine in einen Gesamtbetrag umrechnen."""
from collections import Counter

from .config import EURO_WERTE


def zaehle(ergebnis, min_conf: float = 0.5) -> tuple[Counter, int]:
    """Gibt (Anzahl je Wert, Gesamtbetrag) für ein Ultralytics-Ergebnis zurück."""
    anzahl = Counter()
    for cls, conf in zip(ergebnis.boxes.cls.tolist(), ergebnis.boxes.conf.tolist()):
        if conf >= min_conf:
            anzahl[EURO_WERTE[int(cls)]] += 1
    summe = sum(wert * n for wert, n in anzahl.items())
    return anzahl, summe
