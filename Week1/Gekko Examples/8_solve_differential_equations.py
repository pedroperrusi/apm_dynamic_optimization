import matplotlib.pyplot as plt
import numpy as np
from gekko import GEKKO

m = GEKKO()
k = 10
m.time = np.linspace(0, 20, 100)

y = m.Var(value=5)
t = m.Param(value=m.time)
m.Equation(k * y.dt() == -t * y)
m.options.IMODE = 4
m.solve(disp=False)

plt.plot(m.time, y.value)
plt.xlabel('time')
plt.ylabel('y')
plt.show()
