"""
=========================================================
SAF v13.0
Regla Libro Mayor
=========================================================
"""


class ReglaLibroMayor:

    def ejecutar(self, modelo, hallazgos):

        if modelo.libro.empty:
            return

        print("Validando Libro Mayor...")

        df = modelo.libro.dataframe()

        # ==========================================
        # LIBRO VACÍO
        # ==========================================

        if len(df) == 0:

            hallazgos.agregar(

                regla="Libro Mayor",

                riesgo="CRITICO",

                prioridad="CRITICO",

                archivo="LIBRO MAYOR",

                hoja="-",

                evidencia="0 registros",

                observacion="El Libro Mayor no contiene movimientos."

            )

            return

        # ==========================================
        # CUENTAS VACÍAS
        # ==========================================

        if "CUENTA" in df.columns:

            vacias = (

                df["CUENTA"]

                .fillna("")

                .astype(str)

                .str.strip()

                == ""

            )

            for _, fila in df[vacias].iterrows():

                hallazgos.agregar(

                    regla="Cuenta Contable",

                    riesgo="ALTO",

                    prioridad="ALTO",

                    archivo="LIBRO MAYOR",

                    hoja=fila.get("__HOJA__", ""),

                    evidencia="",

                    observacion="Movimiento sin cuenta contable."

                )

        # ==========================================
        # REGISTROS DUPLICADOS
        # ==========================================

        duplicados = df.duplicated(

            keep=False

        )

        for _, fila in df[duplicados].iterrows():

            hallazgos.agregar(

                regla="Registro Duplicado",

                riesgo="MEDIO",

                prioridad="MEDIA",

                archivo="LIBRO MAYOR",

                hoja=fila.get("__HOJA__", ""),

                evidencia=fila.get("CUENTA", ""),

                observacion="Movimiento duplicado en Libro Mayor."

            )

        print("OK")