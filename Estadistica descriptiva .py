# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 07:23:14 2021

@author: DANIEL
"""

# Ejemplos de estadistica descriptiva con python

import numpy as np 
from scipy import stats 
import pandas as pd

np.random.seed(420) # Semilla no se repitan 

# datos aleatorios normalmente distribuidos
datos = np.random.randn(5, 4) 
datos


# media arítmetica
datos.mean() 
# Mismo resultado desde la funcion de numpy
np.mean(datos)
# media aritmetica de cada fila
datos.mean(axis=1) 
# media aritmetica de cada columna
datos.mean(axis=0) 


# mediana
np.median(datos) 
# mediana aritmetica de cada columna
np.median(datos, 0) 


#Desviación estandar o tipica
np.std(datos)
# Desviación típica de cada columna
np.std(datos, 0) 


#Varianza 
np.var(datos) 
#Varianza de cada columna 
np.var(datos,0) 


# moda moda de cada columna "Vectores"
stats.mode(datos)
#Ej moda 
datos2 = np.array([1, 2, 3, 6, 6, 1, 2, 4, 2, 2, 6, 6, 8, 10, 6])
stats.mode(datos2)


# Crea matriz de correlación.
np.corrcoef(datos) # datos
# calculando la correlación entre dos vectores.
np.corrcoef(datos[0], datos[1])



# calcula matriz de covarianza
np.cov(datos)
# covarianza de dos vectores
np.cov(datos[0], datos[1])



# Usando pandas para hacer un datframe 
dataframe = pd.DataFrame(datos, index=['a', 'b', 'c', 'd', 'e'], columns=['col1', 'col2', 'col3', 'col4'])
dataframe
# resumen estadistadistico con pandas
dataframe.describe()


# sumando las columnas
dataframe.sum()
# sumando filas
dataframe.sum(axis=1)


# media aritmetica de cada columna con pandas
dataframe.mean()
