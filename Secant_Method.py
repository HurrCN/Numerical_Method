# METODE NUMERIK-01
# TUGAS 4.4 : SECANT METHOD
# Nama      : MUHAMMAD HURRICANE
# NPM       : 1906356191

import math
# Input Data
print("==========PERHITUNGAN SECANT METHOD==========")
a = float(input('Titik asumsi Xns1 : '))
b = float(input('Titik asumsi Xns2 : '))
error = float(input('Besar toleransi : '))
max_iter = float(input('Iterasi Maksimum : '))

# Definisi Fungsi       
def f(x):
    return math.pow(x,3)-2.72144556*math.pow(x,2)+0.23166*x-0.013597674
# Definisi Turunan Fungsi
def df(x):
    return 3*math.pow(x,2)-5.44289112*x+0.23166
# Model Operasi Metode Secant
def operationSecant(a,b,error):
    step = 2
    opState = True
    while opState:
        c = b - ((f(b)*(a-b))/(f(a)-f(b)))
        EA = abs((c-b)/c)
        print('i= %d, Xns= %0.4f, f(Xns)= %0.4f, df(Xns)= %0.4f, EA= %0.8f' % (step-1,b,f(b),df(b),EA))
        opState = EA > error and step <= max_iter
        a = b
        b = c
        step = step + 1

operationSecant(a,b,error)
print("Semua pemrograman ini dibuat secara orisinil oleh M. Hurricane")
        

