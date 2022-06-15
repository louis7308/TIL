import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

N = 100
cmap = cm.get_cmap('rainbow', lut=N)
X = np.random.normal(40, 5, (N, ))
Y = (X > 40).astype(int)

a, b = -1, 38
test_x = np.linspace(30, 50, 100)
pred = a*test_x + b
pred = 1/(1 + np.exp(-pred))

fig, ax = plt.subplots(figsize=(10, 5))
ax.scatter(X, Y)
ax.plot(test_x, pred)

learning_rate = 0.03
for i in range(N):
    x, y = X[i], Y[i]

    z = a*x + b;
    pred = 1/(1 + np.exp(-z))
    J = -(y*np.log(pred) + (1-y)*np.log(1-pred))

    dJ_dpred = -(y/pred - (1-y)/(1-pred)) + 0.0001
    dJ_dz = dJ_dpred * pred * (1-pred)
    dJ_da = dJ_dz * x
    dJ_db = dJ_dz * 1

    a = a - learning_rate * dJ_da
    b = b - learning_rate * dJ_db
    ax.plot(test_x, pred, color=cmap(i))