"""
=========================================================
SAF v5.1
Módulo Auditoría de Ingresos
=========================================================
"""

from repositorio.consultas import ConsultasRepositorio
from cruces.cruce_ingresos_cfdi import CruceIngresosCFDI


class AuditoriaIngresos:

    def __init__(self, repo):

        self.repo = repo

        self.consultas = ConsultasRepositorio(repo)

    def ejecutar(self):

        print("\n" + "=" * 60)
        print("AUDITORÍA DE INGRESOS")
        print("=" * 60)

        ingresos = self.consultas.ingresos()

        cfdi = self.consultas.cfdi()

        auxiliar = self.consultas.auxiliar()

        libro = self.consultas.libro_mayor()

        print(f"Hojas Ingresos   : {len(ingresos)}")
        print(f"Hojas CFDI       : {len(cfdi)}")
        print(f"Hojas Auxiliar   : {len(auxiliar)}")
        print(f"Hojas LibroMayor : {len(libro)}")

        print("\nEjecutando Cruce DM Ingresos vs CFDI...\n")

        cruce = CruceIngresosCFDI()

        resumen = cruce.ejecutar(

            ingresos,

            cfdi

        )

        print(resumen)

        return {

            "Resumen": resumen

        }