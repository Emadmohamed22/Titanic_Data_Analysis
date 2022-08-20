from asyncore import read
import imp
from operator import ge
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

# data analyzing
print(df['sex'].value_counts())
print(df['pclass'].value_counts())

# analyzing percentge of survived for men and women
for gen in df['sex'].unique() :
    print(gen)
    gender_df = df[df['sex']==gen]
    survived = gender_df[gender_df['survived']==1]
    survived_percentage = (survived.shape[0] / gender_df.shape[0]) * 100
    print("count of : " , gender_df.shape[0])
    print("servived : ","%.2f" % survived_percentage , '%')
    print("\n=====\n")

# Dictionary to define class catagories

class_dict = {
    1:"class A",
    2:"class B",
    3:"class C"
}

# analyzing percentge of survived for pclass
for x_class in df['pclass'].unique() :
    print(class_dict[x_class])
    pclass_df = df[df['pclass']==x_class]
    sur_class = pclass_df[pclass_df['survived']==1]
    sur_percentage = (sur_class.shape[0] / pclass_df.shape[0])*100
    print("count of : " , pclass_df.shape[0])
    print("servived : ","%.2f" % sur_percentage , '%')
    print("\n=====\n")

# function to convert age to catagories
def age_to_catagory(age) : 
    if age < 4 :
        return 0 #baby
    elif age < 10 :
        return 1 #child
    elif age < 21 :
        return 2 #teen
    elif age < 33 :
        return 3 #young adult
    elif age < 50 :
        return 4 #elder
    return 5 #elder

# Dictionary to define age catagories
age_cats_dict = {
    0:"baby",
    1:"child",
    2:"teen",
    3:"young adult",
    4:"adult",
    5:"elder"
} 
# Create a new column to classify ages
df['age_cat'] = df['age'].apply(age_to_catagory)

# analyzing percentge of survived for each age
for a in df['age_cat'].unique():
    print(age_cats_dict[a])
    age_df =df [df['age_cat']==a]
    age_sur_df = age_df[age_df['survived']==1]
    sur_percentage_age = (age_sur_df.shape[0] / age_df.shape[0])*100
    print("count of : " , age_df.shape[0])
    print("servived : ","%.2f" % sur_percentage_age , '%')
    print("\n=====\n")

