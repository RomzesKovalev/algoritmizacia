import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


def y1(x):
    return np.sin(x)


def y2(x):
    return np.cos(x)


def y3(x):
    return np.sin(0.5 * x) - 0.5


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
        return np.minimum(y1(x), y3(x)) - y2(x)
    return simpson_rule(integrand, 2, 4, N)


def integral_area():
    def integrand(x):
        upper = np.minimum(np.sin(x), np.sin(0.5 * x) - 0.5)
        lower = np.cos(x)
        return np.where(upper > lower, upper - lower, 0)
    result, a = quad(integrand, 2, 4)
    return result


def experiment(N_values):
    return {n: figure_area(n) for n in N_values}


def plot_area():
    x_all = np.linspace(-10, 10, 1000)
    x_shade = np.linspace(2, 4, 1000)
    plt.figure(figsize=(10, 6))
    plt.plot(x_all, y1(x_all), 'blue', label=r'$y = \sin(x)$')
    plt.plot(x_all, y2(x_all), 'red', label=r'$y = \cos(x)$')
    plt.plot(x_all, y3(x_all), 'green', label=r'$y = \sin(0.5x) - 0.5$')
    plt.fill_between(x_shade, y2(x_shade), np.minimum(y1(x_shade), y3(x_shade)), color = 'gray', alpha = 0.3)
    plt.xlim(-1, 1)
    plt.xticks(np.arange(0, 11, 2))
    plt.yticks(np.arange(-2, 2.5, 0.5))
    plt.grid(True)
    plt.legend()
    plt.title('Область интегрирования')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


if __name__ == "__main__":
    print("Значение площади через интеграл: ", integral_area())
    print("Значения площади через Симпсона с подстановкой разных N ")
    for n, value in experiment([100, 1000, 10000]).items():
        print(f"N: {n}, Площадь: {value}")
    plot_area()