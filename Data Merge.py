import pandas as pd
import uuid
file_1='EV_population_WA_cleaned.csv'
file_2='WA_Charging_Stations.csv'
df_pop=pd.read_csv(file_1)
df_chr=pd.read_csv(file_2)


df_pop=df_pop.rename(columns={'Zip':'ZIP'})
print(df_pop.columns)
print(df_chr.columns)

df_chr['ID'] = [str(uuid.uuid4()) for _ in range(len(df_chr))]
print(df_chr.columns)


grouped_pop = df_pop.groupby('ZIP')['EV_ID'].count().reset_index()

grouped_chr = df_chr.groupby('ZIP')['ID'].count().reset_index()


df=pd.merge(grouped_pop,grouped_chr,how='outer',on='ZIP')
print(df)
df.to_csv('testing_1.csv',index=False, header=True)
