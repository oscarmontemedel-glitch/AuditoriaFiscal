"""
=========================================================
SAF v6.3
Auditor Profesional RFC
=========================================================
"""

import re
import pandas as pd


COLUMNAS_RFC = [

    "RFC",

    "RFC EMISOR",

    "RFC RECEPTOR",

    "RFCCLIENTE",

    "RFC_PROVEEDOR"

]


PATRON_FISICA = re.compile(

    r"^[A-ZÑ&]{4}[0-9]{6}[A-Z0-9]{3}$"

)

PATRON_MORAL = re.compile(

    r"^[A-ZÑ&]{3}[0-9]{6}[A-Z0-9]{3}$"

)


RFC_GENERICOS = [

    "XAXX010101000",

    "XEXX010101000"

]


class AuditorRFC:

    def ejecutar(self, df):

        resultados = []

        columnas = [

            c

            for c in df.columns

            if str(c).upper() in COLUMNAS_RFC

        ]

        if not columnas:

            return pd.DataFrame()

        for columna in columnas:

            for fila, valor in df[columna].items():

                rfc = ""

                if pd.notna(valor):

                    rfc = str(valor).strip().upper()

                error = ""

                if rfc == "":

                    error = "RFC VACÍO"

                elif len(rfc) not in (12, 13):

                    error = "LONGITUD INCORRECTA"

                elif rfc in RFC_GENERICOS:

                    error = "RFC GENÉRICO"

                elif len(rfc) == 12:

                    if not PATRON_MORAL.match(rfc):

                        error = "RFC MORAL INVÁLIDO"

                elif len(rfc) == 13:

                    if not PATRON_FISICA.match(rfc):

                        error = "RFC FÍSICA INVÁLIDO"

                if error:

                    resultados.append({

                        "Fila": fila,

                        "Columna": columna,

                        "RFC": rfc,

                        "Hallazgo": error

                    })

        salida = pd.DataFrame(resultados)

        if salida.empty:

            return salida

        duplicados = (

            salida

            .groupby("RFC")

            .size()

            .reset_index(name="Ocurrencias")

        )

        salida = salida.merge(

            duplicados,

            on="RFC",

            how="left"

        )

        return salida