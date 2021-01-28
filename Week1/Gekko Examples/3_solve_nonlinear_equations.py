from gekko import GEKKO

m = GEKKO()  # create GEKKO model
# initial conditions
x0, y0 = 0, 1
x = m.Var()
y = m.Var()
m.Equations([x + y == 0, x ** 2 + y ** 2 == 0])
m.options.SOLVER = 1
m.solve(disp=False)
print(f'Solve x and y in equations:\n x + y == 0 \n x**2 + y**2 == 0')
print(f'Gekko response\n x = {x.value[0]}, y = {y.value[0]}')
