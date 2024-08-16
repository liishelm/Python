#13.07.2024 Python individual work - learning from Titanic disaster

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/content/train.csv')
df.head(3)
df.sample(3)
row, col = df.shape
print(f'There is {row} rows and {col} columns in the dataframe.')
print("Missing values per column:\n", df.isnull().sum())
df_filled = df.fillna(0)
mean_age = df["Age"].mean().round(2)
median_age = df["Age"].median()
min_age = df["Age"].min()
max_age = df["Age"].max()
print(f'Mean age: {mean_age}')
print(f'Median age: {median_age}')
print(f'Min age: {min_age}')
print(f'Max age: {max_age}')  
gender_counts = df['Sex'].value_counts()
print("Gender counts:\n", gender_counts)
class_counts = df['Pclass'].value_counts()
print("Class counts:\n", class_counts)
plt.pie(class_counts, labels=class_counts.index, autopct='%1.1f%%')
plt.title('Class Distribution')
plt.show()
plt.hist(df['Age'], bins=15, color='skyblue', edgecolor='black', alpha=0.7)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')
plt.show()
