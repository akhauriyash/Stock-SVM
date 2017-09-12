from numpy import genfromtxt
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simps
data = genfromtxt('banknifty.csv', delimiter=',')
for j in range(7):
    for i in range(len(data)):
        if(np.isnan(data[i][j])):
            data[i][j] = 0
print(data)
ab = np.arange(len(data)-1)
ab = ab.astype(float)
data = np.delete(data,[0], axis = 0)
print(ab.dtype)
print(len(data))
for k in range(len(data)-2):
    try:
        ab[k] = 100*(float(data[k+1][5]-data[k][5]))/(data[k][5])
    except:
        ab[k] = 9999
ab = np.around(ab, 1)
cd = np.zeros((400,2))
cd = cd.astype(float)
for i in range(400):
    cd[i][0] = (i-200)/10
for k in range(2416):
    for i in range(400):
        if(cd[i][0] == ab[k]):
            cd[i][1] += 1
print(cd)
cd = cd.T
print(cd[1])
plt.plot(cd[0], cd[1])
plt.axis([-20,20, 0, 160])
plt.show()
for i in range(400):
    if(cd[0][i] < 990):
        k += cd[0][i]*cd[1][i]
print(k)
cd = cd.T
np.savetxt('codebanknifty.csv', cd, delimiter = ',')