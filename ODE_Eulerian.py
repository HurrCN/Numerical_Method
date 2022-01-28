"""
Solution by Muhammad Hurricane <muhammad.hurricane@ui.ac.id>
Mechanical Engineering, University of Indonesia

SAMPLE PROBLEM :
A tank contains 1000 gal of water which initially 100 lb of salt is dissolved.
Brine runs in at a rate of 10 gal/min, and each gal contains 5 lb of dissolved
salt. The mixture in the tank is kept uniform by stirring. Brine runs out at 10
gal/min. Find the amount of salt in the tank at anytime t.
"""
# Say, we have iteration interval about 0.01 min
dt = 0.01
# And we observe the tank for 1000 min
obs_time = 1000
# Therefore, the iteration segments nt:
nt = int(obs_time/dt)

from numpy import linspace, zeros
# Fraction of obs_time will be defined as:
t = linspace(0,nt*dt,nt+1)
# Say, m as the amount of salt that we observe.
m = zeros(nt+1)
# which initially 100 lb of salt is dissolved
m[0] = 100

"""
As we all know, y'= dy/dt = (y2-y1)/dt
y2 = y'dt + y1
We can use it to predict the next value of mass.
m[n+1] = m'dt + m[n]
But how about the mass flow rate m'?

We can get the equation of m' by this logic:
Profit = Revenue - Capital
m' = m'_in - m'_out
The inlet mass flows at rate m'_in = (10 gal/min)*(5 lb/gal) = 50 lb/min
The mixture flows out at volumetric rate V'_out = 10 gal/min. We then assume
that the volume inside the tank is kept constant at 1000 gal as the inlet and outlet 
volumetric rate has the same value. By this assumption, we can say that the outflow 
rate is taking 10/1000 = 1% = 0.01 of WHAT'S INSIDE the tank every minute. Hence, the
we get the m'_out = (0.01*m) lb/min.
m' = m'_in - m'_out
m' = 50 - 0.01*m
"""

for n in range (nt):
  m[n+1] = (50-(0.01*m[n]))*dt + m[n]

# Plotting
import matplotlib.pyplot as plt
plt.plot(t,m,'r-')
plt.xlabel('Time [mins]')
plt.ylabel('Salt content [lb]')
plt.title('Brine observation')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#666666', linestyle='-', alpha=0.1)
plt.show()
