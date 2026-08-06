"""
=========================================================
SAF v3.2
Motor RFC
=========================================================
"""

import pandas as pd

from auditoria.rfc import auditar_rfc


def ejecutar(repo):

    detalle = []

    resumen = []

    estadisticas = []

    for tipo in repo.tipos():

        hojas = repo.obtener(tipo)

        for hoja, df in hojas.items():

            resultado = auditar_rfc(

                df,

                archivo=tipo,

                hoja=hoja

            )

            if not resultado["Detalle"].empty:

                detalle.append(

                    resultado["Detalle"]

                )

            resumen.append(

                resultado["Resumen"]

            )

            estadisticas.append(

                resultado["Estadisticas"]

            )

    if detalle:

        detalle = pd.concat(

            detalle,

            ignore_index=True

        )

    else:

        detalle = pd.DataFrame()

    resumen = pd.concat(

        resumen,

        ignore_index=True

    )

    estadisticas = pd.concat(

        estadisticas,

        ignore_index=True

    )

    return {

        "Detalle": detalle,

        "Resumen": resumen,

        "Estadisticas": estadisticas

    }