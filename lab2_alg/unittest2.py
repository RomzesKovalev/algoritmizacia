import unittest
import numpy as np
from scipy.integrate import quad

def simpson_rule(f, a, b, n):
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    fx = f(x)
    integral = (h / 3) * (fx[0] + 4 * sum(fx[1:-1:2]) + 2 * sum(fx[2:-2:2]) + fx[-1])
    return integral

def figure_area(N=1000):
    def integrand(x):
        upper = np.minimum(np.sin(x), np.sin(0.5 * x) - 0.5)
        lower = np.cos(x)
        return np.where(upper > lower, upper - lower, 0)
    return simpson_rule(integrand, 2, 4, N)

def integral_area():
    def integrand(x):
        upper = np.minimum(np.sin(x), np.sin(0.5 * x) - 0.5)
        lower = np.cos(x)
        return np.where(upper > lower, upper - lower, 0)
    result, a = quad(integrand, 2, 4)
    return result


class TestFigureArea(unittest.TestCase):
    def test_N_100(self):
        self.assertAlmostEqual(figure_area(100), integral_area(), places=4)

    def test_N_1000(self):
        self.assertAlmostEqual(figure_area(1000), integral_area(), places=4)

    def test_N_10000(self):
        self.assertAlmostEqual(figure_area(10000), integral_area(), places=4)


if __name__ == "__main__":
    unittest.main()