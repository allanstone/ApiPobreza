import matplotlib.pyplot as plt
import numpy as np
data1=np.genfromtxt('Evolucion2010-2014.csv', delimiter=",",skip_header=1,usecols=(2,3,4,5,6)) 
plt.plot(data1,'o-')
plt.legend(loc='upper center', shadow=True, fontsize='x-large')
plt.xlabel('Niveles por año')
plt.title('Pobreza por estado')
plt.show()