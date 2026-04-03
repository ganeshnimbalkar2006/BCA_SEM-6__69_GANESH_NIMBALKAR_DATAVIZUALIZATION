import pandas as pd
df=pd.read_csv("C:/Users/nimba/Downloads/archive/Smartphone_Usage_Productivity_Dataset_50000.csv")
print("first 10 rescords",df.head(10))#to print first 5 rows of data  
print("-----------------------------------------        -----------------------------")
print("last 10 records",df.tail(10))#to print last 5 rows of data 

print("----------------------")
print("columns in dataset::",df.columns)#to print columns in dataset
print("--------------------------------------")
print("number of rows and columns::",df.shape)#to print number of rows and columns
print("--------------------------------------")
print("data types of columns::",df.dtypes)#to print data types of columns
print("--------------------------------------")
print("number of missing values in each column::",df.isnull().sum())#to print number of missing values in each column
print("--------------------------------------")
print("random 20 records:",df.sample(20))
print("--------------------------------------  ")
print("statistical summary of dataset::",df.describe())#to print statistical summary of dataset
print("--------------------------------------")
print("------------------------")

new_col=df["Health"]="Good"#to add new column health with value good
print(new_col)
print(df["Health"])