import pandas as pd
 
data = [
  { 'h': 1.80, 'w': 80 },
  { 'h': 1.70, 'w': 90 },
  { 'h': 1.60, 'w': 60 },
]
 
df = pd.DataFrame(data)
print(df)
print("------------------")
 
def BMI(data):
    return data['w'] / data['h']**2
 
df['bmi'] = df.apply(BMI, axis=1)
print(df)
print("Maximum BMI:\n")
print(df.max())
print("Minimum BMI:\n")
print(df.min())