"""
=========================================================
SAF v13.0
Cruce CFDI vs Libro Mayor
=========================================================
"""

import pandas as pd

from motor.cruces.cruce_base import CruceBase


class CruceCFDILibro(CruceBase):

    def ejecutar(self, modelo, hallazgos):

        if modelo.cfdi.empty:
            return

        if modelo.libro.empty:
            return

        print()
        print("===================================")
        print("CRUCE CFDI vs LIBRO MAYOR")
        print("===================================")

        cfdi = modelo.cfdi.dataframe()

        libro = modelo.libro.dataframe()

        columnas = modelo.libro.columnas_numericas()

        if not columnas:

            print("No existen columnas numéricas en Libro Mayor.")
            return

        total_cfdi = modelo.cfdi.total_monto()

        total_libro = modelo.libro.total_columna(

            columnas[0]

        )

        diferencia = abs(

            total_cfdi -

            total_libro

        )

        print(f"CFDI       : {total_cfdi:,.2f}")
        print(f"Libro      : {total_libro:,.2f}")
        print(f"Diferencia : {diferencia:,.2f}")

        if diferencia > 1:

            hallazgos.agregar(

                regla="Cruce CFDI vs Libro",

                riesgo="CRITICO",

                prioridad="CRITICO",

                archivo="LIBRO MAYOR",

                hoja="-",

                evidencia=f"{diferencia:,.2f}",

                observacion="El importe del Libro Mayor no coincide con CFDI."

            )

        if "UUID" in cfdi.columns:

            for _, fila in cfdi.iterrows():

                uuid = str(

                    fila.get("UUID", "")

                ).strip()

                if uuid == "":
                    continue

                if not modelo.libro.contiene(uuid):

                    hallazgos.agregar(

                        regla="UUID sin Libro",

                        riesgo="MEDIO",

                        prioridad="MEDIA",

                        archivo="LIBRO MAYOR",

                        hoja="-",

                        evidencia=uuid,

                        observacion="UUID no localizado en Libro Mayor."

                    )

        print("Cruce terminado.")