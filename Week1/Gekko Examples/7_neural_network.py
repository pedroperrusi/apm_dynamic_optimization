import matplotlib.pyplot as plt
import numpy as np
from gekko import brain

# generate training data limited between 0 and 2 pi
x = np.linspace(0.0, 2 * np.pi, 20)
y = np.sin(x)

# Describe Neural Network model in GEKKO brain
b = brain.Brain()
b.input_layer(1)
b.layer(linear=2)
b.layer(tanh=3)
b.layer(linear=2)
b.output_layer(1)

b.learn(x, y)  # train

# Test it in a larger interval, from -2 pi to 4pi
xp = np.linspace(-2 * np.pi, 4 * np.pi, 100)
yp = b.think(xp)  # validate

plt.figure()
plt.plot(x, y, 'bo')
plt.plot(xp, yp[0], 'r-')
plt.show()
