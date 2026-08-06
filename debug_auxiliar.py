from lectores.leer_zip import analizar_zip
from auditoria.inspector import inspeccionar_zip
from config import ARCHIVO_ZIP

resultado = analizar_zip(ARCHIVO_ZIP)

inventario, perfiles, repo = inspeccionar_zip(

    ARCHIVO_ZIP,

    resultado["excel"]

)

# AQUÍ ESTÁ EL CAMBIO
hojas = repo.dataframes["Aux_May26.xlsx"]

for nombre, df in hojas.items():

    print("=" * 80)
    print(nombre)
    print("=" * 80)

    print(df.head(50).to_string())