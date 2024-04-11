import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats


# Custom CSS styling
custom_css = """
<style>
/* Add your CSS rules here */
body {
    font-family: Arial, sans-serif;
    background-color: #f7f7f7;
    color: #808080;
}

.sidebar .sidebar-content {
    background-color: #f7f7f7;
    
}

.stButton>button {
    color: #ffffff !important;
    background-color: #ff9900 !important;
    border-radius: 5px;  /* No change needed */
    padding: 10px 20px;
    font-size: 16px;
    font-weight: bold;
    border: none;
}

.stButton>button:hover {
    background-color: #ff8000 !important;
}

h1, h2, h3, h4, h5 {
    color: #808080;
}

.chart-container {
    background-color: #ffffff;
    border-radius: 10px;  /* No change needed */
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    padding: 20px;
    margin-bottom: 20px;
}

.chart-title {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 20px;
}


.header {
    background-color: #232f3e;
    color: #fff;
    padding: 20px;
    text-align: center;
}

.stDataFrame {
    border: none;
}

.main-content {
    margin: 20px;
    padding: 20px;
    background-color: #fff;
    border-radius: 5px;
}
</style>
"""

# Inject custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Custom HTML structure
custom_html = """
<div>
    <h1 style="text-align: center; color: #ff9900;">Amazon Sales Dashboard</h1>
    <div class="chart-container">
        <h2 class="chart-title">Sales Performance Over Time</h2>
        <!-- Line chart will be displayed here -->
    </div>
</div>
"""

# Inject custom HTML
st.markdown(custom_html, unsafe_allow_html=True)

# app.py content (excluding custom CSS and HTML)

# Load the dataset
df = pd.read_csv('/Users/sakshikarande/cc_miniproject/dataset/shopping_trends_updated.csv')

# Set page title
st.title('Customer Shopping Trends Dashboard')

# Display the first few rows of the dataset
st.subheader('Dataset Overview')
st.write(df.head())

# Add a section for data visualization
st.subheader('Data Visualization')

# Filter data based on age range and gender
min_age = st.sidebar.slider('Minimum Age', min_value=df['Age'].min(), max_value=df['Age'].max(), value=df['Age'].min())
max_age = st.sidebar.slider('Maximum Age', min_value=df['Age'].min(), max_value=df['Age'].max(), value=df['Age'].max())
selected_gender = st.sidebar.selectbox('Select Gender', ['All'] + df['Gender'].unique().tolist(), index=0)

filtered_df = df.copy()
if selected_gender != 'All':
    filtered_df = filtered_df[filtered_df['Gender'] == selected_gender]
filtered_df = filtered_df[(filtered_df['Age'] >= min_age) & (filtered_df['Age'] <= max_age)]

# Display filtered data
st.subheader('Filtered Data')
st.write(filtered_df)

# Display a histogram of customer ages using matplotlib
st.subheader('Distribution of Customer Age')
fig, ax = plt.subplots()
ax.hist(filtered_df['Age'], bins=20, color='skyblue', edgecolor='black')
st.pyplot(fig)

# Display a countplot for gender distribution
st.subheader('Distribution of Gender')
st.bar_chart(filtered_df['Gender'].value_counts())

# Display a countplot for item purchased
st.subheader('Most Popular Items Purchased')
st.bar_chart(filtered_df['Item Purchased'].value_counts())

# Display a countplot for category
st.subheader('Most Popular Categories Purchased')
st.bar_chart(filtered_df['Category'].value_counts())

# Additional Visualizations
st.subheader('Additional Visualizations')

# Scatter Plot of Purchase Amount vs. Age
scatter_fig, scatter_ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=filtered_df, x='Age', y='Purchase Amount (USD)', hue='Gender', palette='Set2', ax=scatter_ax)
scatter_ax.set_xlabel('Age')
scatter_ax.set_ylabel('Purchase Amount (USD)')
scatter_ax.set_title('Purchase Amount vs. Age')
st.pyplot(scatter_fig)

# Line Chart of Purchase Amount over Time
line_fig, line_ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=filtered_df, x='Customer ID', y='Purchase Amount (USD)', marker='o', ax=line_ax)
line_ax.set_xlabel('Customer ID')
line_ax.set_ylabel('Purchase Amount (USD)')
line_ax.set_title('Purchase Amount over Time')
st.pyplot(line_fig)


# Pie Chart of Subscription Status
subscription_counts = filtered_df['Subscription Status'].value_counts()
pie_fig, pie_ax = plt.subplots(figsize=(8, 8))
pie_ax.pie(subscription_counts, labels=subscription_counts.index, autopct='%1.1f%%', startangle=140)
pie_ax.set_title('Subscription Status')
st.pyplot(pie_fig)

# Statistical Analysis
st.subheader('Statistical Analysis')

# Summary Statistics
st.write('Summary Statistics:')
st.write(filtered_df.describe())

# Correlation Matrix
st.write('Correlation Matrix:')
numeric_df = filtered_df.select_dtypes(include=[np.number])
correlation_matrix = numeric_df.corr()
st.write(correlation_matrix)


# Hypothesis Testing (example: t-test for Purchase Amount between genders)
st.subheader('Hypothesis Testing: T-test for Purchase Amount between Genders')

# Separate data by gender
male_purchase_amount = filtered_df[filtered_df['Gender'] == 'Male']['Purchase Amount (USD)']
female_purchase_amount = filtered_df[filtered_df['Gender'] == 'Female']['Purchase Amount (USD)']

# Perform t-test
t_statistic, p_value = stats.ttest_ind(male_purchase_amount, female_purchase_amount)
st.write('T-statistic:', t_statistic)
st.write('P-value:', p_value)

# Interpretation
if p_value < 0.05:
    st.write('There is a significant difference in purchase amount between genders.')
else:
    st.write('There is no significant difference in purchase amount between genders.')

st.title('Data Insights')

# Write your insights using markdown syntax
st.markdown("""
### Insights:
- The distribution of customer age shows a peak around the 40-50 age range, indicating that the majority of customers fall within this age group.
- Gender distribution indicates a relatively equal representation of male and female customers.
- Purchase amount distribution is right-skewed, suggesting that most purchases are of lower amounts, with few high-value purchases.
- The most popular items purchased include [list of popular items].
- [Additional insights based on your analysis]
""")


