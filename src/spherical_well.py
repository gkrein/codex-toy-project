from scipy.optimize import brentq
from scipy.special import spherical_jn


def spherical_bessel_zero(l, n):
    if l < 0:
        raise ValueError("l must be non-negative")
    if n < 1:
        raise ValueError("n must be at least 1")

    roots_found = 0
    step = 0.5
    left = 1e-8
    left_value = spherical_jn(l, left)

    while True:
        right = left + step
        right_value = spherical_jn(l, right)

        if left_value * right_value < 0:
            roots_found += 1
            root = brentq(lambda x: spherical_jn(l, x), left, right)
            if roots_found == n:
                return root

        left = right
        left_value = right_value


def spherical_well_energy(l, n, hbar=1.0, mass=1.0, radius=1.0):
    alpha = spherical_bessel_zero(l, n)
    return hbar**2 * alpha**2 / (2 * mass * radius**2)
