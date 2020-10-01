import pandas as pd
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import LagrangePolynomial as LP

df = pd.DataFrame({'X' : [3.,10.,21.3,-7.], 'Y': [8.,6.5,3.,6.]})

print(df)
#Numpy form
coef = np.polyfit(df.X,df.Y, deg = 3)
p = np.poly1d(coef)

print(p)

#Lagrange form

lagr_poly = interpolate.lagrange(df.X,df.Y)
print(lagr_poly)


#Graficos
x = np.linspace(df.X.min(),df.X.max())

fig, ax = plt.subplots(2,1)

ax[0].plot(x, lagr_poly(x), 'b-')
ax[0].plot(df.X,df.Y,'ro')
ax[0].set_title('$Lagrange$ $form$')

ax[1].plot(x,p(x),'g-')
ax[1].plot(df.X,df.Y,'ro') 
ax[1].set_title('$Numpy$ $form$') 
plt.show()

#Evaluando polinomios de lagrange

print(LP.L(df.X,0)(df.X)) #para el primer punto su valor es 1 y para el resto es 0
print(LP.L(df.X,1)(df.X))
print(LP.L(df.X,2)(df.X))
print(LP.L(df.X,3)(df.X))



