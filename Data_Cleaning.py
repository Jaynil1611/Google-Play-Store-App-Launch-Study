import numpy as np
import pandas as pd  
app = pd.read_csv('App_data.csv')
review = pd.read_csv('user_reviews.csv')
print(app.shape)
app.head()

print(review.shape)
review.head()

print(app.isnull().sum())
print(review.isnull().sum())
review_cleaned = review.dropna(0)

print(review_cleaned.isnull().sum())
print(review_cleaned.dtypes)
# review_cleaned.shape

app['Rating'] = app['Rating'].fillna(round(np.mean(app['Rating']),2))

app.dropna(0,inplace=True)
print(app.isnull().sum())
print(app.shape)
app['Installs'] = app['Installs'].str.strip('+')
app['Installs'] = app['Installs'].str.replace(',','')
app['Installs'] = app['Installs'].astype(int)
# CLEANING DATA FOR COLUMN 'Price'
app['Price'] = app['Price'].astype(str)
app['Price'] = app['Price'].apply(lambda x: x.replace('$', ''))
app['Price'] = app['Price'].astype(float)

# Converting the last Updated column in the form 01-02-2003
app['Last Updated'] = app['Last Updated'].astype('datetime64[ns]')
app['Year'] = pd.DatetimeIndex(app['Last Updated']).year
app['Month'] = pd.DatetimeIndex(app['Last Updated']).month

app['Reviews'] = app['Reviews'].astype(int)
print(app.dtypes)

review_cleaned.to_excel('user_review_cleaned.xlsx',index=False)
app.to_excel('app_data_cleaned.xlsx',index=False)
