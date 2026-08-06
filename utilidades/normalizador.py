"""
=========================================================
SAF v9.0
Normalizador de DataFrames
=========================================================
"""

import re
import unicodedata

from modelo.diccionario_contable import DICCIONARIO


# ==========================================================
# UTILIDADES
# ==========================================================

def quitar_acentos(texto):

    texto = unicodedata.normalize("NFKD", str(texto))

    return "".join(

        c

        for c in texto

        if not unicodedata.combining(c)

    )


def limpiar_nombre(nombre):

    nombre = quitar_acentos(nombre)

    nombre = nombre.upper()

    nombre = nombre.replace("\n", " ")

    nombre = re.sub(r"\s+", " ", nombre)

    nombre = nombre.strip()

    nombre = nombre.replace("N°", "NUMERO")

    nombre = nombre.replace("NO.", "NUMERO")

    nombre = nombre.replace("NO ", "NUMERO ")

    return nombre


# ==========================================================
# NORMALIZADOR
# ==========================================================

def normalizar_dataframe(df):

    columnas = []

    usadas = set()

    for columna in df.columns:

        nombre = limpiar_nombre(columna)

        if nombre.startswith("UNNAMED"):

            continue

        if nombre == "":

            continue

        nombre = DICCIONARIO.get(

            nombre,

            nombre

        )

        if nombre in usadas:

            continue

        usadas.add(nombre)

        columnas.append(

            (columna, nombre)

        )

    originales = [

        c[0]

        for c in columnas

    ]

    df = df[originales].copy()

    df.columns = [

        c[1]

        for c in columnas

    ]

    df = df.dropna(

        how="all"

    )

    return df