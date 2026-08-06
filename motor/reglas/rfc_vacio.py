"""
=========================================================
Regla RFC Vacío
=========================================================
"""

import pandas as pd

from motor.reglas.regla_base import ReglaBase


class RFCVacio(ReglaBase):

    COLUMNAS = [

        "RFC",

        "RFC_EMISOR",

        "RFC_RECEPTOR",

        "RFC_CLIENTE",

        "RFC_PROVEEDOR"

    ]

    def ejecutar(self, movimientos):

        errores = []

        for columna in self.COLUMNAS:

            if columna not in movimientos.columns:

                continue

            vacios = movimientos[

                movimientos[columna]

                .fillna("")

                .astype(str)

                .str.strip()

                == ""

            ]

            if vacios.empty:

                continue

            copia = vacios.copy()

            copia["REGLA"] = self.nombre

            copia["COLUMNA"] = columna

            errores.append(copia)

        if errores:

            return pd.concat(

                errores,

                ignore_index=True

            )

        return pd.DataFrame()