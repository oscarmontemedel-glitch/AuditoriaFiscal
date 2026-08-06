"""
=========================================================
SAF v13.0
Cruce UUID vs Libro Mayor
=========================================================
"""

from motor.cruces.cruce_base import CruceBase


class CruceUUIDLibro(CruceBase):

    def ejecutar(self, modelo, hallazgos):

        if modelo.cfdi.empty:
            return

        if modelo.libro.empty:
            return

        print()
        print("===================================")
        print("CRUCE UUID vs LIBRO MAYOR")
        print("===================================")

        cfdi = modelo.cfdi.dataframe()

        encontrados = 0
        faltantes = 0

        for _, fila in cfdi.iterrows():

            uuid = str(

                fila.get("UUID", "")

            ).strip()

            if uuid == "":
                continue

            if modelo.libro.contiene(uuid):

                encontrados += 1

            else:

                faltantes += 1

                hallazgos.agregar(

                    regla="UUID sin Libro",

                    riesgo="ALTO",

                    prioridad="ALTO",

                    archivo="LIBRO MAYOR",

                    hoja="-",

                    evidencia=uuid,

                    observacion="El UUID del CFDI no fue localizado en el Libro Mayor."

                )

        print(f"UUID encontrados : {encontrados}")
        print(f"UUID faltantes   : {faltantes}")

        print("Cruce terminado.")