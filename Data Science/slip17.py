# Import pandas library
import pandas as pd
import numpy as np
# List of Tuples
employees = [('Stuti', 28, 'Varanasi'),
			('Saumya', 32, 'Delhi'),
			('Aaditya', 25, 'Mumbai'),
			('Saumya', 32, 'Delhi'),
			('Saumya', np.nan, 'Delhi'),
			('Saumya', 32, 'Mumbai'),
			('Aaditya', 40, np.nan),
			('Seema', 32, 'Delhi')
			]

df = pd.DataFrame(employees)


print(df.info)