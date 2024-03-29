# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 05:26:08 2021

@author: DANIEL
"""

### Caminatas aleatorias ###
import numpy as np
from matplotlib import pyplot as plt

S0 = 100 #initial stock price
K = 100 #strike price 
r = 0.05 #risk-free interest rate
sigma = 0.50 #volatility in market
T = 1 #time in years
N = 100 #number of steps within each simulation
deltat = T/N #time step
i = 1000 #number of simulations
#discount_factor = np.exp(-r*T) #discount factor

S = np.zeros([i,N])

n=range(0,N,1)


for y in range(0,i-1):
    S[y,0]=S0
    for x in range(0,N-1):
        S[y,x+1] = S[y,x]*(np.exp((r-(sigma**2)/2)*deltat + sigma*deltat*np.random.normal(0,1)))
    plt.plot(n,S[y])

plt.title('Simulations %d Steps %d Sigma %.2f r %.2f S0 %.2f' % (i, N, sigma, r, S0))
plt.xlabel('Steps')
plt.ylabel('Stock Price')
plt.show()
