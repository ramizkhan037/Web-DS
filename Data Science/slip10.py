import pandas as pd
import numpy as np
employees = [('Stuti', 28, np.nan,),
			('Saumya', 32, 20000,),
			('Aaditya', 25, 15000,),
			('Saumya', 32, np.nan,),
			('Saumya', np.nan, 10000,),
			('Saumya', np.nan, 8000,),
			('Aaditya', 40, np.nan),
			('Seema', 32, np.nan,)
			]

df = pd.DataFrame(employees,
				columns = ['Name', 'Age', 'City'])
New = df.fillna(df.mean())
print(New)