# METODE NUMERIK-01
# TUGAS 4.3 : METODE NEWTON-RAPHSON
# Nama      : MUHAMMAD HURRICANE
# NPM       : 1906356191

import math
# Input Data
print("==========PERHITUNGAN NEWTON-RAPHSON==========")
a = float(input('Titik asumsi Xns awal : '))
error = float(input('Besar toleransi : '))
max_iter = float(input('Iterasi Maksimum : '))

# Definisi Fungsi       
def f(x):
    return math.pow(x,3)-2.72144556*math.pow(x,2)+0.23166*x-0.013597674
# Definisi Turunan Fungsi
def df(x):
    return 3*math.pow(x,2)-5.44289112*x+0.23166
# Model Operasi Metode Newton-Raphson
def operationNR(a,error):
    step = 1
    opState = True
    while opState:
        c = a - (f(a)/df(a))
        EA = abs((c-a)/c)
        print('i= %d, Xns= %0.6f, f(Xns)= %0.4f, df(Xns)= %0.4f, EA= %0.8f' % (step,a,f(a),df(a),EA))
        opState = EA > error and step <= max_iter
        a = c
        step = step + 1

operationNR(a,error)
print("Semua pemrograman ini dibuat secara orisinil oleh M. Hurricane")

        
