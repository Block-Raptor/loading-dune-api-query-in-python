# -*- coding: utf-8 -*-

from dune_client.client import DuneClient
from dune_client.query import QueryBase
from dune_client.types import QueryParameter
import pandas as pd
import matplotlib.pyplot as plt
import creds

    
dune = DuneClient(api_key=creds.api_key)
   
query = QueryBase(
    query_id=5800764)


df = dune.run_query_dataframe(query=query)

#show first 5 values in the dataset
print(df.head())

#check datatypes of column
print(df.dtypes)

#as total_volume_usd is showing in exponential e.g. 4.563793e+07, let's convert to integer
df['total_volume_usd'] = df['total_volume_usd'].astype('int64') 

print(df.head())

avg_volume = df['total_volume_usd'].mean()
print(f"Average Daily Volume: ${avg_volume:,.2f}")

#basic plot
df['day']=pd.to_datetime(df['day'])
print(df.dtypes)

#aspect ratio of plot
plt.figure(figsize=(10,5))
#columns to plot
plt.plot(df['day'],df['total_volume_usd'])
#plot title
plt.title('Balancer Daily Trading Volume - last 7 D')
#axis labels for x and y axis
plt.xlabel('Date')
plt.ylabel('Volume USD')
#show y axis labels in regular number, not exponential
plt.ticklabel_format(style='plain', axis='y')

plt.grid(True)
#adjust spacing between elements in case
plt.tight_layout()
#display plot
plt.show()
