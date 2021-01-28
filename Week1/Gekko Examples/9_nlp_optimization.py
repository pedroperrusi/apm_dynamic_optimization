from gekko import GEKKO

# Initialize Model
m = GEKKO()

# help(m)

# define parameter
eq = m.Param(value=40)

# initialize variables
x0 = [1, 5, 5, 1]  # initial values
xlow = [1, 1, 1, 1]  # lower bounds
xup = [5, 5, 5, 5]  # upper bounds

# Define model variables
x1, x2, x3, x4 = [m.Var(value=x0[i], lb=xlow[i], ub=xup[i]) for i in range(4)]

# Objective to minimize
m.Obj(x1 * x4 * (x1 + x2 + x3) + x3)

# Subject to Constraints
m.Equation(x1 * x2 * x3 * x4 >= 25)
m.Equation(x1 ** 2 + x2 ** 2 + x3 ** 2 + x4 ** 2 == eq)


# Set global options
m.options.IMODE = 3  # steady state optimization

# Solve simulation
m.solve()

# Results
print('')
print('Results')
print('x1: ' + str(x1.value))
print('x2: ' + str(x2.value))
print('x3: ' + str(x3.value))
print('x4: ' + str(x4.value))
