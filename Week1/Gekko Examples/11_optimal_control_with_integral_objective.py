import matplotlib.pyplot as plt
import numpy as np
from gekko import GEKKO

m = GEKKO()  # initialize gekko
nt = 101  # number of timestamps
m.time = np.linspace(0, 2, nt)
# Variables
x1 = m.Var(value=1)
x2 = m.Var(value=0)
u = m.Var(value=0, lb=-1, ub=1)  # bounded control signal
p = np.zeros(nt)  # mark final time point (logic mask)
p[-1] = 1.0
final = m.Param(value=p)
# Equations
m.Equation(x1.dt() == u)
m.Equation(x2.dt() == 0.5 * x1 ** 2)
m.Obj(x2 * final)  # Objective function - minimize x2
m.options.IMODE = 6  # optimal control mode
m.solve(disp=False)  # solve
plt.figure(1)  # plot results
plt.plot(m.time, x1.value, 'k-', label=r'$x_1$')
plt.plot(m.time, x2.value, 'b-', label=r'$x_2$')
plt.plot(m.time, u.value, 'r--', label=r'$u$')
plt.legend(loc='best')
plt.xlabel('Time')
plt.ylabel('Value')
plt.show()
