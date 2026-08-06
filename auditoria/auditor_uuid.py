"""
=========================================================
SAF v6.2
Auditor UUID
=========================================================
"""

import pandas as pd

from adaptadores.cfdi import AdaptadorCFDI


class AuditorUUID:

    def __init__(self, repo):

        self.repo = repo

    def ejecutar(self):

        cfdi = AdaptadorCFDI(

            self.repo

        ).obtener()

        if cfdi.empty:

            return pd.DataFrame()

        # ------------------------------------------
        # Normalización
        # ------------------------------------------

        cfdi["UUID"] = (

            cfdi["UUID"]

            .astype(str)

            .str.upper()

            .str.strip()

        )

        # ------------------------------------------
        # Conteo
        # ------------------------------------------

        conteo = (

            cfdi

            .groupby("UUID")

            .size()

            .reset_index(name="OCURRENCIAS")

        )

        resultado = cfdi.merge(

            conteo,

            on="UUID",

            how="left"

        )

        resultado["HALLAZGO"] = ""

        resultado.loc[

            resultado["OCURRENCIAS"] > 1,

            "HALLAZGO"

        ] = "UUID DUPLICADO"

        return resultado