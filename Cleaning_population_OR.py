import pandas as pd
file='EV_population_OR.csv'
OR_1=pd.read_csv(file)

print(OR_1.info())
Unique_value_count=OR_1['Index_'].nunique()
print(Unique_value_count)

#select columns
OR_2=OR_1[['Make','Model','City','Zip','State','Index_']]
print(OR_2.columns)

#select OR, Portland
OR_3=OR_2[OR_2['State']=='OR']
OR_4=OR_3[OR_3['City']=='PORTLAND']
print(OR_4['State'].unique())
print(OR_4['City'].unique())
print(OR_4.info())

#dropduplicae and NA
OR_5=OR_4.drop_duplicates()
OR_6=OR_5.dropna(subset=['Index_'])
print(OR_6.info())

OR_final=OR_6.rename(columns={'Index_':'EV_ID'})
print(OR_final.info())

OR_final['Zip']=OR_final['Zip'].astype(str)
OR_final['EV_ID']=OR_final['EV_ID'].astype(str)
print(OR_final.dtypes)


#export
OR_final.to_csv('EV_population_OR_cleaned.csv',index=False,header=True)
