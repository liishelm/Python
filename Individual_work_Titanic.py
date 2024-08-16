#13.07.2024 Python individual work - learning from Titanic disaster

import pandas as pd
import matplotlib.pyplot as plt

#Exploratory Data Analysis (EDA):
df = pd.read_csv('/content/train.csv')
#Display the first 3 rows
df.head(3)
#Display sample of random 3 rows
df.sample(3)
#number of rows and columns
row, col = df.shape
print(f'There is {row} rows and {col} columns in the dataframe.')
#How many missing values are there by column
print("Missing values per column:\n", df.isnull().sum())
#fill the cells with missing values with 0
df_filled = df.fillna(0)
#Compute basic statistics (e.g., mean, median, min, max) for Age column
mean_age = df["Age"].mean().round(2)
median_age = df["Age"].median()
min_age = df["Age"].min()
max_age = df["Age"].max()
print(f'Mean age: {mean_age}')
print(f'Median age: {median_age}')
print(f'Min age: {min_age}')
print(f'Max age: {max_age}')  
#Analyze categorical variables
gender_counts = df['Sex'].value_counts()
print("Gender counts:\n", gender_counts)
class_counts = df['Pclass'].value_counts()
print("Class counts:\n", class_counts)

#Data Visualization:
#Create a pie chart to visualize the proportion of different traveler classes.
plt.pie(class_counts, labels=class_counts.index, autopct='%1.1f%%')
plt.title('Class Distribution')
plt.show()
#Create histogramm to visualize the age distribution of travelers.
plt.hist(df['Age'], bins=15, color='skyblue', edgecolor='black', alpha=0.7)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')
plt.show()
