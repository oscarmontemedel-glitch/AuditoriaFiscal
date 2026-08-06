"""
=========================================================
SAF v13.0
Motor Central de Reglas y Cruces
=========================================================
"""

from motor.motor import Motor


class MotorReglas:

    def __init__(self, modelo):

        self.motor = Motor(modelo)

    # =====================================================
    # EJECUTAR
    # =====================================================

    def ejecutar(self):

        resultado = self.motor.ejecutar()

        return resultado