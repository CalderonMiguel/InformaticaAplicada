#Importacion de librerias 
import numpy as np
import statistics as stat 
import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns

#importacion de la base de datos 
basedatos=pd.read_csv(r'C:\Users\36174\InformaticaAplicada\InformaticaAplicada\ProyectoFinal\iris.csv')

#Acceso a cada dato por columna 
LSepalo=basedatos.iloc[:,0]   #Longitud del Sepalo       tipo: float64
ASepalo=basedatos.iloc[:,1]   #Ancho del Sepalo          tipo: float64
LPetalo=basedatos.iloc[:,2]   #Longitud del petalo       tipo: float64
APetalo=basedatos.iloc[:,3]   #Ancho del petalo          tipo: float64
Variedad=basedatos.iloc[:,4]  #Variedad                  tipo: object

#Estadistica Descriptiva 
#Promedio/media 
LSM=np.mean(LSepalo)  #Media o promedio de longitu del sepalo
ASM=np.mean(ASepalo)  #Media o promedio de ancho del sepalo
LPM=np.mean(LPetalo)  #Media o promedio de largo del petalo
APM=np.mean(APetalo)  #Media o promedio de ancho del petalo
print(" Media Largo Sepalo= ",LSM,"\n","Media Ancho Sepalo= ",ASM,"\n","Media Largo Petalo=",LPM,"\n","Media Ancho Petalo=",APM)
#Desviacion Estandar 
DELS=np.std(LSepalo) #Desviacion Estandar de longitu del sepalo
DEAS=np.std(ASepalo) #Desviacion Estandar de ancho del sepalo
DELP=np.std(LPetalo) #Desviacion Estandar de longitu del petalo
DEAP=np.std(APetalo) #Desviacion Estandar de ancho del petalo 
print("\n Desviacion Estandar Largo Sepalo=",DELS,"\n","Desviacion EstandarAncho Sepalo=",DEAS,"\n","Desviacion Estandar Largo Petalo=",DELP,"\n","Desviacion Estandar Ancho Petalo=",DEAP)
#Minímos y  maximos 
mLS=[min(LSepalo),max(LSepalo)] #Minimo y maximo de Longitud del Sepalo
mAS=[min(ASepalo),max(ASepalo)] #Minimo y maximo de Ancho del Sepalo
mLP=[min(LPetalo),max(LPetalo)] #Minimo y maximo de Largo del Petalo
mAP=[min(APetalo),max(APetalo)] #Minimo y maximo de Ancho del petalo 
print(f"\n Longitud minima: {mLS[0]} y maxima: {mLS[1]} del sepalo \n Ancho minim0: {mAS[0]} y maximo: {mAS[1]} del sepalo \n Longitud minima: {mLP[0]} y maxima: {mLP[1]} del petalo \n Ancho minimo: {mAP[0]} y maximo: {mAP[1]} del petalo")

#Graficas del inciso A informacion de datos y caracteristicas 
fig=plt.figure("Inciso A")
fig.clf()
ax=fig.subplots(2,4) #divicion de la figura en varios planos
x=range(0,150) #numero de observaciones 

ax[0,0].hist(LSepalo,rwidth=0.85)                    #Hisstograma de la longitud del sepalo 
ax[0,0].axvline(LSM,color='r')                       #graficacion de la media 
ax[0,0].set_title("Histograma de longitud sepalos ") #Titulo del histograma

ax[0,1].plot(x[0:49],LSepalo[0:49],x[50:99],LSepalo[50:99],x[100:149],LSepalo[100:149]) #Grafica del numero de observacion y la especie en longitud
ax[0,1].set_title("Grafico segun especie") #titulo

ax[0,2].hist(ASepalo,rwidth=0.85)                 #Histograma del ancho del sepalo 
ax[0,2].axvline(ASM,color='r')                    #graficacion de la mediana 
ax[0,2].set_title("Histograma de ancho sepalos ") #nombre del histograma 

ax[0,3].plot(x[0:49],ASepalo[0:49],x[50:99],ASepalo[50:99],x[100:149],ASepalo[100:149]) #Grafica del Ancho del sepalo con el numero de observacion dividido por especie
ax[0,3].set_title("Grafico segun especie") #titulo
 
ax[1,0].hist(LPetalo,rwidth=0.85)                  #Histograma de la longitud del petalo 
ax[1,0].axvline(LPM,color='r')                     #Linea de la mediana del largo del petalo 
ax[1,0].set_title("Histograma de largo  petalos ") #Titulo del histograma 

ax[1,1].plot(x[0:49],LPetalo[0:49],x[50:99],LPetalo[50:99],x[100:149],LPetalo[100:149]) #grafica de la observacion con longitud del petalo segun la especie 
ax[1,1].set_title("Grafico segun especie") #titulo 

ax[1,2].hist(APetalo,rwidth=0.85)                 #Histograma del ancho del petalo 
ax[1,2].axvline(APM,color='r')                    #graficacion de la mediana del ancho 
ax[1,2].set_title("Histograma de ancho petalos ") #titulo del histograma 

ax[1,3].plot(x[0:49],APetalo[0:49],x[50:99],APetalo[50:99],x[100:149],APetalo[100:149]) #Grafica del ancho del petalo segun observacion y especie
ax[1,3].set_title("Grafico segun especie") #Titulo segun especie 

plt.show()



fig2=plt.figure("Inciso B") #Graficas del inciso B relacion de variables
fig2.clf()
ax2=fig2.subplots(2,3) #sub segmentos de la grafica 

aux=np.mean(LPetalo[0:49])                                    #Calculo de la mediana para una sola variante
ax2[0,0].hist(LPetalo[0:49],rwidth=0.85,color="lightgreen")   #Grafica de histograma para una sola variante
ax2[0,0].axvline(aux,color='r')                               #Grafica del valor de la mediana para esta variante
ax2[0,0].set_title(" Histogramas de longitud de petalos \n (Setosa)") #Titulo 

aux=np.mean(LPetalo[49:99])                                    #Calculo de la mediana para una sola variante
ax2[0,1].hist(LPetalo[49:99],rwidth=0.85)                      #Grafica de histograma para una sola variante
ax2[0,1].axvline(aux,color='r')                                #Grafica del valor de la mediana para esta variante
ax2[0,1].set_title("Histogramas de longitud de petalos \n (Versicolor)") #Titulo 

aux=np.mean(LPetalo[100:149])                                    #Calculo de la mediana para una sola variante
ax2[0,2].hist(LPetalo[100:149],rwidth=0.85, color="orange")      #Grafica de histograma para una sola variante
ax2[0,2].axvline(aux,color='r')                                  #Grafica del valor de la mediana para esta variante
ax2[0,2].set_title("Histogramas de longitud de petalos \n (Virginica) ") #Titulo 

ax2[1,0].scatter(LSepalo[0:49],ASepalo[0:49],color="lightgreen") #Diagrama de dispercion largoxAncho del sepalo una variante
ax2[1,0].set_title(" Diagrama de dispersion") #Titulo 

ax2[1,1].scatter(LSepalo[50:99],ASepalo[50:99]) #Diagrama de dispercion largoxAncho del sepalo una variante
ax2[1,1].set_title(" Diagrama de dispersion") #Titulo 

ax2[1,2].scatter(LSepalo[100:149],ASepalo[100:149],color="orange") #Diagrama de dispercion largoxAncho del sepalo una variante
ax2[1,2].set_title(" Diagrama de dispersion")  #Titulo 
ax2[1,0].set_ylabel("Ancho Sepalo") #nombre del eje y diagrama 1
ax2[1,0].set_xlabel("Largo Sepalo") #nombre del eje x diagrama 1
ax2[1,1].set_ylabel("Ancho Sepalo") #nombre del eje y diagrama 2
ax2[1,1].set_xlabel("Largo Sepalo") #nombre del eje x diagrama 2
ax2[1,2].set_ylabel("Ancho Sepalo") #nombre del eje y diagrama 3
ax2[1,2].set_xlabel("Largo Sepalo") #nombre del eje x diagrama 3 
plt.show()

fig3=plt.figure("Inciso B") #Graficas del inciso B relacion de variables
fig3.clf()
ax3=fig3.subplots(3,1) #Division de la figura para graficar 
ax3[0].hist(LPetalo[0:49],rwidth=0.85,color="lightgreen",alpha=0.5,label="LPetalo") #histograma una variante longitud de petalos
ax3[0].hist(LPetalo[49:99],rwidth=0.85,alpha=0.5,label="LPetalo")                   #histograma una variante longitud de petalos
ax3[0].hist(LPetalo[100:149],rwidth=0.85, color="orange",alpha=0.5,label="LPetalo") #histograma una variante longitud de petalos

ax3[1].scatter(LSepalo[0:49],ASepalo[0:49],color="lightgreen",alpha=0.5)  #Diagrama una variante Largo x Ancho Sepalo
ax3[1].scatter(LSepalo[50:99],ASepalo[50:99],alpha=0.5)                   #Diagrama una variante Largo x Ancho Sepalo
ax3[1].scatter(LSepalo[100:149],ASepalo[100:149],color="orange",alpha=0.5)#Diagrama una variante Largo x Ancho Sepalo
ax3[1].set_ylabel("Ancho Sepalo") #nombre eje y
ax3[1].set_xlabel("Largo Sepalo") #nombre eje x 

ax3[2].scatter(LPetalo[0:49],APetalo[0:49],color="lightgreen",alpha=0.5)  #Diagrama una variante Largo x Ancho Petalo
ax3[2].scatter(LPetalo[50:99],APetalo[50:99],alpha=0.5)                   #Diagrama una variante Largo x Ancho Petalo
ax3[2].scatter(LPetalo[100:149],APetalo[100:149],color="orange",alpha=0.5)#Diagrama una variante Largo x Ancho Petalo
ax3[2].set_ylabel("Ancho Petalo") #nombre eje y
ax3[2].set_xlabel("Largo Petalo") #nombre eje x 

plt.legend(loc="upper right") 
plt.show()