"""
=========================================================
SAF v8.0
Adaptador Libro Mayor
=========================================================
"""

import pandas as pd


class AdaptadorLibroMayor:

    def __init__(self, repo):

        self.repo = repo

    def obtener(self):

        hojas = self.repo.obtener("LIBRO MAYOR")

        if not hojas:

            print("⚠ No se encontró Libro Mayor en el repositorio.")

            return pd.DataFrame()

        dataframes = []

        for nombre_hoja, df in hojas.items():

            if df.empty:

                continue

            copia = df.copy()

            copia["__HOJA__"] = nombre_hoja

            dataframes.append(copia)

        if not dataframes:

            return pd.DataFrame()

        libro = pd.concat(

            dataframes,

            ignore_index=True

        )

        libro.columns = [

            str(col).strip().upper()

            for col in libro.columns

        ]

        libro = libro.dropna(

            how="all"

        )

        print()

        print("===================================")
        print("ADAPTADOR LIBRO MAYOR")
        print("===================================")

        print(f"Hojas leídas : {len(hojas)}")
        print(f"Registros    : {len(libro)}")
        print(f"Columnas     : {len(libro.columns)}")

        return libro