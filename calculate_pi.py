import numpy as np
import math

def calc_pi(n=1000000):
    '''
    An approximation of pi. n is the number of points to count in the approximation. Larger n leads to more accurate estimation, in addition to longer runtime.
    '''

    x = np.random.uniform(-1,1,n)
    y = np.random.uniform(-1,1,n)

    count = 0
    for i in range(n):
        if x[i]**2 + y[i]**2 <= 1:
            count += 1

    pi = count / n * 4
    return pi, math.pi - pi
