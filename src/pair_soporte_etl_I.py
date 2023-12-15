
#%%
import pandas as pd

#%%
def abrir_archivo(nombre):
    return pd.read_csv(nombre, sep= ",")


# %%

def nombres_columnas(nombre):
    nuevas_columnas = {columna: columna.lower() for columna in nombre.columns}
    return nombre.rename(columns=nuevas_columnas, inplace= True)



