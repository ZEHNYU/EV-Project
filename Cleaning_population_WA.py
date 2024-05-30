import pandas as pd
file='EV_popuation_WA.csv'
WA_1=pd.read_csv(file)
print(WA_1.info())

#select columns
WA_2=WA_1[['City','State','Postal Code','Make','Model','DOL Vehicle ID']]
print(WA_2.columns)

#select Seattle
WA_3=WA_2[WA_2['State']=='WA']
WA_4=WA_3[WA_2['City']=='Seattle']

print(WA_4['State'].unique())
print(WA_4['City'].unique())
print(WA_4.info())

print(WA_4.dtypes)
WA_4['DOL Vehicle ID'] = WA_4['DOL Vehicle ID'].astype(str)
print(WA_4.dtypes)

#Drop duplicate
WA_5=WA_4.drop_duplicates(subset=['DOL Vehicle ID'])
print(WA_5.info())

WA_final=WA_5.rename(columns={'DOL Vehicle ID':'EV_ID','Postal Code':'Zip'})
print(WA_final.info())

WA_final.to_csv('EV_population_WA_cleaned.csv',index=False,header=True)
