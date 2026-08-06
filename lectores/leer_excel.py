"""
=========================================================
SAF v10.0
Motor Inteligente de Lectura Excel
=========================================================
"""

from io import BytesIO
import zipfile

import pandas as pd

from utilidades.header_detector import detectar_fila_encabezado
from utilidades.normalizador import normalizar_dataframe
from utilidades.tipos import tipar_dataframe
from utilidades.reparar_excel import reparar_excel_bytes


# ==========================================================
# APERTURA SEGURA DEL LIBRO
# ==========================================================

def abrir_libro(contenido):

    # Reparar SIEMPRE el archivo
    contenido = reparar_excel_bytes(contenido)

    return pd.ExcelFile(

        BytesIO(contenido),

        engine="openpyxl"

    )


# ==========================================================
# LECTURA DE UNA HOJA
# ==========================================================

def leer_hoja(libro, hoja):

    temporal = pd.read_excel(

        libro,

        sheet_name=hoja,

        header=None,

        dtype=str

    )

    fila = detectar_fila_encabezado(

        temporal

    )

    df = pd.read_excel(

        libro,

        sheet_name=hoja,

        header=fila,

        dtype=str

    )

    df.columns = (

        df.columns

        .astype(str)

        .str.strip()

        .str.replace("\n", " ", regex=False)

        .str.upper()

    )

    df = df.loc[:, ~df.columns.duplicated()]

    df = df.dropna(

        how="all"

    )

    df = normalizar_dataframe(

        df

    )

    df = tipar_dataframe(

        df

    )

    return {

        "dataframe": df,

        "encabezado": fila,

        "filas": len(df),

        "columnas": len(df.columns)

    }


# ==========================================================
# LECTURA DEL ZIP
# ==========================================================

def leer_excel_zip(ruta_zip, archivo_excel):

    datos = {}

    with zipfile.ZipFile(

        ruta_zip,

        "r"

    ) as z:

        with z.open(

            archivo_excel

        ) as archivo:

            contenido = archivo.read()

    libro = abrir_libro(

        contenido

    )

    print()
    print(f"📘 Leyendo: {archivo_excel}")

    for hoja in libro.sheet_names:

        print(f"   ├── {hoja}")

        try:

            info = leer_hoja(

                libro,

                hoja

            )

            datos[hoja] = info

        except Exception as e:

            print()
            print(f"❌ Error leyendo {hoja}")
            print(type(e).__name__)
            print(e)

    return datos