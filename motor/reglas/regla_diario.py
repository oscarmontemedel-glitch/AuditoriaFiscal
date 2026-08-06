"""
=========================================================
SAF v13.0
Regla Diario General
=========================================================
"""


class ReglaDiario:

    def ejecutar(self, modelo, hallazgos):

        if modelo.diario.empty:
            return

        print("Validando Diario General...")

        df = modelo.diario.dataframe()

        # ==========================================
        # DIARIO VACÍO
        # ==========================================

        if len(df) == 0:

            hallazgos.agregar(

                regla="Diario General",

                riesgo="CRITICO",

                prioridad="CRITICO",

                archivo="DIARIO",

                hoja="-",

                evidencia="0 registros",

                observacion="El Diario General no contiene movimientos."

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

                    archivo="DIARIO",

                    hoja=fila.get("HOJA", ""),

                    evidencia="",

                    observacion="Movimiento sin cuenta contable."

                )

        # ==========================================
        # PÓLIZAS VACÍAS
        # ==========================================

        if "POLIZA" in df.columns:

            vacias = (

                df["POLIZA"]

                .fillna("")

                .astype(str)

                .str.strip()

                == ""

            )

            for _, fila in df[vacias].iterrows():

                hallazgos.agregar(

                    regla="Póliza",

                    riesgo="MEDIO",

                    prioridad="MEDIA",

                    archivo="DIARIO",

                    hoja=fila.get("HOJA", ""),

                    evidencia=fila.get("CUENTA", ""),

                    observacion="Movimiento sin número de póliza."

                )

        # ==========================================
        # FECHAS VACÍAS
        # ==========================================

        if "FECHA" in df.columns:

            vacias = (

                df["FECHA"]

                .fillna("")

                .astype(str)

                .str.strip()

                == ""

            )

            for _, fila in df[vacias].iterrows():

                hallazgos.agregar(

                    regla="Fecha",

                    riesgo="MEDIO",

                    prioridad="MEDIA",

                    archivo="DIARIO",

                    hoja=fila.get("HOJA", ""),

                    evidencia=fila.get("POLIZA", ""),

                    observacion="Movimiento sin fecha."

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

                riesgo="BAJO",

                prioridad="BAJA",

                archivo="DIARIO",

                hoja=fila.get("HOJA", ""),

                evidencia=fila.get("POLIZA", ""),

                observacion="Movimiento duplicado en Diario General."

            )

        print("OK")