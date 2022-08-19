from asyncore import read
import imp
import os
import pandas as pd 
import matplotlib.pyplot as plt


# reading data from titanc dataset 
df = pd.read_excel('titanic.xls')

#verfing data
print(df.head(n=50)) # print first 50 row to verfing data 
dfT = df.shape ; print(dfT) # print total numbers of rows and columns from loaded sheet to verfing it
print(df.columns) # print all columns 

# data panorama 
print(df.info()) # print type and non-null status of columns 
print(df.describe()) # print statistaics for numeric values of columns

# data cleaning
df.drop(['fare','home.dest','name'],axis=1,inplace=True) # deleting data from dataset
df["age"] = df['age'].fillna(0) # fill na cells with 0

# Histogram
df.hist()
plt.show()
