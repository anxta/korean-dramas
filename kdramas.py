# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 11:10:24 2023

@author: anamo
"""
#%% 
# Importing libraries

import seaborn as sns
import numpy as np
import seaborn as sns 
import pandas as pd
import matplotlib.pyplot as plt


#Understanding Data and DatFrames
import pandas as pd
df_kdrama= pd.read_csv('C:/Users/anamo/Downloads/Korean Dramas/korean_drama.csv')
print(df_kdrama.head())
df_kdrama.info()
df_kdrama.describe()

#checking individual values 
print(df_kdrama.isna())
print(df_kdrama.isna().sum())
# Filing 0 non values 
df_kdrama.fillna(0)


df_review= pd.read_csv('C:/Users/anamo/Downloads/Korean Dramas/reviews.csv')
#checking individual values 
print(df_review.isna())
print(df_review.isna().sum())
# Filing 0 non values 
df_review.fillna(0)


# Plot 1: 10 Kdramas with longer duration
drama_sorted= df_kdrama.sort_values("duration", ascending= False)
drama10= drama_sorted.iloc[0:10]
sns.barplot(data= drama10, x="duration", y= "drama_name", palette= "magma")
plt.title("10 Kdramas with longer duration")
plt.ylabel("Name")
plt.xlabel("Duration")
plt.show()

#Plot 2 Top 10 Kdramas with the hightest overall score
overall_sorted= df_review.sort_values("overall_score", ascending= False)
overall= overall_sorted.iloc[0:10]
sns.barplot(data= overall, x= "overall_score", y= "title", palette= "mako")
plt.xlabel("Overall score")
plt.ylabel("Title")
plt.title("Top 10 Kdramas with the hightest overall score")
plt.show()

#Plot 3 "Amount of Kdramas (2015-2023)"
amount= df_kdrama["year"].value_counts()
print(amount)
sns.lineplot(data= amount)
sns.set_style(rc = {'axes.facecolor': 'lightsteelblue'})
plt.xlabel("Years")
plt.ylabel("Amount")
plt.title("Amount of Kdramas (2015-2023)")
plt.show()

