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

# Finding the null values.
print(df.isnull().sum())

df = df.dropna()
df.count()

# After dropping the values
print(df.isnull().sum())

sns.boxplot(x=df['Price'])

sns.boxplot(x=df['HP'])

sns.boxplot(x=df['Cylinders'])

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
print(IQR)

df = df[~((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=1)]
df.shape

df.Make.value_counts().nlargest(40).plot(kind='bar', figsize=(10,5))
plt.title('Number of cars by make')
plt.ylabel('Number of cars')
plt.xlabel('Make')

# Finding the relations between the variables.
plt.figure(figsize=(20,10))
c= df.corr()
sns.heatmap(c,cmap='BrBG',annot=True)

# Plotting a scatter plot
fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(df['HP'], df['Price'])
ax.set_xlabel('HP')
ax.set_ylabel('Price')
plt.show()