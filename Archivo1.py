import numpy as np
import pylab as pl 
# crea un vector con los valores de x
x = [5000, 6000, 7000, 8000, 9000]
# crea un vector con los valore de y 
y = [65, 78, 88, 89, 93]
# grafica el vector x contra el vector y
pl.plot(x,y)

# crea un vector con los valores del eje x 
x1 = [7000, 8000, 9000, 10000, 11000]
# crea un vector con los valores del eje y para cada valor en el eje x
y2 = [65, 75, 85, 86, 90]
# grafica el vector x contra el vector y 
pl.plot(x1,y2)

pl.xlabel('Voltaje [V]')
pl.ylabel('Eficiencia [%]')
# guarda la grafica en formato png
pl.savefig('Archivo1.png')


