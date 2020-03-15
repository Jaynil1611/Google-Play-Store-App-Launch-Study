import matplotlib.pyplot as plt
import pandas as pd
import pymysql
import numpy as np
import statistics  
import warnings 
warnings.filterwarnings('ignore')
df = pd.read_excel('C:\\Users\\Jaynil Gaglani\\Machine_Learning_Coding_Track_Module_5\\Datasets_Python_Project\\app_data_cleaned.xlsx',header=0)
df['Rating'] = df['Rating'].astype(float)
free = df[df['Type']=='Free']
d = free[['Rating','Installs']]
frees = {}
 
def normalize(df):
    result = df.copy()
    for feature_name in df.columns:
        max_value = df[feature_name].max()
        min_value = df[feature_name].min()
        result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
    return result
d = normalize(d)
# print(d.head())
for i in range(len(d)):
    frees[free['App'].iloc[i]] = statistics.mean(d.iloc[i,:])
Maxfree = sorted(frees, key=frees.get, reverse=True)[:5]
# print(Maxfree)

paid = df[df['Type']=='Paid']
d1 = paid[['Rating','Installs']]
paids = {}
d1 = normalize(d1)
for i in range(len(d1)):
    paids[paid['App'].iloc[i]] = statistics.mean(d1.iloc[i,:])
Maxpaid = sorted(paids, key=paids.get, reverse=True)[:5]
# print(Maxpaid)

review_df = pd.read_csv('C:\\Users\\Jaynil Gaglani\\Machine_Learning_Coding_Track_Module_5\\Datasets_Python_Project\\user_review_cleaned.csv',header=0)
df2 = review_df.groupby('App')['Sentiment_Polarity','Sentiment_Subjectivity'].mean()
# print(df2.head())
d3 = df2[['Sentiment_Polarity','Sentiment_Subjectivity']]
trends = {}
for i in range(len(d3)):
    trends[df2.index[i]] = statistics.mean(d3.iloc[i,:])
Trending = sorted(trends, key=trends.get, reverse=True)[:5]
# print(Trending)