import matplotlib.pyplot as plt
import numpy as np
from gekko import GEKKO

xm = np.array([0, 1, 2, 3, 4, 5])
ym = np.array([0.1, 0.2, 0.3, 0.5, 1.0, 0.9])

# Create interpolation model
m = GEKKO()  # create GEKKO model
m.x = m.Param(value=np.linspace(-1, 6))
m.y = m.Var()
m.options.IMODE = 2
m.cspline(m.x, m.y, xm, ym)
m.solve(disp=False)
# help(m.cspline)

# Create a second interpolation model with an objective function
p = GEKKO()
p.x = p.Var(value=1, lb=0, ub=5)
p.y = p.Var()
p.cspline(p.x, p.y, xm, ym)
p.Obj(-p.y)  # minimize -Y == maximize Y
p.solve(disp=False)

# create plot
plt.plot(xm, ym, 'bo', label='data')
plt.plot(m.x.value, m.y.value, 'r--', label='cubic spline')
plt.plot(p.x.value, p.y.value, 'ko', label='maximum')
plt.legend(loc='best')
plt.show()
