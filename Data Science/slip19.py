import matplotlib.pyplot as plt
x= ["Sajid", "Yasin", "Sahil", "Sameer"]
y= [83, 85, 82, 84]
plt.plot(x, y, color="red")  
plt.xlabel("Name")  # add X-axis label
plt.ylabel("percentage")  # add Y-axis label
plt.title("Line Chart")  # add title
plt.show()