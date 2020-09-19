import numpy as np

#initial conditions

#car 1
x1_0 = 0
t1_0 = 0
v1_0 = 0
a1 = 6 

x1 = np.poly1d([0.5*a1,v1_0,x1_0], variable = 't')

#car 2
x2_0 = 0
t2_0 = 10
v2_0 = 10
a2 = 10

x2 = np.poly1d([0.5*a2, v2_0-a2*t2_0, x2_0-v2_0*t2_0 + 0.5*a2*(t2_0)**2], variable = 't')
#roots
r = (x1-x2).roots

print('Polinomio 1\n', x1,'\n', 'Polinomio 2\n', x2)
print('Los autos se encuentran en x = {} m'.format(x2(r[1])))