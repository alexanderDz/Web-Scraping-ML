import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from unidecode import unidecode
import re
import matplotlib.pyplot as plt
#%%
df = pd.read_csv('datos_limpios_1.csv')
#%%
# Limpiar la columna de nombres
df["Titulo"] = df["Titulo"].apply(lambda x: unidecode(str(x))) # eliminar tildes
df["Titulo"] = df["Titulo"].apply(lambda x: re.sub(r'[^\w\s]', '', x)) # eliminar caracteres especiales
df["Titulo"] = df["Titulo"].apply(lambda x: x.lower()) # convertir a minúsculas
#%%
# Crear una lista de todas las palabras en la columna "nombre"
all_words = []
for nombre in df["Titulo"]:
    words = word_tokenize(nombre.lower())
    all_words.extend(words)

# Crear una distribución de frecuencia de palabras
fdist = FreqDist(all_words)

# Mostrar las frecuencias de todas las palabras
fdist.tabulate()

#%%
import matplotlib.pyplot as plt

# Crear una figura y un eje
fig, ax = plt.subplots(figsize=(8, 6))

# Crear la gráfica de barras
fdist.plot(30, cumulative=False)

# Configurar el título y las etiquetas de los ejes
ax.set_title("Distribución de Frecuencia de Palabras")
ax.set_xlabel("Palabras")
ax.set_ylabel("Frecuencia")

# Mostrar la gráfica
plt.show()
