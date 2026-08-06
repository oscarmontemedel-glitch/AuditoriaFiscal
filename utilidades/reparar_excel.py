"""
=========================================================
SAF v10.0
Reparador Excel CONTPAQi
=========================================================

Corrige archivos XLSX generados por CONTPAQi que
incluyen el atributo:

customWidth

dentro del nodo:

<sheetFormatPr>

=========================================================
"""

from io import BytesIO
import zipfile
import re


def reparar_excel_bytes(excel_bytes):

    entrada = BytesIO(excel_bytes)

    salida = BytesIO()

    with zipfile.ZipFile(entrada, "r") as zin:

        with zipfile.ZipFile(salida, "w", zipfile.ZIP_DEFLATED) as zout:

            for item in zin.infolist():

                contenido = zin.read(item.filename)

                # -------------------------------------------------
                # SOLO reparar hojas
                # -------------------------------------------------

                if item.filename.startswith("xl/worksheets/") and item.filename.endswith(".xml"):

                    texto = contenido.decode(

                        "utf-8",

                        errors="ignore"

                    )

                    # Eliminar cualquier atributo customWidth
                    texto = re.sub(

                        r'\s*customWidth="[^"]+"',

                        "",

                        texto

                    )

                    contenido = texto.encode(

                        "utf-8"

                    )

                zout.writestr(

                    item,

                    contenido

                )

    salida.seek(0)

    return salida.getvalue()