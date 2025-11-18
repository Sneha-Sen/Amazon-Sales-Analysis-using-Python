import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('Amazon Sale Report.csv')
#print(df.head())
#print(df.shape)
#print(df.tail())
#print(df.info())
df.drop(['New','PendingS'], axis=1, inplace=True)
#print(df.info())
#print(df.isnull().sum())
df.dropna(inplace=True)
#print(df.shape)
#print(df.columns)
# change data type
df['ship-postal-code']=df['ship-postal-code'].astype('int')
#print(df.info())
df['Date']=pd.to_datetime(df['Date'])
#rename Columns
df.rename(columns={'Qty':'Quantity'})
#print(df.columns)

#print(df.describe())

#ax=sns.countplot(x='Size' ,data=df)
#for bars in ax.containers:
#    ax.bar_label(bars)
#plt.show()
#most of the people buys M-Size

grouped_data= df.groupby(['Size'], as_index=False)['Qty'].sum().sort_values(by='Qty',ascending=False)
#print(grouped_data)
#sns.barplot(x='Size',y='Qty', data=grouped_data)
#plt.show()
#most of the Qty of M-Size is bought in the sales

plt.figure(figsize=(10,5))
#sns.countplot(data=df, x='Courier Status',hue= 'Status')
#plt.show()
#the majority of the orders are shipped through the courier

#df['Size'].hist() 
#plt.show()

df['Category'] = df['Category'].astype(str)
plt.figure(figsize=(10, 5))
#plt.hist(df['Category'], bins=30, edgecolor='Black')
#plt.xticks(rotation=90)
#plt.show()
#that most of the buyers buy T-shirt

B2B_Check = df['B2B'].value_counts()
#plt.pie(B2B_Check, labels=B2B_Check, autopct='%1.1f%%')
#plt.show()
#maximum i.e. 99.3% of buyers are retailers and 0.7% are B2B buyers

x_data = df['Category']  
y_data = df['Size'] 
#plt.scatter(x_data, y_data)
plt.xlabel('Category')  
plt.ylabel('Size')  
plt.title('Scatter Plot') 
#plt.show()

# top_10_States 
top_10_state = df['ship-state'].value_counts().head(10)
plt.figure(figsize=(12, 6))
sns.countplot(data=df[df['ship-state'].isin(top_10_state.index)], x='ship-state')
plt.xlabel('ship-state')
plt.ylabel('count')
plt.title('Distribution of  State')
plt.xticks(rotation=45)
plt.show()
#most of the buyers are from Maharashtra state