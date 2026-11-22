
"""
Program Name: Lab 15 - Plotting Cubic Numbers
Author: Misker Negash
Purpose: Generate and save plots of the first 5 cubes
         and the first 5000 cubes using matplotlib.
Starter Code: No starter code used.
Date: November 22, 2026
"""

import matplotlib.pyplot as plt


# Part 1: Plot the first 5 cubes
x_values = [1, 2, 3, 4, 5]
y_values = [1, 8, 27, 64, 125]

plt.plot(x_values, y_values)
plt.title("First 5 Cubes")
plt.xlabel("Value")
plt.ylabel("Cube of Value")
plt.grid(True)

plt.savefig("cubes_5.png")
plt.close()

