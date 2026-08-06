"""
=========================================================
SAF v7.0
Inspector Inteligente
=========================================================
"""

import pandas as pd

from lectores.leer_excel import leer_excel_zip
from auditoria.clasificador import clasificar_archivo
from auditoria.perfilador import perfilar_dataframe
from repositorio.repositorio import RepositorioDatos


def inspeccionar_zip(ruta_zip, lista_excel):

    resumen = []

    perfiles = []

    repo = RepositorioDatos()

    total = len(lista_excel)

    print("\n==========================================")
    print("INSPECCIONANDO EXPEDIENTE")
    print("==========================================")

    for indice, archivo in enumerate(lista_excel, start=1):

        print(f"\n[{indice}/{total}] {archivo}")

        tipo = clasificar_archivo(

            archivo

        )

        hojas = leer_excel_zip(

            ruta_zip,

            archivo

        )

        if not hojas:

            continue

        # ==========================================
        # Guardar el Excel ORIGINAL completo
        # ==========================================

        originales = {}

        for hoja, info in hojas.items():

            originales[hoja] = info["dataframe"].copy()

        repo.agregar_original(

            archivo,

            originales

        )

        # ==========================================
        # Procesar hojas
        # ==========================================

        for hoja, info in hojas.items():

            df = info["dataframe"]

            repo.agregar(

                tipo,

                hoja,

                df

            )

            resumen.append({

                "Archivo": archivo,

                "Tipo": tipo,

                "Hoja": hoja,

                "Encabezado": info["encabezado"],

                "Filas": len(df),

                "Columnas": len(df.columns)

            })

            perfil = perfilar_dataframe(df)

            perfil.insert(

                0,

                "Hoja",

                hoja

            )

            perfil.insert(

                0,

                "Archivo",

                archivo

            )

            perfiles.append(

                perfil

            )

    if perfiles:

        perfiles = pd.concat(

            perfiles,

            ignore_index=True

        )

    else:

        perfiles = pd.DataFrame()

    print("\n==========================================")
    print("INSPECCIÓN TERMINADA")
    print("==========================================")

    return (

        pd.DataFrame(resumen),

        perfiles,

        repo

    )