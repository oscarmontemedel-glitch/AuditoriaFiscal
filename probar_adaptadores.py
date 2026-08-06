"""
=========================================================
SAF v9.0
Prueba de Integración de Adaptadores
=========================================================
"""

from config import ARCHIVO_ZIP

from lectores.leer_zip import analizar_zip
from auditoria.inspector import inspeccionar_zip

from adaptadores.cfdi import AdaptadorCFDI
from adaptadores.libro_mayor import AdaptadorLibroMayor
from adaptadores.auxiliar import AdaptadorAuxiliar
from adaptadores.dm_ingresos import AdaptadorDMIngresos
from adaptadores.iva import AdaptadorIVA
from adaptadores.balanza import AdaptadorBalanza
from adaptadores.diario import AdaptadorDiario


print("=" * 70)
print("SAF - PRUEBA DE ADAPTADORES")
print("=" * 70)

print()
print("Analizando expediente...")

resultado = analizar_zip(

    ARCHIVO_ZIP

)

print()
print("Construyendo repositorio...")

_, _, repo = inspeccionar_zip(

    ARCHIVO_ZIP,

    resultado["excel"]

)

print()
print("=" * 70)
print("PRUEBA DE ADAPTADORES")
print("=" * 70)


adaptadores = [

    ("CFDI", AdaptadorCFDI),

    ("Libro Mayor", AdaptadorLibroMayor),

    ("Auxiliar", AdaptadorAuxiliar),

    ("DM Ingresos", AdaptadorDMIngresos),

    ("IVA", AdaptadorIVA),

    ("Balanza", AdaptadorBalanza),

    ("Diario", AdaptadorDiario)

]


for nombre, clase in adaptadores:

    print()

    print(f"Probando {nombre}...")

    try:

        objeto = clase(

            repo

        )

        datos = objeto.obtener()

        if isinstance(datos, dict):

            print("✓ OK")

            print(

                f"  Tablas: {list(datos.keys())}"

            )

            for clave, df in datos.items():

                try:

                    print(

                        f"     {clave:<15} {len(df):>8} registros"

                    )

                except Exception:

                    print(

                        f"     {clave:<15} ERROR"

                    )

        else:

            print("✓ OK")

            print(

                f"  Registros: {len(datos)}"

            )

            print(

                f"  Columnas : {len(datos.columns)}"

            )

    except Exception as e:

        print()

        print("✗ ERROR")

        print(type(e).__name__)

        print(e)

print()
print("=" * 70)
print("PRUEBA TERMINADA")
print("=" * 70)