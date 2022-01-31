"""
Developed by Muhammad Hurricane <muhammad.hurricane@ui.ac.id>
Mechanical Engineering, University of Indonesia
"""
from sympy import symbols, diff
# declare involved variables
x, y = symbols('x y')
# declare eqs that are required in the calculation
f1_eqs = x**2 + 2*x + 2*y**2 - 26
f2_eqs = 2*x**3 - y**2 + 4*y - 19
# Partial derivative of f1 and f2 respect to x
df1dx_eqs = diff(f1_eqs,x)
df2dx_eqs = diff(f2_eqs,x)
# Partial derivative of f1 and f2 respect to y
df1dy_eqs = diff(f1_eqs,y)
df2dy_eqs = diff(f2_eqs,y)

'''
Syntax :
>> converted_Eq = sympy.lambdify([var1,var2,...],Eq)
'''
# Transformed into usable eqs
from sympy import lambdify
f1 = lambdify([x,y],f1_eqs)
df1dx = lambdify([x,y],df1dx_eqs)
df1dy = lambdify([x,y],df1dy_eqs)
f2 = lambdify([x,y],f2_eqs)
df2dx = lambdify([x,y],df2dx_eqs)
df2dy = lambdify([x,y],df2dy_eqs)

# Let's define the main function
def Func(x,y):
    return [f1(x,y),
            f2(x,y)]

# Jacobian Eqs = Define all partial derivatives in one place
def Jacob(x,y):
    return [[df1dx(x,y), df1dy(x,y)],
            [df2dx(x,y), df2dy(x,y)]]
    
# Pengaplikasian metode Newton-Jacob
def Newton(q_awal):
    import numpy
    ux = q_awal[0] # tebakan pertama x
    uy = q_awal[1] # tebakan pertama y
    J = Jacob(ux,uy)
    F = Fungsi(ux,uy)
    # q sebagai vektor solusi. Jika matriks Jq = F,
    # maka x dapat dicari dengan Gauss-Jordan
    q = numpy.linalg.solve(J,F)
    # Tebakan selanjutnya...
    q_Accumulator = q_awal - q
    return q_Accumulator

# Mekanisme proses iterasi
def Iterasi(q_awal):
    import numpy
    error = 10**(-6)
    max_iter = 1000
    q_lama = q_awal          # ambil dari nilai tebakan awal
    q_baru = Newton(q_lama)  # ambil dari metode Newton-Jacob
    dq = numpy.linalg.norm(q_lama-q_baru)  # cek bedanya (dlm bentuk vektor)
    step = 0
    looping = True
    while looping:
        q_baru = Newton(q_lama)
        dq = numpy.linalg.norm(q_lama-q_baru)
        q_lama = q_baru
        step += 1
        looping = dq>error and step<=max_iter
    hasil = q_baru
    print('\n\nMUHAMMAD HURRICANE 1906356191 Newton-Jacob')
    print('Hasil tercapai pada iterasi ke %d dan nilai error sebesar %0.20f' %(step,dq))
    return hasil

# Tebakan nilai q
ux = 1  # tebakan pertama x
uy = 1  # tebakan pertama y
# Mengakumulasi semua nilai hasil iterasi
hasil = list(map(float,(Iterasi([ux,uy]))))
print(f'Adapun hasil rooting dari sistem yang diberikan adalah {hasil}')
