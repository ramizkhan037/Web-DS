import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4])
y = x*x

# first plot with X and Y data
plt.plot(x, y)

x1 = ["Sajid", "Yasin", "Sahil", "Sameer"]
y1 = [83, 75, 67, 79]

# second plot with x1 and y1 data
plt.plot(x1, y1, '-.')

plt.xlabel("Name")
plt.ylabel("Percentage")
plt.show()
