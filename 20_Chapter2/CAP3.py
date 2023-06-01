import numpy as np
import statistics as stat 


dts=np.array([5,7,8,9,10,11,12,14,15,16])

dts1=np.array([5,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

print("Moda=",stat.mode(dts))
print("Mediana=",np.median(dts))
print("Desviacion=",np.std(dts))

dev=np.std(dts1)
var=np.var(dts1)

cv=dev/var
print("Coeficioente de variacion=",cv)


