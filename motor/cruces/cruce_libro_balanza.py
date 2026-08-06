"""
=========================================================
SAF v13.0
Cruce Libro Mayor vs Balanza
=========================================================
"""

from motor.cruces.cruce_base import CruceBase


class CruceLibroBalanza(CruceBase):

    def ejecutar(self, modelo, hallazgos):

        if modelo.libro.empty:
            return

        if modelo.balanza.empty:
            return

        print()
        print("===================================")
        print("CRUCE LIBRO MAYOR vs BALANZA")
        print("===================================")

        columnas_libro = modelo.libro.columnas_numericas()
        columnas_balanza = modelo.balanza.columnas_numericas()

        if not columnas_libro:

            print("Libro Mayor sin columnas numéricas.")
            return

        if not columnas_balanza:

            print("Balanza sin columnas numéricas.")
            return

        total_libro = modelo.libro.total_columna(

            columnas_libro[0]

        )

        total_balanza = modelo.balanza.total_columna(

            columnas_balanza[0]

        )

        diferencia = abs(

            total_libro -

            total_balanza

        )

        print(f"Libro      : {total_libro:,.2f}")
        print(f"Balanza    : {total_balanza:,.2f}")
        print(f"Diferencia : {diferencia:,.2f}")

        if diferencia > 1:

            hallazgos.agregar(

                regla="Cruce Libro vs Balanza",

                riesgo="CRITICO",

                prioridad="CRITICO",

                archivo="BALANZA",

                hoja="-",

                evidencia=f"{diferencia:,.2f}",

                observacion="Los saldos del Libro Mayor y la Balanza no coinciden."

            )

        cuentas_libro = set(

            modelo.libro.buscar("").get("CUENTA", [])

        )

        cuentas_balanza = set(

            modelo.balanza.cuentas()

        )

        faltantes = cuentas_libro - cuentas_balanza

        for cuenta in sorted(faltantes):

            hallazgos.agregar(

                regla="Cuenta sin Balanza",

                riesgo="ALTO",

                prioridad="ALTO",

                archivo="BALANZA",

                hoja="-",

                evidencia=str(cuenta),

                observacion="La cuenta existe en Libro Mayor pero no en la Balanza."

            )

        print("Cruce terminado.")