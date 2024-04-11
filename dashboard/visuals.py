import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('/Users/sakshikarande/cc_miniproject/dataset/shopping_trends_updated.csv')

# Display the first few rows of the DataFrame
print(df.head())

# Get information about the dataset
print(df.info())

# Summary statistics of numerical columns
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Handle missing values
df.dropna(inplace=True)

# Handle duplicate entries
df.drop_duplicates(inplace=True)
print(df.isnull().sum())

# Set the style of seaborn plots
sns.set_style('whitegrid')

# 1. Distribution of Customer Age
plt.figure(figsize=(12, 6))
sns.histplot(df['Age'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of Customer Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# 2. Distribution of Gender
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Gender', palette='pastel', hue='Gender', legend=False)
plt.title('Distribution of Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# 3. Purchase Amount Distribution
plt.figure(figsize=(12, 6))
sns.histplot(df['Purchase Amount (USD)'], bins=20, kde=True, color='salmon')
plt.title('Purchase Amount Distribution')
plt.xlabel('Purchase Amount (USD)')
plt.ylabel('Frequency')
plt.show()

# 4. Most Popular Items Purchased
plt.figure(figsize=(12, 6))
sns.countplot(data=df, y='Item Purchased', order=df['Item Purchased'].value_counts().index, palette='pastel', hue='Item Purchased', legend=False)
plt.title('Most Popular Items Purchased')
plt.xlabel('Count')
plt.ylabel('Item Purchased')
plt.show()

# 5. Most Popular Categories Purchased
plt.figure(figsize=(12, 6))
sns.countplot(data=df, y='Category', order=df['Category'].value_counts().index, palette='pastel', hue='Category', legend=False)
plt.title('Most Popular Categories Purchased')
plt.xlabel('Count')
plt.ylabel('Category')
plt.show()

# Repeat the same steps for other visualizations...
