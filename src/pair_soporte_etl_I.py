
#%%
import pandas as pd

#%%
def abrir_archivo(nombre):
    return pd.read_csv(nombre, sep= ",")


# %%

def nombres_columnas(nombre):
    nuevas_columnas = {columna: columna.lower() for columna in nombre.columns}
    return nombre.rename(columns=nuevas_columnas, inplace= True)


def productos(csv):
    columnas_prov = ["1","2", "3", "4", "5" , "6", "7",  "8",  "9",  "10"]
    pr2=pd.read_csv(csv, names = columnas_prov)
    pr2 = pr2.fillna(' ')
    pr2['6'] = pr2['6'] + pr2['7'] + pr2['8'] + pr2['9'] + pr2['10'] 
    pr2.drop(['7', '8', '9', '10'], axis = 1, inplace = True)
    # Crear un diccionario de mapeo para los nuevos nombres de las columnas
    nuevos_nombres = {'1': 'id', '2': 'nombre_producto', '3':'categoría', '4':'precio', 	'5' :'origen', '6':	'descripción'}
    # Utilizar el método rename con el diccionario de mapeo
    pr2 = pr2.rename(columns=nuevos_nombres)
    pr2.drop(0,axis=0, inplace=True)
    return pr2

def nulos_clientes(df, columnas):
    for columna in columnas:
        if columna == "country":
            df[columna] = df[columna].fillna("Spain")
        else: df[columna] = df[columna].fillna("Unknown")
    return df

'''def unir_tablas(df1, df2, columna):
    tabla = df1.join(df2.set_index( [ 'id' ], verify_integrity=True ),
               on=[ columna ], how='outer' )'''

'''def unir_tablas(df1, df2, columna):
    tabla = df1.join(df2.set_index('id'), on=columna, how='inner')
    tabla.drop('id', axis=1, inplace=True)'''

def unir_tablas(df1, df2, columna):
    tabla = df1.merge(right=df2, left_on= columna, right_on = "id",  how = "outer")
    return tabla

def nulos_tabla(df, lista, texto):
    df[lista]= df[lista].fillna(texto)
    return df

