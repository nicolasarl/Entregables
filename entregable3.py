# -*- coding: utf-8 -*-
"""
Created on Mon 14 00:32:27 2018

@author: Nicolás Adrián Rodríguez Linares
"""

import matplotlib.pyplot as plt
import numpy as np

#Datos del entregable

R = 4394.0#4394.0 #Resistencia en ohmios
Ti = 1. # Ventana de muestreo
Fs = 44100. # Frecuencia de muestreo: muestras/s
Ts = 1/Fs # Periodo de muestreo
f0 = (1/Ti);# Frecuencia de la señal, dependiente ventana temporal
w0 = (np.pi*2)*f0
t = np.arange(0,Ti,Ts) # Vector de tiempos
muestras = int(Fs*Ti) # Número de muestras

#Apartado A: Sintetizamos una señal
y =np.cos(2*np.pi*f0*t)+1j*np.sin(2*np.pi*f0*t)#Puede ser voltaje o intensidad

n = len(y) # longitud vector señal

fig,ax = plt.subplots(2,1)#Representamos la señal sintetizada
ax[0].plot(t,y.real)#Parte real
ax[0].set_ylabel('Amplitud [V] o  [A]')
ax[0].set_title('Señal sintetizada, parte real')
ax[1].plot(t,y.imag)#Parte imaginaria
ax[1].set_xlabel('Tiempo [s]')# Señal temporal
ax[1].set_ylabel('Amplitud [V] o [A]')
ax[1].set_title('Señal sintetizada, parte imaginaria')
plt.show()  

frq = np.zeros(n)# calculamos el vector que almacena las frecuencias
for i in range(int(len(frq)/2)):
    frq[i] = i*f0
    frq[-i] = -i*f0
#Apartado B: Cálculo coefcientes con FFT    
Y = np.fft.fft(y)/n # cálculo de los coeficientes de fourier normalizados (0-1)
Y = Y[range(n)]

plt.plot(frq,abs(Y),'g') # Espectro frecuencias
plt.xlabel(u'Frecuencia [Hz]')
plt.ylabel('|Fn|')
plt.title(u'Coeficientes de Fourier vs Frecuencia')
plt.show()
#Apartado C: Espectro de potencias
Pv = np.zeros(n)   
Pi = np.zeros(n)
for j in range(muestras): #Suponiendo que es un voltaje
    Pv[j] = ((abs(Y[j])*abs(Y[j]))/R)
for k in range(muestras): #Suponiendo que es un intensidad
    Pi[k] = ((abs(Y[k])*abs(Y[k]))*R)
#Representación Espectro de Potencias para ambos casos: Señal de tensión y de voltaje    
fig1, ax1 = plt.subplots(2, 1)
ax1[0].plot(frq,Pv,'m') # Espectro frecuencias
ax1[0].set_ylabel('Potencia [W]')
ax1[0].set_title('Espectro de potencias con la señal como V')
ax1[1].plot(frq,Pi,'m') # Espectro frecuencias
ax1[1].set_xlabel('Frecuencia [Hz]')
ax1[1].set_ylabel('Potencia [W]')
ax1[1].set_title('Espectro de potencias con la señal como I')
plt.show()



