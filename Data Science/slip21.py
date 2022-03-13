# Write a Python program to find the shape, size, datatypes of the dataframe object. 
# importing pandas module
import pandas as pd

# making data frame
data = pd.read_csv("iris.csv")

# dataframe.size
size = data.size

# dataframe.shape
shape = data.shape

#Type of dataframe
Type= type(data)

print(type(data))
# printing size and shape
print("Size = {}\nShape ={}\n Type = {}".format(size, shape,Type ))
