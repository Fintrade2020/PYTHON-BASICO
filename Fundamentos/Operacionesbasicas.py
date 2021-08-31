# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 02:50:27 2021

@author: DANIEL
"""
import pandas as pd
import numpy as np
from pandas_datareader import data
import matplotlib as plt
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.arima_model import ARIMA
import math
import statistics
from pylab import *
import seaborn as sns

#Operador suma  
3+2
#Operador resta
4-7
#Numero negativo 
-7
#Multiplicación 
2*6
# Operador de potencia
2**6
# Operador de división 
3.5 / 2
# División entera, que el resultado solo me de la parte entera 
3.5 // 2
#Se puede dividir entre dos entero y que den decimal 3.0/2
3/2


#Otra forma de operar una potencia
pow (2,6)
#Logaritmo natural (base 1)
math.log(6)
#logaritmo en base 10 
math.log10(5)
#Logarimo con una base y x defiido. 
math.log(25, 5)
#Raiz cuadrada 
math.sqrt (52)
#Raiz cubica 
8**(1/3)
# Euler 
math.exp(6)

# Se pueden definir variables
x = 5 
y = 8 

# se pueden sumar variables 
x+y

#Ejemplo para la clase 
D = (math.log(6*math.exp(4+8)))**2
# D = Out[870]: 190.2126292570417

# Ejemplo para la clase 
A= (math.sqrt(326/2))*4
# = Out[872]: 51.068581339214816

N = math.exp(D/pow(5,2))
# N=Out[876]: 2015.2633694505614

D+A*N #Out[877]: 103106.85393198316
