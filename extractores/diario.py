"""
=========================================================
SAF v10.0
Extractor Diario General
=========================================================

Responsabilidad:

- Leer el reporte del Diario General.
- Detectar automáticamente pólizas.
- Detectar movimientos.
- Devolver un DataFrame limpio.

NO normaliza nombres de columnas.
NO convierte tipos.
NO realiza auditoría.

=========================================================
"""

import pandas as pd

from extractores.base import ExtractorBase


class ExtractorDiario(ExtractorBase):

    def __init__(self, repo):

        super().__init__(repo)

    def obtener(self):

        hojas = self.repo.obtener("DIARIO")

        if not hojas:

            print("⚠ No se encontró Diario General.")

            return pd.DataFrame()

        movimientos = []

        for nombre_hoja, df in hojas.items():

            df = self.limpiar_dataframe(df)

            poliza_actual = None
            fecha_actual = None
            tipo_actual = None

            for _, fila in df.iterrows():

                valores = [

                    str(v).strip()

                    for v in fila.tolist()

                ]

                valores = [

                    v for v in valores

                    if v != ""

                    and v.lower() != "nan"

                ]

                if len(valores) < 2:

                    continue

                # -------------------------------------------------
                # Detectar encabezado de póliza
                # -------------------------------------------------

                if (
                    len(valores) >= 3
                    and valores[0].isalpha()
                    and valores[1].isdigit()
                ):

                    tipo_actual = valores[0]

                    poliza_actual = valores[1]

                    fecha_actual = valores[2]

                    continue

                # -------------------------------------------------
                # Detectar movimiento
                # -------------------------------------------------

                cuenta = None

                for valor in valores:

                    if "-" in valor:

                        cuenta = valor

                        break

                if cuenta is None:

                    continue

                descripcion = ""

                if len(valores) > 1:

                    descripcion = " ".join(

                        valores[1:]

                    )

                movimientos.append({

                    "TIPO": tipo_actual,

                    "POLIZA": poliza_actual,

                    "FECHA": fecha_actual,

                    "CUENTA": cuenta,

                    "DESCRIPCION": descripcion,

                    "HOJA": nombre_hoja

                })

        diario = pd.DataFrame(movimientos)

        self.imprimir_resumen(

            "Extractor Diario",

            diario

        )

        return diario