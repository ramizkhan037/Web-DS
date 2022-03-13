# Write a Python program to create a dataframe containing columns name, age and percentage.
#  Add  10 rows to the dataframe. View the dataframe. 
import pandas as pd
import numpy as np

exam_data  = {'Name': ['Sajid', 'Yasin', 'Sahil', 'Sameer', 'Arif', 'Alfia', 'Tayyaba', 'Muskaan', 'Rohit', 'Rashmi'],
        'Age': [21, 18, 19, 18, 19, 20, 17, 22, 19, 27],
        'Percentage': [70, 83, 70, 63, 72, 83, 51, 71, 62, 81]}
labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

df = pd.DataFrame(exam_data , index=labels)
print(df)