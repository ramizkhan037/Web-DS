# Write a Python program to create a Bar plot to get the frequency of the three species of the Iris data. 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
iris = pd.read_csv("iris.csv")
ax=plt.bar(1,1,figsize=(10,8))
sns.countplot('Species',data=iris)
plt.title("Iris Species Count")
plt.show()