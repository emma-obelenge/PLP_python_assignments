
# Analyzing Data with Pandas and Visualizing Results with Matplotlib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the random seed for reproducibility
np.random.seed(42)

# Created a mock dataset similar to the Iris dataset
species = ['setosa', 'versicolor', 'virginica']
data = {
    'sepal_length': np.random.normal(loc=5.8, scale=0.5, size=150),
    'sepal_width': np.random.normal(loc=3.0, scale=0.3, size=150),
    'petal_length': np.random.normal(loc=3.7, scale=1.5, size=150),
    'petal_width': np.random.normal(loc=1.2, scale=0.5, size=150),
    'species': np.random.choice(species, size=150)
}

df = pd.DataFrame(data)

# Display first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Check data types and missing values
print("\nDataset Information:")
print(df.info())
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# Task 2: Basic Data Analysis
print("\nBasic Statistics:")
print(df.describe())

# Group by species and compute mean
grouped = df.groupby('species').mean()
print("\nAverage Measurements by Species:")
print(grouped)

# Task 3: Data Visualization

# Line Chart - Mean Sepal Length per Species
grouped['sepal_length'].plot(kind='line', marker='o')
plt.title('Average Sepal Length by Species')
plt.xlabel('Species')
plt.ylabel('Sepal Length (cm)')
plt.grid(True)
plt.tight_layout()
plt.show()

# Bar Chart - Average Petal Width by Species
grouped['petal_width'].plot(kind='bar', color='skyblue')
plt.title('Average Petal Width by Species')
plt.ylabel('Petal Width (cm)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Histogram - Distribution of Petal Length
plt.hist(df['petal_length'], bins=20, color='green', edgecolor='black')
plt.title('Distribution of Petal Length')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Scatter Plot - Sepal Length vs. Petal Length
sns.scatterplot(x='sepal_length', y='petal_length', hue='species', data=df)
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.tight_layout()
plt.show()
