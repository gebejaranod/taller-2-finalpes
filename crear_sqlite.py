"""Copia datos/churn.csv, tal como viene, a la tabla churn de datos/churn.sqlite para explorarla en Metabase.

Uso, desde la raíz del repositorio:  python crear_sqlite.py
"""
import sqlite3

import pandas as pd

datos = pd.read_csv("datos/churn.csv")

conexion = sqlite3.connect("datos/churn.sqlite")
datos.to_sql("churn", conexion, if_exists="replace", index=False)
conexion.close()

print(f"{len(datos)} registros guardados en la tabla churn de datos/churn.sqlite")
