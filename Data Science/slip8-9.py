# Create own dataset and do simple preprocessing 
# Dataset Name: Data.CSV (save following data in Excel and save it with .CSV extension) Country, Age, Salary, Purchased 
# France, 44, 72000, No 
# Spain, 27, 48000, Yes 
# Germany, 30, 54000, No 
# Spain, 38, 61000, No 
# Germany, 40, , Yes 
# France, 35, 58000, Yes 
# Spain, 52000, No 
# France, 48, 79000, Yes 
# Germany, 50, 83000, No 
# France, 37, 67000, Yes 

# Q1) Describing the dataset 
import numpy as np 
import pandas as pd 
df=pd.read_csv('Data.csv') 
print(df.describe())  




# Q2 shape of data set
import numpy as np 
import pandas as pd 
df=pd.read_csv('Data.csv') 
print(df.shape)


# Q3
print(df.head(3))