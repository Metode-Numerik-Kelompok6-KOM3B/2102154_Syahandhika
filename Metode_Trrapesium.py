# Mencari integral untuk f(x) dengan metode trapesium
e= 2.71828
def f(x):
    pepega = eval(fx)
    return pepega

# Algoritma Trapesium
def trapezoidal(a,b,n):
    h = (b - a) / n
    integration = f(a)+f(b)
    for i in range(1,n):
        k = a + i*h
        integration = integration+ 2 * f(k)
    integration = integration * h/2
    return integration
    
# Input
fx = str(input("masukan fungsinya : "))
a = float(input("Masukkan batas bawah: "))
b = float(input("Masukkan batas atas: "))
n = int(input("Masukkan jumlah iterasi: "))

# Hasil
result = trapezoidal(a, b, n)
print("Integral dengan metode trapesium: %0.6f" % (result))