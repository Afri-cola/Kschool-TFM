#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


def tipo_cambio(root):
    
    """Esta función lee el fichero con la variable. 
    Se transforma la variable de dolares a euros aplicando el tipo de cambio anual.
    La variable se mide en millones de € y se redondea en dos decimales.
    
    """
    #Lectura y tratamiento del fichero
    df_export = pd.read_csv(root, header=0)
    df_export.rename(columns={'Country Name':'country', 'Indicator Name':'variables' }, inplace=True)
    df_export = df_export[df_export.country == 'México']
    df_export['country'] = df_export['country'].replace('México', 'MEXICO')
    df_export = df_export.drop(['Indicator Code', 'Country Code', 'country'], axis=1)
    
    #Lectura del fichero del cambio de dolar a Euro
    root = '/home/dsc/git/Kschool-TFM/Variables_economicas/Tipo de cambio- Dolar a Euro.csv'

    df = pd.read_csv(root)
    df.rename(columns={'Unnamed: 0' : 'variables'}, inplace=True)
    var_name = df_export.loc[152].iloc[0]
    df= df.replace({'Tipo de cambio': var_name})
    df.set_index('variables', inplace=True)
    
    #Aplicar el tipo de cambio en millones de euro
    df_export.set_index('variables', inplace=True)
    df_export = df_export.div(1000000)
    df_export = df_export.mul(df, axis=0)
    
    #Redondear
    df_export = df_export.round(2)
    df_export = df_export.transpose()
    
    return df_export


# In[3]:


def variable_porcentaje(root):
    "limpieza del fichero inicial de cada indicador económico. Base de datos del Banco Mundial"
    
    df = pd.read_csv(root, header=0)
    df.rename(columns={'Country Name':'country', 'Indicator Name':'variables' }, inplace=True)
    df = df[df.country == 'México']
    df['country'] = df['country'].replace('México', 'MEXICO')
    df = df.drop(['country', 'Country Code', 'Indicator Code'], axis=1)
    df = df.round(2)
    
    
    return df


# In[ ]:




