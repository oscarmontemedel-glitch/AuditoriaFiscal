from pathlib import Path
import zipfile


def analizar_zip(ruta_zip):

    ruta_zip = Path(ruta_zip)

    if not ruta_zip.exists():
        raise FileNotFoundError(f"No existe {ruta_zip}")

    resumen = {
        "excel": [],
        "csv": [],
        "pdf": [],
        "xml": [],
        "otros": []
    }

    with zipfile.ZipFile(ruta_zip, "r") as z:

        for archivo in z.namelist():

            nombre = archivo.lower()

            if nombre.endswith(".xlsx"):

                resumen["excel"].append(archivo)

            elif nombre.endswith(".csv"):

                resumen["csv"].append(archivo)

            elif nombre.endswith(".pdf"):

                resumen["pdf"].append(archivo)

            elif nombre.endswith(".xml"):

                resumen["xml"].append(archivo)

            else:

                resumen["otros"].append(archivo)

    return resumen