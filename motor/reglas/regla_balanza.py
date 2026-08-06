"""
=========================================================
SAF v13.0
Regla Balanza
=========================================================
"""


class ReglaBalanza:

    def ejecutar(self, modelo, hallazgos):

        if modelo.balanza.empty:
            return

        print("Validando Balanza...")

        df = modelo.balanza.dataframe()

        # ==========================================
        # BALANZA VACÍA
        # ==========================================

        if len(df) == 0:

            hallazgos.agregar(

                regla="Balanza",

                riesgo="CRITICO",

                prioridad="CRITICO",

                archivo="BALANZA",

                hoja="-",

                evidencia="0 registros",

                observacion="La balanza no contiene información."

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

                    archivo="BALANZA",

                    hoja=fila.get("HOJA", ""),

                    evidencia="",

                    observacion="Cuenta contable vacía."

                )

        # ==========================================
        # SALDOS NEGATIVOS
        # ==========================================

        if "SALDO_FINAL" in df.columns:

            for _, fila in df.iterrows():

                try:

                    saldo = float(

                        fila.get("SALDO_FINAL", 0)

                    )

                except Exception:

                    continue

                if saldo < 0:

                    hallazgos.agregar(

                        regla="Saldo Final",

                        riesgo="MEDIO",

                        prioridad="MEDIA",

                        archivo="BALANZA",

                        hoja=fila.get("HOJA", ""),

                        evidencia=fila.get("CUENTA", ""),

                        observacion="Saldo final negativo."

                    )

        # ==========================================
        # CUENTAS DUPLICADAS
        # ==========================================

        if "CUENTA" in df.columns:

            duplicadas = df[

                df["CUENTA"]

                .duplicated(

                    keep=False

                )

            ]

            for _, fila in duplicadas.iterrows():

                hallazgos.agregar(

                    regla="Cuenta Duplicada",

                    riesgo="MEDIO",

                    prioridad="MEDIA",

                    archivo="BALANZA",

                    hoja=fila.get("HOJA", ""),

                    evidencia=fila.get("CUENTA", ""),

                    observacion="Cuenta duplicada en la balanza."

                )

        print("OK")