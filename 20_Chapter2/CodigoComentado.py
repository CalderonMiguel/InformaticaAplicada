# importacion de las librerias necesarias 
import numpy as np #Posee una coleccion de funciones matematicas 
import matplotlib.pyplot as plt #Permite generar los graficos en dos dimensiones a partir de listas o arrys
from scipy import signal #herramientas y algoritmos matematicos 
import math #Permite usar funciones matematicas definidas para estandar de C
  
#Funcion para convertir las frecuencias de borde 
def convertX(f_sample, f):
    w = []
  
    #Ciclo para la frecuencia de paso o de corte segun el uso de la funcion
    for i in range(len(f)):  #Ciclo que va desde 0 hasta el valor final del tamaño de f 
        b = 2*((f[i]/2) / (f_sample/2))  #division de la frecuencia de paso/corte entre la mitad de la del muestreo 
        w.append(b) #Genera un vector donde aparences los valores correspondientes de acuerdo a la operacion asiganada en b
  
    omega_mine = []
    #Ciclo para la frecuencia de muestreo 
    for i in range(len(w)):  #Ciclo que va desde 0 hasta el valor final del tamaño de w
        c = (2/Td)*np.tan(w[i]/2)
        omega_mine.append(c)
  
    return omega_mine




# Especificaciones del Filtro 
  
# Frecuencia de muestreo 
f_sample = 12000
  
# Frecuencia de paso de banda 
f_pass = [2100, 4500]
  
# Frecuencia de la banda de rechazo 
f_stop = [2700, 3900]
  
# Rizo de la banda de paso 
fs = 0.5
  
# Tiempo de muestreo
Td = 1
  
# Rizo de la banda de paso en dB
g_pass = 0.6
  
# atenuacion de la banda de rechazo  en dB
g_stop = 45

# Convercion a la frecuencia analogica programada
omega_p = convertX(f_sample, f_pass) #llamado de la funcion de borde con la frecuencia de muestreo y de paso
omega_s = convertX(f_sample, f_stop) #llamado de la funcion de borde con la frecuencia de muestreo y corte 
  
#Diseño de la señal con filtro butterword a traves de una funcion 
N, Wn = signal.buttord(omega_p, omega_s,
                       g_pass, g_stop,
                       analog=True)
  
  
#Impresion en terminal del orden del filtro y la frecuencia de corte 
#N contiene el orden del filtro 
print("Orden del filtro=", N)
  
# La variable wn contiene el valor de la frecuencia de corte 
print("Frecuencia de corte = {:} rad/s ".format(Wn))
  
#Conversion en el dominio Z (Transformada )
  
#b es el numerador del filtro y a el denominador 
b, a = signal.butter(N, Wn, 'bandpass', True) #Filtro pasa banda buterwort
z, p = signal.bilinear(b, a, fs) 
  
#w es la frecuencia en el dominio z y h es la magnitud en el dominio  z
w, h = signal.freqz(z, p, 512)

# Respuesta en magnitud 
plt.semilogx(w, 20*np.log10(abs(h))) #General los puntos a graficar con los valores correspondientes de las abcisas y las ordenadas 
plt.xscale('log') #escala
plt.title('Butterworth filter frequency response') #titulo
plt.xlabel('Frecuencia [Hz]') #etiqueta de x
plt.ylabel('Amplitud [dB]') #etiqueta de y 
plt.margins(0, 0.1) #margenes
plt.grid(which='both', axis='both') #Red/cuadricula
plt.axvline(100, color='green')
plt.show() #muestra la figura 

# Respuesta inpulso 
imp = signal.unit_impulse(40) #señal impulso unitario
c, d = signal.butter(N, 0.5) #Señal butterwort
response = signal.lfilter(c, d, imp) 

#Trasado de la resuesta de fase 
plt.stem(np.arange(0, 40), imp, markerfmt='D', use_line_collection=True)
plt.stem(np.arange(0, 40), response, use_line_collection=True)
plt.margins(0, 0.1)
  
plt.xlabel('Time [samples]') #Muestreo en Tiempo
plt.ylabel('Amplitude') #Amplitud 
plt.grid(True)
plt.show()

# Respuesta en frecuencia 
fig, ax1 = plt.subplots()
ax1.set_title('Digital filter frequency response') #Filtro digital respuesta en frecuencia 
ax1.set_ylabel('Angulo(radians)', color='g')
ax1.set_xlabel('Frecuencia [Hz]')
  
angles = np.unwrap(np.angle(h))
  
ax1.plot(w/2*np.pi, angles, 'g')
ax1.grid()
ax1.axis('tight')
plt.show()
