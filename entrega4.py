# -*- coding: utf-8 -*-
"""
Created on Thu May 17 20:41:39 2018

@author: Nicolás Adrián Rodríguez Linares
"""

import numpy as np
import matplotlib.pyplot as plt

#Parámetros del circuito:

R = 8.2 #Resistencia en Ohmios
L = 1e-3 #Inductancia en Henrios
C =  10e-6#Capacidad en Faradios

fi = 50 #Frecuencia angular inicial en rad/s
ff =  1e6 #Frecuencia angular final en rad/se
f = np.arange(fi,ff,150)#Tomaremos un punto cada 150 HZ para el Bode
gain = np.zeros(len(f))
phase = np.zeros(len(f))

for i in range(len(f)):
    s = 1j*np.pi*2*f[i]
    tf = (s*L+R)/((s*L+R)+R*(1+s*s*L*C))#Función de transferencia
    gain[i] = abs(tf)#Ganancia [V/V]
    phase[i] = ((np.arctan2(tf.imag,tf.real)*360)/(2*np.pi))#Fase en grados 
   
fig,ax = plt.subplots(2,1)
ax[0].plot(f,20*np.log10(gain),'b')
ax[0].set_ylabel('Ganancia [dB]')
ax[0].set_title('Diagrama magnitud')
ax[0].set_xscale('log')
ax[1].plot(f,phase,'b')
ax[1].set_xlabel('Frecuencia [Hz]')
ax[1].set_ylabel('Fase [º]')
ax[1].set_xscale('log')
ax[1].set_title('Diagrama fase')
plt.show()