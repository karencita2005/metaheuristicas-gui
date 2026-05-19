# ==========================================
# FUNCIÓN SPHERE
# ==========================================

def sphere(x):

    return sum(i**2 for i in x)

# ==========================================
# FUNCIÓN RASTRIGIN
# ==========================================

import math

def rastrigin(x):

    n = len(x)

    return 10 * n + sum(
        (i**2 - 10 * math.cos(2 * math.pi * i))
        for i in x
    )

# ==========================================
# FUNCIÓN ROSENBROCK
# ==========================================

def rosenbrock(x):

    total = 0

    for i in range(len(x) - 1):

        total += (
            100 * (x[i+1] - x[i]**2)**2
            + (1 - x[i])**2
        )

    return total