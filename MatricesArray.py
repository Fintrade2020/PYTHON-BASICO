"""
Created on Wed Jan 20 02:50:27 2021

@author: DANIEL ESTEBAN CASTIBLANCO MALDONADO
"""

import numpy as np 

#Crear un vector de ceros 
np.zeros(4)

#Crear un array de ceros 4x5
np.zeros([4,5])

#Podemos crear un vector de unos
np.ones ([4])

#Podemos crear una matriz de unos
np.ones([4,5])

#Podremos calcular matrices de identidad 
# las matrices de identidad son matrices que tienen misma cantidad de filas y columnas con una diagonal de 1. 
np.eye (3)

# Se puede hacer arrays vector apartir de un rango de valores ej de 0 a 5
np.arange(6)

#Se puede generar un array de numeros negativos y posivos 
np.arange(-3,6)

#Podemos hacer un rango de 0 a 20 cada dos digitos
np.arange(0,21,2)


### Operaciones basicas con array

#Suma o Resta (Para sumar o restar dos matrices deben tener las mismas dimenciones) F y C 

C = np.array ([4,3,6,7])
A = np.array ([5,4,3,2])

A+C
A-C



#El # de columnas del primero debe ser iguaul al # filas del segundo 
#Multiplicación 
C*A
#sSe puede multiplicar el array por 1 número.
A*5

#Dividir 
C/A
#Se puede dividir el arra entre por un número. 
A/2

# Se puede sacar la inversa de del array elevandolo a la -1
A ** -1. # debe colocar . como numero decimal 

#Un array elevado a otro array 
C**A
pow (C,A)
#Potencia con un número 
pow(A,3)


#### Array en dos dimenciones 

S = np.array ([[4,5,6],[6,8,5]]) 
T = np.array ([[6,0,1],[1,2,3]]) 

#Suma
S+T
#Multiplicación
T*S
#División 
T/S
#Potencia 
T**np.array([[1,2,3],[4,5,6]])


#Tare "construyanme 2 matrices 2x2 y operenlas"


##           Vectores 
vec = np.arange(0,60,5)
vec

#Si queremos tomar el primer numero 
vec [0]

#Si queremos tomar el 5to numero 
vec[4]

# Si queremos tomar el ultimo número 
vec[-1]
 
# Támbien podemos modificar valores "el primer valor sea un 420
vec[0]=420  



## Slicin ":" para tomar un rango de números de un inicio a un fin

# Solo : toma todo el array 
vec [:]

#Tomar desde el inicio hasta la 5ta posición 
vec [:5]

# Definir la posición de comienzo y de fin 
vec[1:4] # Slicin excluye la ultima posición 
 


##           Arrays de 2 dimensiones 

M = np.array([[1,2,3],[4,5,6],[7,8,9]])
M

# Si quiero tomar la primera fila 
M [0]
#Si quiero seleccionar la 1ra fiña de la 1ra columna 
M[0][0]
#Si quiero seleccionar la ultima fila de la ultima columna
M[-1][-1]

## Slicin ":"
#Todos los elementos 
M[:,:]
#Solo queremos las dos primeras filas 
M[:2,:]
#Solo la primera columna 
M[:,0:1]


###        Arrays Transpuestas
##Las filas se vuelven columnas y las columnas filas 

#MAtriz Transúeste 
M.T
#Volver a transponer la matriz 
M.T.T


#Tarea Creen una matris de 2 dimensiones, cambienle un dato de la matriz y hagala transpuesta. 