from config import ARCHIVO_ZIP

from lectores.leer_zip import analizar_zip

from auditoria.inspector import inspeccionar_zip

resultado = analizar_zip(ARCHIVO_ZIP)

inventario, perfiles, repo = inspeccionar_zip(

    ARCHIVO_ZIP,

    resultado["excel"]

)

hojas = repo.obtener_original(

    "LIBRO MAYOR DIKEN DE MEXICO MAY26.xlsx"

)

print(type(hojas))

print(hojas.keys())