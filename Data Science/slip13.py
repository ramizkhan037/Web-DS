# Create two lists, one representing subject names and the other representing marks obtained in those subjects. Display the data in a pie chart and bar chart. 
import matplotlib.pyplot as plt
import numpy as np
# Creating dataset
name = ['Sajid', 'Yasin', 'Sahil',
        'Sameer', 'Arif']
 
marks = [83, 71, 56, 79, 72]
 
# Creating plot
fig = plt.figure(figsize =(10, 7))
plt.pie(marks, labels = name)
 
# show plot
plt.show()


# creating the bar plot
plt.bar(name, marks, color ='maroon',
        width = 0.4)
 
plt.xlabel("Name")
plt.ylabel("Marks")
plt.title("Bar Chart")
plt.show()