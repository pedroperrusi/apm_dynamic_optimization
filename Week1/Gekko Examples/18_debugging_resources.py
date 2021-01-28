from gekko import GEKKO

m = GEKKO()  # create GEKKO model

print('--------- Follow local path to view files --------------')
print(m.path)  # show source file path
print('--------------------------------------------------------')

# test application
u = m.FV(value=5, name='u')  # define fixed value
x = m.SV(name='state')  # define state variable
m.Equation(x == u)  # define equation
m.options.COLDSTART = 1  # coldstart option
m.options.DIAGLEVEL = 0  # diagnostic level (0-10)
m.options.MAX_ITER = 500  # adjust maximum iterations
m.options.SENSITIVITY = 1  # sensitivity analysis
m.options.SOLVER = 1  # change solver (1=APOPT,3=IPOPT)
m.solve(disp=True)  # solve locally (remote=False)
print('x: ' + str(x.value))  # print variable value
