"""
=========================================================
SAF v9.0
Ejecutor del Motor de Reglas
=========================================================
"""

from modelo.dataframe_global import construir_dataframe_global
from modelo.movimientos import construir_movimientos

from motor.motor_reglas import MotorReglas


def ejecutar(repo):

    print()
    print("=" * 60)
    print("EJECUTANDO MOTOR DE REGLAS")
    print("=" * 60)

    # =====================================================
    # DATAFRAME GLOBAL
    # =====================================================

    print()
    print("Construyendo DataFrame Global...")

    global_df = construir_dataframe_global(

        repo

    )

    print(f"Registros : {len(global_df)}")
    print(f"Columnas  : {len(global_df.columns)}")

    # =====================================================
    # MOVIMIENTOS
    # =====================================================

    print()
    print("Construyendo modelo de movimientos...")

    movimientos = construir_movimientos(

        global_df

    )

    print(f"Movimientos : {len(movimientos)}")

    # =====================================================
    # MOTOR
    # =====================================================

    print()
    print("Ejecutando reglas...")

    motor = MotorReglas()

    resultado = motor.ejecutar(

        movimientos

    )

    print()
    print("=" * 60)
    print("MOTOR TERMINADO")
    print("=" * 60)

    return resultado