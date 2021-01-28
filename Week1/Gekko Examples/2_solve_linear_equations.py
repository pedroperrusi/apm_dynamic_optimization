from gekko import GEKKO

m = GEKKO()  # create GEKKO model
x = m.Var()
y = m.Var()
m.Equations([3 * x + 2 * y == 1, x + 2 * y == 0])
m.options.SOLVER = 3
m.solve(disp=False)
print(f'Solve x and y in equations:\n 3*x + 2*y == 1 \n x + 2*y == 0')
print(f'Gekko response\n x = {x.value[0]}, y = {y.value[0]}')
