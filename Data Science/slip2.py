# Write a Python program to print the shape, number of rows-columns, 
# data types, feature names  and the description of the data 
import pandas as pd
data = pd.read_csv("iris.csv")
print("Shape of the data:")
print(data.shape)
print("\nData Type:")
print(type(data))
print("\nFirst 6 rows:")
print(data.head(6))