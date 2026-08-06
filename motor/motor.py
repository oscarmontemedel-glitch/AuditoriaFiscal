"""
=========================================================
SAF v13.0
Motor Central de Reglas
=========================================================
"""

from motor.hallazgos import Hallazgos
from motor.registro import (
    obtener_reglas,
    obtener_cruces
)


class Motor:

    def __init__(self, modelo):

        self.modelo = modelo

        self.hallazgos = Hallazgos()

        self.reglas = obtener_reglas()

        self.cruces = obtener_cruces()

    # =====================================================
    # REGLAS
    # =====================================================

    def ejecutar_reglas(self):

        print()
        print("=" * 60)
        print("MOTOR DE REGLAS")
        print("=" * 60)

        for regla in self.reglas:

            print(
                f"Ejecutando {regla.__class__.__name__}..."
            )

            regla.ejecutar(

                self.modelo,

                self.hallazgos

            )

    # =====================================================
    # CRUCES
    # =====================================================

    def ejecutar_cruces(self):

        print()
        print("=" * 60)
        print("MOTOR DE CRUCES")
        print("=" * 60)

        for cruce in self.cruces:

            print(
                f"Ejecutando {cruce.__class__.__name__}..."
            )

            cruce.ejecutar(

                self.modelo,

                self.hallazgos

            )

    # =====================================================
    # EJECUCIÓN GENERAL
    # =====================================================

    def ejecutar(self):

        self.ejecutar_reglas()

        self.ejecutar_cruces()

        print()
        print("=" * 60)
        print("RESUMEN")
        print("=" * 60)

        print(
            f"Hallazgos encontrados : {self.hallazgos.total()}"
        )

        return self.hallazgos.dataframe()