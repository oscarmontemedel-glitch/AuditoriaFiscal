"""
=========================================================
SAF v6.0
Carga Inteligente del Repositorio
=========================================================
"""

from lectores.leer_excel import leer_excel_zip

from auditoria.clasificador import clasificar_archivo

from repositorio.repositorio import RepositorioDatos


def cargar_repositorio(ruta_zip, lista_excel):

    repo = RepositorioDatos()

    print("\n==========================================")
    print("CONSTRUYENDO REPOSITORIO")
    print("==========================================")

    total_archivos = len(lista_excel)

    for indice, archivo in enumerate(lista_excel, start=1):

        print()

        print(f"[{indice}/{total_archivos}] {archivo}")

        tipo = clasificar_archivo(

            archivo

        )

        hojas = leer_excel_zip(

            ruta_zip,

            archivo

        )

        if not hojas:

            print("   ⚠ Archivo sin hojas válidas")

            continue

        contador = 0

        for hoja, info in hojas.items():

            repo.agregar(

                tipo,

                hoja,

                info["dataframe"]

            )

            contador += 1

        print(

            f"   ✓ {contador} hoja(s) agregadas"

        )

    print()

    print("==========================================")
    print("REPOSITORIO TERMINADO")
    print("==========================================")

    return repo