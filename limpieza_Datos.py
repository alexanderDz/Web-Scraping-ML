import pandas as pd
import re

df = pd.read_csv('datos.csv')

#%% Patrón de expresión regular para buscar la palabra "Bogotá" seguida de cualquier cosa
pattern = re.compile(r'.*Bogotá')

# Aplicar el patrón a todas las filas en la columna 'Ubicacion' y extraer la ubicación modificada
new_locations = df['Ubicacion'].str.replace(pattern, 'Bogotá', regex=True)

# Reemplazar los valores originales en la columna 'Ubicacion' por los valores modificados
df['Ubicacion'] = new_locations
#%%
# Reemplazar 'Bogotá D.C.' por 'Bogotá' en la columna 'Ubicacion'
df['Ubicacion'] = df['Ubicacion'].str.replace('Bogotá D.C..', 'Bogota')
#%% 
pattern = re.compile(r', [^.]+')
# Aplicar el patrón a todas las filas en la columna 'Ubicacion' y extraer la ubicación modificada
new_locations = df['Ubicacion'].str.replace(pattern, '', regex=True)

# Reemplazar los valores originales en la columna 'Ubicacion' por los valores modificados
df['Ubicacion'] = new_locations
#%%
# Eliminar el punto al final de las filas que lo tienen en la columna 'Ubicacion'
df['Ubicacion'] = df['Ubicacion'].str.rstrip('.')
#%%
# Eliminar los puntos y convertir la columna de precios a enteros
df['Precio'] = df['Precio'].str.replace('.', '').astype(int)
#%%
df['Rating'] = df['Rating'].astype(float)
#%%
# Eliminar los puntos y convertir la columna de precios a enteros
df['Ventas 60 dias'] = df['Ventas 60 dias'].str.replace('mil', '000')
df['Ventas 60 dias'] = df['Ventas 60 dias'].str.replace('+', '').astype(int)
#%%
# Eliminar los puntos y convertir la columna de precios a enteros
df['Reviews'] = df['Reviews'].str.replace('calificaciones', '')
df['Reviews'] = df['Reviews'].str.replace('calificación', '')
df['Reviews'] = df['Reviews'].astype(int)
#%% eliminar NaN
df = df.dropna()
#eliminar precios menores a 100k
df = df.loc[df['Precio'] >= 100000]
#eliminar respuestos y demases
df = df[~df['Titulo'].str.contains('repuestos|partes|accesorios|Repuestos|Partes|Accesorios|Repuesto')]
#%%
# Obtener una lista de los nombres de ciudades únicos en la columna 'Ciudad'
city_list = df['Ubicacion'].unique().tolist()
# Crear un diccionario de mapeo de ciudades a números
city_map = {city: i+1 for i, city in enumerate(city_list)}

df['Ciudad_num'] = df['Ubicacion'].replace(city_map)

#%% para conteo de palabras
df['num_palabras'] = df['Titulo'].apply(lambda x: len(str(x).split()))
#%% Guardar DataFrame como archivo CSV
df.to_csv('datos_limpios.csv', index=False)