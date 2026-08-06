from config import ARCHIVO_ZIP

from lectores.leer_zip import analizar_zip
from auditoria.inspector import inspeccionar_zip
from modelo.modelo_datos import ModeloDatos

resultado = analizar_zip(ARCHIVO_ZIP)

_, _, repo = inspeccionar_zip(
    ARCHIVO_ZIP,
    resultado["excel"]
)

modelo = ModeloDatos(repo).cargar()

print("\n====================")
print(type(modelo.cfdi))
print("====================")

print(dir(modelo.cfdi))