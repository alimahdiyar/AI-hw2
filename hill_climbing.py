import random
from math import sin, cos, pi, log, copysign
import numpy as np
import matplotlib.pyplot as plt

STEP = 1e-4

def f(x):
    return sin(10 * pi * x) / (2 * x) + (x - 1) ** 4

def fp(x):
    return -sin(10 * pi * x) / (2 * x ** 2) + (5 * pi * cos(10 * pi * x)) / x + 4 * (x - 1) ** 3

def draw(x_arr, minimum, f):
    fv = np.vectorize(f)
    all_f = np.arange(0.5, 2.5, STEP)
    _, plot = plt.subplots()
    plot.set_xlabel('x')
    plot.set_ylabel('f(x)')
    plot.plot(all_f, fv(all_f))
    plot.scatter(x_arr, fv(x_arr), s=50, c='green', marker='s')
    plot.scatter(minimum, f(minimum), s=50, c='red', marker='s')
    plt.show()

def draw_sa(x, path, minimum, f):
    fv = np.vectorize(f)
    all_f = np.arange(0.5, 2.5, STEP)
    _, plot = plt.subplots()
    plot.set_xlabel('x')
    plot.set_ylabel('f(x)')
    plot.plot(all_f, fv(all_f))
    plot.plot(path, fv(path))
    plot.scatter(x, f(x), s=50, c='green', marker='s')
    plot.scatter(minimum, f(minimum), s=50, c='red', marker='s')
    plt.show()

def hill_climbing(x, f, fp):
    sign = lambda x: copysign(1, x)
    ans = x
    while True:
        step = (-1) * sign(fp(ans)) * STEP
        if(ans <= 0.5 or ans >= 2.5 or sign(fp(ans)) != sign(fp(ans + step))):
            return ans
        ans += step
        
def iterative_hill_climbing(f, fp, times):
    x_arr = [random.random() * 2 + 0.5 for _ in range(times)]
    ans = min([hill_climbing(x, f, fp) for x in x_arr])
    draw(x_arr, ans, f)

def simulated_annealing(f, fp):
    x = random.random() * 2 + 0.5
    ans = x
    path = [x]
    Temperature = 1
    for i in range(1, 10000):
        step = random.choice([-1,1]) * Temperature
        p = Temperature
        n = ans + step
        if 0.5 <= n <= 2.5:
            if f(n) < f(ans):
                ans = n
                path.append(n)
            else:
                if random.random() < p:
                    ans = n
                    path.append(n)
        Temperature *= 0.95
    draw_sa(x, path, ans, f)

# iterative_hill_climbing(f, fp, 1) #normal hill climbing
# iterative_hill_climbing(f, fp, 100) #iterative hill climbing
simulated_annealing(f, fp) #simulated_annealing
