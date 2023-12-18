#%%
from src import soporte_creacion_BBDD as query
from src import BBDD_soporte as bbdd
import pandas as pd
#%%
#Creamos el Schema
bbdd.creacion_BBDD_tablas(query.query_creacion_bbdd,'AlumnaAdalab')
# %%
#Creamos la tabla
bbdd.creacion_BBDD_tablas(query.query_creacion_tabla_ventas,'AlumnaAdalab','pair_ETL')
# %%
#Cargamos el archivo
ventas=pd.read_csv('c1_ventas.csv')
# %%
#Pasar el DF a tuplas (usamos set en lugar de tuple por si hay filas duplicadas)
datos_tabla_ventas=list(set(zip(ventas['ID_Cliente'].values,ventas['ID_Producto'].values,ventas['Fecha_Venta'].values,ventas['Cantidad'].values,ventas['Total'].values)))
# %%
#Pasamos los datos a float porque no nos dejaba meterlo en el MySQL
datos_tabla_ventas_def=bbdd.convertir_floats(datos_tabla_ventas)
# %%
bbdd.insertar_datos(query.query_insertar_ventas,'AlumnaAdalab','pair_ETL',datos_tabla_ventas_def)
# %%
