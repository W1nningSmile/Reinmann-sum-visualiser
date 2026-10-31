import numpy as np
import matplotlib.pyplot as plt

# 1. Define the math-heavy parts outside the class for easy compilation
def fast_formula(x):
    return np.sin(x)


def fast_area_calc(lspace, x1):
    x_fodder = x1
    area = 0.0
    for i in lspace:
        area += (i - x_fodder) * fast_formula(i)
        x_fodder = i
    return area


class Integration:
    def __init__(self, x1, x2, n=20000):
        self.x1 = x1
        self.x2 = x2
        self.n = n

    def calculation(self):
        x_list = np.linspace(self.x1, self.x2, self.n, endpoint=True)
        y_list = fast_formula(x_list)
        return x_list, y_list

    def area(self):
        lspace, _ = self.calculation()
        # 2. Call the compiled Numba function here
        return fast_area_calc(lspace, self.x1)

    def graphing(self):
        x_list, y_list = self.calculation()
        area_val = self.area()

        plt.fill_between(x_list, 0, y_list, alpha=0.2)
        print(f"The area is equal to: {area_val}")

        # Plotting remains in standard Python (Matplotlib isn't Numba-compatible)
        plt.axhline(0, color='black')
        plt.axvline(0, color='black')
        plt.plot(x_list, y_list)
        plt.xlim(-11.1, 11.1)
        plt.ylim(-1.1, 1.1)
        plt.show()


test = Integration(-100, 100)
test.graphing()