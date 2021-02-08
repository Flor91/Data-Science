import numpy as np

seed = 2843
size = 500
n = 100
p = 0.7


def random_binomial(seed, size, n, p):
    random_generator = np.random.default_rng(seed)
    result = random_generator.normal(loc=n, scale=p, size=size)

    return result


def random_uniforme(seed, size, low, high):
    random_generator = np.random.default_rng(seed)
    result = random_generator.uniform(low=low, high=high, size=size)

    return result


r = random_binomial(seed, size, n, p)
# print(r)

ru = random_uniforme(seed, (3, 4, 5), 5, 100)
# print(ru)
