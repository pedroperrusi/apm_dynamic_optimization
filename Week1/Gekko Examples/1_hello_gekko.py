from gekko import GEKKO

m = GEKKO()  # create GEKKO model
y = m.Var(value=2)  # define new variable, initial value=2
m.Equation(y ** 2 == 1)  # define new equation
m.options.SOLVER = 3  # change solver (1=APOPT,3=IPOPT)
m.solve(disp=False)
print(f'Solve y in equation:\n y ** 2 = 1')
print(f'Gekko response y: {y.value[0]}')  # print variable value
