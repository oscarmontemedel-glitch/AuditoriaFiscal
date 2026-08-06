from io import BytesIO
import zipfile
import traceback

import pandas as pd

from config import ARCHIVO_ZIP
from utilidades.reparar_excel import reparar_excel_bytes

ARCHIVO = "LIBRO MAYOR DIKEN DE MEXICO MAY26.xlsx"

print("=" * 70)
print("DIAGNÓSTICO LIBRO MAYOR")
print("=" * 70)

with zipfile.ZipFile(ARCHIVO_ZIP, "r") as z:
    with z.open(ARCHIVO) as f:
        contenido = f.read()

print("Reparando...")

contenido = reparar_excel_bytes(contenido)

print("Abriendo...")

libro = pd.ExcelFile(
    BytesIO(contenido),
    engine="openpyxl"
)

print("Workbook OK")
print(libro.sheet_names)

print("\nIntentando leer Sheet1...")

try:

    df = pd.read_excel(
        libro,
        sheet_name="Sheet1",
        header=None,
        dtype=str
    )

    print("\nLECTURA EXITOSA")
    print(df.head())

except Exception:
    traceback.print_exc()