# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 11:10:24 2023

@author: anamo
"""
import seaborn as sns
import numpy as np
import seaborn as sns 
import pandas as pd

df_kdrama= pd.read_csv('C:/Users/anamo/Downloads/Korean Dramas/korean_drama.csv')
print(df_kdrama.head())
df_kdrama.info()
df_kdrama.describe()

import matplotlib.pyplot as plt

#checking individual values 
print(df_kdrama.isna())

print(df_kdrama.isna().sum())


df_kdrama.fillna(0)

drama_sorted= df_kdrama.sort_values("duration", ascending= False)
drama10= drama_sorted.iloc[0:10]
sns.barplot(data= drama10, x="duration", y= "drama_name", palette= "magma")

plt.title("10 Kdramas with longer duration")
plt.ylabel("Name")
plt.xlabel("Duration")
plt.show()

df_review= pd.read_csv('/kaggle/input/korean-drama-2015-23-actor-and-reviewmydramalist/reviews.csv')
print(df_review.head())
df_review.info

# checking each column for missing values 
print(df_review.isna().sum())

overall_sorted= df_review.sort_values("overall_score", ascending= False)
overall= overall_sorted.iloc[0:10]
sns.barplot(data= overall, x= "overall_score", y= "title", palette= "mako")
plt.xlabel("Overall score")
plt.ylabel("Title")
plt.title("Top 10 Kdramas with the hightest overall score")

amount= df_kdrama["year"].value_counts()
print(amount)
sns.lineplot(data= amount)
sns.set_style(rc = {'axes.facecolor': 'lightsteelblue'})
plt.xlabel("Years")
plt.ylabel("Amount")
plt.title("Amount of Kdramas (2015-2023)")



