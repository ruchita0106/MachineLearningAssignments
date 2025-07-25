import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("used_cars_data.csv")

#print first 10 records
print(data.head(10))

#print last 10 records
print(data.tail(10))

print(data.info())

print(data.nunique())
print(data.isnull().sum())
print((data.isnull().sum()/(len(data)))*100)

#remove the column which is not required
data = data.drop(['S.No.'], axis = 1)
data.info()
print(data.info())

#creating new features
from datetime import date
date.today().year
data['Car_Age']=date.today().year-data['Year']
data.head()
print(data.head(5))

data['Parsing'] = data['Car_Age'].apply(lambda x: 'Reparse' if x > 10 else 'Done')
print(data.head(10))

#spliting
data['Brand'] = data.Name.str.split().str.get(0)
data['Model'] = data.Name.str.split().str.get(1) + data.Name.str.split().str.get(2)
data[['Name','Brand','Model']]

#data cleaning
print(data.Brand.unique())
print(data.Brand.nunique())

searchfor = ['Isuzu' ,'ISUZU','Mini','Land']
data[data.Brand.str.contains('|'.join(searchfor))].head(5)
data.describe().T
data.describe(include='all').T

cat_cols=data.select_dtypes(include=['object']).columns
num_cols = data.select_dtypes(include=np.number).columns.tolist()
print("Categorical Variables:")
print(cat_cols)
print("Numerical Variables:")
print(num_cols)

# Pie chart of Parsing column
parsing_counts = data['Parsing'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(parsing_counts, labels=parsing_counts.index, autopct='%1.1f%%', startangle=140, colors=['#FF9999','#66B3FF'])
plt.title('Parsing Status of Used Cars')
plt.axis('equal')
plt.show()

#bar chart for number of cars per top 10 brands
brand_counts = data['Brand'].value_counts().head(10) 
plt.figure(figsize=(10, 6))
sns.barplot(x=brand_counts.index, y=brand_counts.values, palette='Set2')
plt.title('Top 10 Most Common Car Brands')
plt.xlabel('Brand')
plt.ylabel('Number of Cars')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Histogram for car age
plt.figure(figsize=(8, 5))
plt.hist(data['Car_Age'], bins=15, color='lightgreen', edgecolor='black')
plt.title('Distribution of Car Age')
plt.xlabel('Car Age')
plt.ylabel('Frequency')
plt.show()




