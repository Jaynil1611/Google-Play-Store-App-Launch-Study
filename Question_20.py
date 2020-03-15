import matplotlib.pyplot as plt
import pandas as pd
a=pd.read_excel('C:\\Users\\Jaynil Gaglani\\Machine_Learning_Coding_Track_Module_5\\Datasets_Python_Project\\app_data_cleaned.xlsx',header=0)
x=a[['Category','App','Rating','Installs','Size','Content Rating','Type']]
cat =a['Category'].unique()
cat=cat.tolist()
d1={}
d2={}
for i in cat:
    d1[i]=[0]*5
z=x.to_dict(orient='split')
for i in cat:
    c=0
    for j in range(len(x)):
        if(i==z['data'][j][0]):
            d1[i][c]=z['data'][j][1]
            c+=1
            if(c==5):
                break
for i in cat:
  d2[i] = {}
  for j in d1[i]:      #app name in i cat
     d2[i][j] = [0]*5  #app of that cat list of 5

for i in d2.keys():
    for j in d2[i].keys():
      for k in range(len(x)):
        if(i==z['data'][k][0] and j==z['data'][k][1]):
            d2[i][j][0]=z['data'][k][2]
            d2[i][j][1]=z['data'][k][3]
            d2[i][j][2]=z['data'][k][4]
            d2[i][j][3]=z['data'][k][5]
            d2[i][j][4]=z['data'][k][6]
