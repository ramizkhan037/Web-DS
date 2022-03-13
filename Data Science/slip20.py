# Write a Python program to generate a scatter plot of name vs percentage 
import matplotlib.pyplot as plt

x = ["Sajid", "Yasin", "Sahil", "Sameer"]
y = [53, 72, 58, 10]
plt.scatter(x, y, color="red")
x1 = ["Sajid", "Yasin", "Sahil", "Sameer"]
y1 = [83, 75, 67, 79]
plt.scatter(x1, y1, color="blue")
plt.show()