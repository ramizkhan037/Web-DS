#  Write a Python program to get the number of observations, missing values and nan values. 

import pandas as pd
iris = pd.read_csv("iris1.csv")
print(iris.info())