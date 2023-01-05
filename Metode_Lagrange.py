

# Import NumPy Library
import numpy as np
    
# tampilan grafik 
import matplotlib.pyplot as plt

# Memasukan banyak titik
n = int(input('Memasukan banyak titik: '))

# inisialisasi x
x = np.zeros((n))
# inisialisasi y
y = np.zeros((n))


# Masukan data x dan y
print('Masukan data x dan y: ')
#perulangan untuk input data
for i in range(n):
    x[i] = float(input( 'x['+str(i)+']=')) # masukan x[i]
    y[i] = float(input( 'y['+str(i)+']=')) # masukan y[i]


# input masukan yang dicari
xp = float(input('masukan input yang mau dicari: '))

# set data dari 0
yp = 0 

# algoritma Lagrange
for i in range(n): 
    p = 1
    for j in range(n):
        if i != j:
            p = p * (xp - x[j])/(x[i] - x[j])
    yp = yp + p * y[i]    

# tampilan hasil
print('Pada x %.3f mempunyai f(x) atau y  %.3f' % (xp, yp))
plt.plot(x, y, marker = '*')
plt.plot(xp, yp, marker = 'o')
plt.show()