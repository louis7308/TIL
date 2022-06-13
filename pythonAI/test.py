import numpy as np
import matplotlib.pyplot as plt

w, b = 3, -1
x = np.random.normal(0, 1, size=(100, ))
y = w*x + b
noise = np.random.normal(0, 0.3, (100, ))
y = y + noise
# y = 1/(1 + np.exp(-y))

fig, ax = plt.subplots(figsize=(10, 10))
ax.scatter(x, y, alpha=0.5)
ax.tick_params(labelsize=20)
plt.show()