# Download iris dataset file. Read this csv file using read_csv() function.
#  Take samples from entire dataset. Display maximum and minimum values of all numeric attributes. 
import pandas as pd
data = pd.read_csv("iris.csv")
df = pd.DataFrame(data)
print("Maximum value :")
print(df.max(data))
print("Minimum value :")
print(df.min(data))