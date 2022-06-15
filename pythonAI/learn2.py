import numpy as np
import matplotlib.pyplot as plt

t_a, t_b = 3, -1
N = 100
X = np.random.normal(loc=0, scale=1, size=(N, ))
Y = t_a * X + t_b
noise = 0.3*np.random.normal(loc=0, scale=1, size=(N, ))
Y = Y + noise

a, b = -2, 5
X_min, X_max = X.min(), X.max()
Y_min = a*X_min + b
Y_max = a*X_max + b


fig, ax = plt.subplots(figsize=(10, 10))
ax.scatter(X, Y, alpha=0.5)
ax.plot([X_min, X_max], [Y_min, Y_max])
ax.axvline(x=0, linestyle=':', linewidth=1)
ax.axhline(y=0, linestyle=':', linewidth=1)

plt.show()