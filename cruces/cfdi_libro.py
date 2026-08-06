"""
=========================================================
SAF v7.0
Cruce CFDI vs Libro Mayor
=========================================================
"""

import pandas as pd

from adaptadores.cfdi import AdaptadorCFDI


class CruceCFDILibro:

    def __init__(self, repo):

        self.repo = repo

    def ejecutar(self):

        cfdi = AdaptadorCFDI(

            self.repo

        ).obtener()

        libro = self.repo.obtener(

            "LIBRO MAYOR"

        )

        if cfdi.empty:

            return pd.DataFrame()

        if not libro:

            return pd.DataFrame()

        libro_df = list(

            libro.values()

        )[0]

        texto = (

            libro_df.astype(str)

            .agg(

                " ".join,

                axis=1

            )

            .str.upper()

        )

        resultado = []

        for _, fila in cfdi.iterrows():

            uuid = str(

                fila["UUID"]

            ).upper()

            encontrado = texto.str.contains(

                uuid,

                regex=False

            ).any()

            resultado.append({

                "UUID": uuid,

                "RFC_EMISOR": fila["RFC_EMISOR"],

                "RFC_RECEPTOR": fila["RFC_RECEPTOR"],

                "TOTAL": fila["TOTAL"],

                "ENCONTRADO_LIBRO": "SI" if encontrado else "NO"

            })

        return pd.DataFrame(

            resultado

        )