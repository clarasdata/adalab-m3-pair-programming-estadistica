
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
productos = sp.productos("productos.csv") 
# %%

sp.nombres_columnas(ventas)
sp.nombres_columnas(clientes)
# %%
clientes_sin_nulos = sp.nulos_clientes(clientes, clientes.columns.tolist())
# %%
vc = sp.unir_tablas(ventas, clientes, "id_cliente")
tabla = sp.unir_tablas(vc, productos, "id_producto")

# %%
lista_clientes_sin_compra = tabla.columns.tolist()[:5]
lista_compra_sin_cliente =  tabla.columns.tolist()[5:13]
lista_compra_sin_producto =  tabla.columns.tolist()[13:]
#queremos sobreescrivir la tabla actual con los cambios:
tabla = sp.nulos_tabla(tabla,lista_clientes_sin_compra, ("clientes sin registrar") )
tabla = sp.nulos_tabla(tabla,lista_compra_sin_cliente, ("cliente sin compra este año") )
tabla = sp.nulos_tabla(tabla,lista_compra_sin_producto , ("sin producto registrado"))

# %%
tabla.drop(['id_x', 'id_y'], axis = 1, inplace=True)
# %%
