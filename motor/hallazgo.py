"""
=========================================================
SAF v13.0
Clase Hallazgo
=========================================================
"""


class Hallazgo:

    def __init__(

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

        self.regla = regla

        self.riesgo = riesgo

        self.prioridad = prioridad

        self.archivo = archivo

        self.hoja = hoja

        self.evidencia = evidencia

        self.observacion = observacion

        self.fundamento = fundamento

        self.recomendacion = recomendacion

    def diccionario(self):

        return {

            "Regla": self.regla,

            "Riesgo": self.riesgo,

            "Prioridad": self.prioridad,

            "Archivo": self.archivo,

            "Hoja": self.hoja,

            "Evidencia": self.evidencia,

            "Observacion": self.observacion,

            "Fundamento": self.fundamento,

            "Recomendacion": self.recomendacion

        }