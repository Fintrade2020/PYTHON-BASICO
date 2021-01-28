# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 12:27:45 2021

@author: DANIEL
"""
import pandas as pd
import numpy as np
from pandas_datareader import data
import matplotlib 
import matplotlib as plt
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.arima_model import ARIMA
import math
import statistics
from pylab import *
import seaborn as sns


#Nombramos los datos en un conjunto

tickers = ["CVX","DJD","FENY","IGE","IXC","IYE","JHME","NANR","VDE","XLE"]
start_date = '2018-01-06'
end_date = '2021-01-06'

#Llamamos los datos
panel_data = data.DataReader(tickers, 'yahoo', start_date, end_date)
panel_data.head(9)


##Lo convertimos en una serie de tiempo para que coja los datos diarios de cada semana.
all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')


##Sacamos los precios de cierre
close = panel_data['Close']
close = close.reindex(all_weekdays)
close = close.fillna(method='ffill') #Encontrar NAN error 
close = close.iloc[1:,]#Resolver error
close.describe() # Describe los precios de cierre por activo.



#Obstener los retornos de solo CVX
cvx = close.loc[:, 'CVX']


##Graficarla 

# Calcule las medias móviles de 20 y 100 días de los precios de cierre (Promedio )
short_rolling_cvx = cvx.rolling(window=20).mean()
long_rolling_cvx = cvx.rolling(window=100).mean()

# Plot everything by leveraging the very powerful matplotlib package
fig, ax = plt.subplots(figsize=(16,9))

ax.plot(cvx.index, cvx, label='CVX')
ax.plot(short_rolling_cvx.index, short_rolling_cvx, label='20 days rolling')
ax.plot(long_rolling_cvx.index, long_rolling_cvx, label='100 days rolling')

ax.set_xlabel('Date')
ax.set_ylabel('Adjusted closing price ($)')
ax.legend()


#Vamos a sacar los retornos de  CVX con sus ETF´s
returns=close.pct_change()
returns=returns.iloc[1:,]
returns.head(5)


#Sacamos el retorno de solo cvx
chevron_R = returns['CVX']

#ARIMA
model = ARIMA(chevron_R, order=(1,0,0))
model_fit = model.fit(disp=0)
print(model_fit.summary())
model_fit.params
Ar1 = model_fit.params[1]
Int1 = model_fit.params[0]

