from io import BytesIO
import zipfile

from config import ARCHIVO_ZIP

ARCHIVO = "LIBRO MAYOR DIKEN DE MEXICO MAY26.xlsx"

with zipfile.ZipFile(ARCHIVO_ZIP) as z:

    with z.open(ARCHIVO) as f:

        contenido = f.read()

excel = BytesIO(contenido)

with zipfile.ZipFile(excel) as libro:

    xml = libro.read(

        "xl/worksheets/sheet1.xml"

    ).decode(

        "utf-8",

        errors="ignore"

    )

for linea in xml.split(">"):

    if "sheetFormatPr" in linea:

        print(linea + ">")