import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(color_codes=True)

df = pd.read_csv('data/data.csv')
# To display the top 5 rows
df.head(5)
df.dtypes
df = df.rename(columns={'Engine HP': 'HP', 'Engine Cylinders': 'Cylinders',
                        'Transmission Type': 'Transmission',
                        'Driven_Wheels': 'Drive Mode',
                        'highway MPG': 'MPG-H', 'city mpg': 'MPG-C',
                        'MSRP': 'Price'})

df.shape
duplicate_rows_df = df[df.duplicated()]
print('number of duplicate rows: ', duplicate_rows_df.shape)

df.count()

df = df.drop_duplicates()

df.count()
