
#%%
import pandas as pd
import os
import sys
from src import pair_soporte_etl_I as sp

#sys.path.append("../")

#%%

'''1 . Lectura de la Información:
- Leer los archivos CSV (ventas.csv, productos.csv, clientes.csv).

- Explorar los conjuntos de datos para comprender su estructura, columnas, tipos de datos, etc.'''

'''2. Transformación de Datos:

- Limpiar los datos: manejar valores nulos, eliminar duplicados si los hay, corregir errores tipográficos, etc.
- Realizar la integración de datos: unir los conjuntos de datos apropiados para obtener una tabla única que contenga información de ventas junto con detalles de productos y clientes.
- Aplicar transformaciones relevantes según sea necesario: por ejemplo, convertir tipos de datos, renombrar columnas, crear nuevas características derivadas, etc.

'''

#%%



def abrir_archivo(nombre):
    return pd.read_csv(nombre)
