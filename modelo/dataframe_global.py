"""
Modelo Global de Datos

Une todos los DataFrames encontrados
en un único DataFrame.
"""

import pandas as pd


def crear_dataframe_global(datos):

    lista = []

    for archivo, hojas in datos.items():

        for hoja, df in hojas.items():

            df = df.copy()

            # ------------------------------------
            # Eliminar columnas duplicadas
            # ------------------------------------

            df = df.loc[:, ~df.columns.duplicated()]

            # ------------------------------------
            # Convertir nombres de columnas a texto
            # ------------------------------------

            df.columns = [
                str(col).strip()
                for col in df.columns
            ]

            # ------------------------------------
            # Agregar información de origen
            # ------------------------------------

            df["ARCHIVO"] = archivo
            df["HOJA"] = hoja

            lista.append(df)

    if not lista:

        return pd.DataFrame()

    try:

        global_df = pd.concat(
            lista,
            ignore_index=True,
            sort=False
        )

    except Exception as e:

        print("\n❌ ERROR AL CREAR DATAFRAME GLOBAL")

        print(e)

        return pd.DataFrame()

    return global_df