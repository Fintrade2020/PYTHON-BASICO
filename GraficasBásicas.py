# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 10:05:38 2021

@author: DANIEL
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#Definimos una lista con paises como string
paises = ['MEdellin', 'Neiva', 'Guajira', 'Bogotá', 'Meta']
#Definimos una lista con ventas como entero
ventas = [24, 32, 36, 20, 28]
 

#Le decimos que vamos a graficar dos ejes  
fig, ax = plt.subplots()
#Colocamos una etiqueta en el eje Y
ax.set_ylabel('Ventas')
#Colocamos una etiqueta en el eje X
ax.set_title('Cantidad de Ventas por Pais')
#Creamos la grafica de barras utilizando 'paises' como eje X y 'ventas' como eje y.
plt.bar(paises, ventas)
plt.savefig('barras_simple.png') # Oiga recuerde que que es un diagrama de barras 
#Finalmente mostramos la grafica con el metodo show()
plt.show()




##Grafica de barras traspuesta 

lenguajes = ['Inglé', 'Español', 'Frances', 'Mandarin', 'Italiano', 'Ruso']
#Obtenemos una lista con las posiciones de cada lenguaje, ejemplo 0, 1, 2, 3.....
y_pos = np.arange(len(lenguajes))
 
#Ahora obtenemos la cantidad de usos de cada lenguaje
cantidad_usos = [10,7,6,3,2,1]
 
#Creamos la grafica pasando los valores en el eje X, Y, donde X = cantidad_usos y Y = lenguajes
plt.barh(y_pos, cantidad_usos, align='center') #align Centrado 
#Añadimos la etiqueta de nombre de cada lenguaje en su posicion correcta
plt.yticks(y_pos, lenguajes)
#añadimos una etiqueta en el eje X
plt.xlabel('Usuarios')
#Y una etiqueta superior
plt.title('Lenguajes Mas Usados En El Año')
plt.savefig('barras_horizontal.png')
plt.show()


## Grafica de lineas 

#generamos 100 numero de 0 a 2
x = np.linspace(0, 2, 100)
#Generamos una grafica lineal para una recta en X
plt.plot(x, x, label='linear')
#Generamos otra grafica lineal para una X cuadratica
plt.plot(x, x**2, label='quadratic')
#Generamos una grafica lineas para una X Cubica
plt.plot(x, x**3, label='cubic')
#Agregamos las etiquetas y añadimos una leyenda.
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title("Grafica Simple")
plt.legend()
plt.savefig('grafica_lineal.png')
plt.show()



## Podemos graficar una función 
x = np.arange(0, 10, 0.2)
#Generamos valores en el eje Y de seno
y = np.sin(x) 
fig, ax = plt.subplots() # Ax significa que vamos a graficar uha matriz de ejes.
#Creamos la Grafica
ax.plot(x, y)
plt.savefig('grafica_lineal_seno.png')
plt.show()




## Grafica de Pie##

#Asignamos la variable 
medios_transporte = 'Vehiculos', 'Motocicletas', 'Bicicleta', 'Metro'
#Declaramos el tamaño de cada 'rebanada' y en sumatoria todos deben dar al 100%
sizes = [45, 30, 15, 10]
#En este punto señalamos que posicion debe 'resaltarse' y el valor, si se coloca 0, se omite
explode = (0.1, 0, 0, 0)  #Cual es la variable que queremos señaral 
 
fig1, ax1 = plt.subplots()
#Creamos el grafico, añadiendo los valores
ax1.pie(sizes, explode=explode, labels=medios_transporte,shadow=True, startangle=90)# cuadro 90 grados
#señalamos la forma, en este caso 'equal' es para dar forma circular
ax1.axis('equal')
plt.title("Principal Medio de Transporte")
plt.legend()
plt.savefig('grafica_pastel.png')
plt.show()
