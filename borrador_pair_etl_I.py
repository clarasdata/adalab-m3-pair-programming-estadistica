
#%%
import pandas as pd
import os
import sys
from src import pair_soporte_etl_I as sp

#sys.path.append("../") -> mejor desconectado no tocar!!
#os.getcwd()  -> para saber en que ruta estamos
#os.chdir("ruta donde queremos trabajar")  -> para cambiar la ruta
#pd.read_csv("productos.csv", on_bad_lines = 'skip') 
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
ventas = sp.abrir_archivo("c1_ventas.csv") 
clientes = sp.abrir_archivo("clientes.csv") 


# %%
#productos = sp.abrir_archivo("productos.csv") 
# %%

sp.nombres_columnas(ventas)
sp.nombres_columnas(clientes)
# %%
clientes
# %%

pr=pd.read_csv("productos.csv", on_bad_lines = 'skip')


# %%

columnas_prov = ["1","2", "3", "4", "5" , "6", "7",  "8",  "9",  "10"]
pr2=pd.read_csv("productos.csv", names = columnas_prov)
# %%
pr2 = pr2.fillna(' ')



# %%
pr2['6'] = pr2['6'] + pr2['7'] + pr2['8'] + pr2['9'] + pr2['10'] 




# %%
pr2
# %%
pr2.drop(['7', '8', '9', '10'], axis = 1, inplace = True)
# %%
pr2
# %%



# Crear un diccionario de mapeo para los nuevos nombres de las columnas
nuevos_nombres = {'1': 'id', '2': 'first_name', '3':'last_name', '6':'email', 	'7' :'gender', '8':	'city', '9':	'country'}

# Utilizar el método rename con el diccionario de mapeo
pr = pr.rename(columns=nuevos_nombres)
# %%
pr
# %%
