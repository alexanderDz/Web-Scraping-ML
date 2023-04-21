# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 13:14:28 2023

@author: User
"""
#%%
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import numpy as np
#%%
df1 = pd.read_csv('info_portatiles_1.csv')
df2 = pd.read_csv('info_portatiles_2.csv')
df3 = pd.read_csv('info_portatiles_3.csv')
#%% Elimina las listas vacias
df1['Comentarios'].replace('[]', np.nan, inplace=True)
df2['Comentarios'].replace('[]', np.nan, inplace=True)
df3['Comentarios'].replace('[]', np.nan, inplace=True)
#%%
# Realiza un left join para unir df1 y df2 basándose en la columna 'Link'
merged_df = pd.merge(df1, df2, on='Link', how='left')

# Reemplaza los valores faltantes en df1 con los valores correspondientes en df2
merged_df['Titulo_x'].fillna(merged_df['Titulo_y'], inplace=True)
merged_df['Precio_x'].fillna(merged_df['Precio_y'], inplace=True)
merged_df['Ubicacion_x'].fillna(merged_df['Ubicacion_y'], inplace=True)
merged_df['Ventas 60 dias_x'].fillna(merged_df['Ventas 60 dias_y'], inplace=True)
merged_df['Reviews_x'].fillna(merged_df['Reviews_y'], inplace=True)
merged_df['Rating_x'].fillna(merged_df['Rating_y'], inplace=True)
merged_df['Comentarios_x'].fillna(merged_df['Comentarios_y'], inplace=True)

# Elimina las columnas duplicadas (con el sufijo _x o _y)
merged_df.drop(merged_df.filter(regex='_y$').columns.tolist(), axis=1, inplace=True)
#%%
# Realiza un left join para unir df1 y df2 basándose en la columna 'Link'
merged_df = pd.merge(df1, df3, on='Link', how='left')

# Reemplaza los valores faltantes en df1 con los valores correspondientes en df2
merged_df['Titulo_x'].fillna(merged_df['Titulo_y'], inplace=True)
merged_df['Precio_x'].fillna(merged_df['Precio_y'], inplace=True)
merged_df['Ubicacion_x'].fillna(merged_df['Ubicacion_y'], inplace=True)
merged_df['Ventas 60 dias_x'].fillna(merged_df['Ventas 60 dias_y'], inplace=True)
merged_df['Reviews_x'].fillna(merged_df['Reviews_y'], inplace=True)
merged_df['Rating_x'].fillna(merged_df['Rating_y'], inplace=True)
merged_df['Comentarios_x'].fillna(merged_df['Comentarios_y'], inplace=True)

# Elimina las columnas duplicadas (con el sufijo _x o _y)
merged_df.drop(merged_df.filter(regex='_y$').columns.tolist(), axis=1, inplace=True)

#%%
mask = merged_df['Comentarios_x'].isna()

links_restantes = merged_df[mask]['Link'].tolist()
#%%
datos = merged_df.dropna(how='any', inplace=True)  
#%%
merged_df = merged_df.rename(columns={'Titulo_x': 'Titulo','Precio_x': 'Precio','Ubicacion_x': 'Ubicacion','Ventas 60 dias_x': 'Ventas 60 dias','Reviews_x': 'Reviews','Rating_x': 'Rating','Comentarios_x': 'Comentarios'})        
#%%
merged_df.to_csv('datos.csv', index=False)    
