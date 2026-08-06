"""
=========================================================
SAF v3.2
Auditor RFC Profesional
=========================================================
"""

import re
import pandas as pd


COLUMNAS_RFC = [
    "RFC",
    "RFC_EMISOR",
    "RFC_RECEPTOR",
    "RFC_CLIENTE",
    "RFC_PROVEEDOR"
]


PATRON_RFC = re.compile(
    r"^[A-ZÑ&]{3,4}[0-9]{6}[A-Z0-9]{3}$"
)


def auditar_rfc(df, archivo="", hoja=""):

    detalle = []

    revisados = 0
    vacios = 0
    longitud = 0
    formato = 0
    espacios = 0
    duplicados = 0

    columnas = [
        c
        for c in df.columns
        if c in COLUMNAS_RFC
    ]

    if len(columnas) == 0:

        return {

            "Detalle": pd.DataFrame(),

            "Resumen": pd.DataFrame(),

            "Estadisticas": pd.DataFrame()

        }

    for columna in columnas:

        serie = (
            df[columna]
            .fillna("")
            .astype(str)
        )

        serie_duplicada = serie.str.strip().str.upper()

        duplicados_mask = serie_duplicada[
            serie_duplicada != ""
        ].duplicated(
            keep=False
        )

        for indice, valor in serie.items():

            revisados += 1

            original = valor

            rfc = valor.strip().upper()

            error = None

            if rfc == "":

                vacios += 1

                error = "RFC vacío"

            elif len(rfc) not in (12, 13):

                longitud += 1

                error = "Longitud incorrecta"

            elif original != original.strip():

                espacios += 1

                error = "Espacios al inicio/final"

            elif not PATRON_RFC.match(rfc):

                formato += 1

                error = "Formato SAT inválido"

            elif indice in duplicados_mask.index and duplicados_mask.loc[indice]:

                duplicados += 1

                error = "RFC duplicado"

            if error:

                detalle.append({

                    "Archivo": archivo,

                    "Hoja": hoja,

                    "Fila": indice + 2,

                    "Columna": columna,

                    "RFC": rfc,

                    "Error": error

                })

    detalle_df = pd.DataFrame(detalle)

    resumen_df = pd.DataFrame({

        "TipoError": [

            "RFC vacío",

            "Longitud incorrecta",

            "Formato SAT inválido",

            "Espacios",

            "Duplicados"

        ],

        "Cantidad": [

            vacios,

            longitud,

            formato,

            espacios,

            duplicados

        ]

    })

    estadisticas_df = pd.DataFrame({

        "Concepto": [

            "RFC revisados",

            "RFC con error",

            "RFC correctos"

        ],

        "Valor": [

            revisados,

            len(detalle_df),

            revisados - len(detalle_df)

        ]

    })

    return {

        "Detalle": detalle_df,

        "Resumen": resumen_df,

        "Estadisticas": estadisticas_df

    }