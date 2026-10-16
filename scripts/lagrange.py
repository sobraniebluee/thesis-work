# Lagrange Interpolation
# Check: https://www.is.umk.pl/~pierzcham/numerical/#orgf340dc7
# Check: https://github.com/ApurbaKumarNath/numerical-methods-python/blob/main/03_Polynomial_Interpolation/2_Lagrange_Interpolation.ipynb

import matplotlib.pyplot as plt
import numpy as np


def lagrange_basis_i(index: float, x: float, x_points: list[float]):
    n = len(x_points)
    result = 1

    for k in range(n):
        if k == index:
            continue
        
        result *= (x - x_points[k]) / (x_points[index] - x_points[k])

    return result 



def lagrange_interpolation(x, x_points, y_points):
    if len(x_points) != len(y_points):
        raise AssertionError("x_points array and y_points array should have the same length")

    n = len(x_points)

    result = 0
    for i in range(n):
        result += y_points[i] * lagrange_basis_i(index=i, x=x, x_points=x_points)

    return result


def interpolate(x_arr, x_points, y_points):
    result = []
    for x in x_arr:
        result.append(
            lagrange_interpolation(x, x_points, y_points)
        )

    return np.array(result)


# Interpolation function
f = lambda x: x**2 + 2*x + 2

interpolation_x = np.array([-2, 0, 3, 5])
interpolation_y = np.array([-8, 2, 15, 40])
# interpolation_y = [f(x) for x in interpolation_x]
# X_POINTS = np.array([-2, 0, 3, 5])
# Y_POINTS = np.array([-8, 2, 15, 40])

test_x = np.array([-1, 1, 2, 4])

x = np.linspace(-3, 6, num=200)
f_y = f(x)
inerpolated_y = interpolate(
    x, x_points=interpolation_x, y_points=interpolation_y
)

test_y = f(test_x)



# error_arr = np.abs(y - y_for_inter_points)
# print(np.max(error_arr))
plt.figure(figsize=(10, 6))
plt.title("Lagrange Interpolation")

plt.plot(
    interpolation_x, interpolation_y, marker='o', linestyle='', color='green', label="Interpolation Points"
)

plt.plot(x, inerpolated_y, label="Langrange'a Polynomial")
plt.plot(x, f_y, label=r"$f(x) = x^3 + 2x + 2$", linestyle="--")

plt.plot(test_x, test_y, marker='s', linestyle="", color='red')

plt.legend()

plt.savefig("plot.pdf", format="pdf")  
