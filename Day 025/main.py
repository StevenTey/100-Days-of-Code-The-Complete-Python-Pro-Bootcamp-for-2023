import pandas as pd

data = pd.read_csv('Squirrel_Data.csv')

# print(data.columns)

df = data[['Primary Fur Color', 'Unique Squirrel ID']]

df_g = df.groupby('Primary Fur Color').count()

df_g = df_g.rename(columns={'Unique Squirrel ID': 'Count', 'Primary Fur Color': 'Fur Color'})
df_g.sort_values(by='Count', ascending=False, inplace=True)

df_g.to_csv('squirrel_count.csv')