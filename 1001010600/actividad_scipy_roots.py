from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np

#funcion dada
def f(x):
    return np.sqrt(x**2 + 1) + np.exp(x)*np.sin(x) -7 

#parametros donde se espera hallar la raiz
a = 0
b = 2

#se halla la raiz con scipy
r = optimize.bisect(f, a, b, maxiter = 1000, full_output = False) 
print('La primera solucion es: {}'.format(r))

#grafico
x= np.linspace(0, 2, 50000)

plt.plot(x,np.sqrt(x**2 + 1) + np.exp(x)*np.sin(x) -7,'g')
plt.plot(r,0, 'bo') #raiz en el grafico
plt.text(0.8,0.8, 'First solution\nx = {}'.format(r), fontsize = 12) #texto en el grafico

plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()
