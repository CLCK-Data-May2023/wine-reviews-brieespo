# add your code here

import pandas as pd

reviews = pd.read_csv("data/winemag-data-130k-v2.csv.zip")


df = reviews.groupby('country').agg({'country':'count', 'points':'mean'}).round(1)

df_summary = df.rename(columns = {'country': 'count'})

df_summary = df_summary.sort_values('count', ascending=False) 


df_summary.to_csv('data/reviews-per-country.csv')
