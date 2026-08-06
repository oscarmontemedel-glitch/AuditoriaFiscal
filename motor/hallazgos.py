"""
=========================================================
SAF v13.0
Administrador de Hallazgos
=========================================================
"""

import pandas as pd

from motor.hallazgo import Hallazgo


class Hallazgos:

    def __init__(self):

        self._hallazgos = []

    # =====================================================

    def agregar(

        self,

        regla,

        riesgo,

        prioridad,

        archivo,

        hoja,

        evidencia,

        observacion,

        fundamento="",

        recomendacion=""

    ):

        self._hallazgos.append(

            Hallazgo(

                regla,

                riesgo,

                prioridad,

                archivo,

                hoja,

                evidencia,

                observacion,

                fundamento,

                recomendacion

            )

        )

    # =====================================================

    def dataframe(self):

        datos = [

            h.diccionario()

            for h in self._hallazgos

        ]

        return pd.DataFrame(datos)

    # =====================================================

    def total(self):

        return len(self._hallazgos)

    # =====================================================

    def limpiar(self):

        self._hallazgos.clear()

    # =====================================================

    def resumen(self):

        print()

        print("=" * 60)

        print("RESUMEN HALLAZGOS")

        print("=" * 60)

        print(

            f"Total: {self.total()}"

        )