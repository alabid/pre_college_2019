"""

Contains some functions to generate synthetic datasets and estimate the following functions:
1) Mean (with differential privacy).
2) Sum (with differential privacy).
3) Mean (without differential privacy).
4) Sum (without differential privacy).

"""

import numpy as np

def non_private_mean(data):
    return np.mean(data)

def non_private_sum(data):
    return np.sum(data)

def private_mean(data, n, eps):
    L = np.random.laplace(0., 1/(n*eps))
    m = non_private_mean(data)
    return m + L

def private_sum(data, n, eps):
    L = np.random.laplace(0., 1/eps)
    s = non_private_sum(data)
    return s + L

def main():
    n = 200
    # Generate n random floating point numbers between 0 and 1
    float_data = np.random.random(n)

    # Generate n random integers between 0 and 100
    integer_data = np.random.choice(100, n)

    # set epsilon privacy paramater (typically between 0 and 1)
    eps = 0.2

    print "non-private mean: ", non_private_mean(float_data)
    print "private mean: ", private_mean(float_data, n, eps), "\n"

    print "non-private sum: ", non_private_sum(float_data)
    print "private sum: ", private_sum(float_data, n, eps), "\n"

    print "non-private mean: ", non_private_mean(integer_data)
    print "private mean: ", private_mean(integer_data, n, eps), "\n"

    print "non-private sum: ", non_private_sum(integer_data)
    print "private sum: ", private_sum(integer_data, n, eps), "\n"

if __name__ == "__main__":
    main()

