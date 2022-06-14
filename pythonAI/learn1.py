t_x = -10
x = 8
learning_rate = 0.1

for i in range(10):
    diff = 2 * (x-2)
    x = x - learning_rate * diff
    print(x)