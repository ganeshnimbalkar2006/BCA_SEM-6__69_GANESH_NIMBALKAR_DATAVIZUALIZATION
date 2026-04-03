#Basic statistical operations  1
import pandas as pd


students={
    "name":["a","b","c"],   
    "graduation_percentage":[80,85,90],
    "age":[20,21,22],

}
df=pd.DataFrame(students)#to print first 5 rows of data
print("--------------------------------------")
print(df)
print("--------------------------------------")
print( "to calculate mean(average) of age column::",df["age"].mean())
print("--------------------------------------")
print("#to calculate mean(average) of graduation percentage column:",df["graduation_percentage"].mean()) 
print("--------------------------------------")
print("#describe all basic statistics of data::",df.describe())

print("--------------------------------------")
df=pd.read_csv("C:\Users\nimba\Downloads\archive(1)\IRIS.csv")
print(pd.DataFrame(df))#to print first 5 rows of data
print("--------------------------------------")

print(df.describe())#describe all basic statistics of data
print("--------------------------------------")

print("Mean age::",df[ "Age"].mean())#to calculate mean of age column
print("--------------------------------------")
print("Median Stress_Level::",df["Stress_Level"].median())#to calculate median of stress level column
print("--------------------------------------")
print("range of aage::",df["Age"].max()-df["Age"].min())#to calculate range of age column
print("--------------------------------------")
print("standard deviation::",df["Stress_Level"].std())#to calculate standard deviation of stress level column  

print("--------------------------------------")
print("variance of stress level::",df["Stress_Level"].var())#to calculate variance of stress level column

print("--------------------------------------")
print("random records",df.sample(1000))
print("--------------------------------------   ")    
print(df["Gender"].unique())#to find unique values in gender column
print("--------------------------------------   ")
