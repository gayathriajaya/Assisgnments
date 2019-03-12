import csv
import pandas
loc='C:\\Users\\gajaya.SAPIENT\\Desktop\\ggggg.csv'
'''
with open(loc) as csv_file:
    csv_reader =csv.reader(csv_file,delimiter=',')
    for row in csv_reader:
        print(row)
'''
df=pandas.read_csv(loc)
print(df.head())
print(df.columns)
df['SUM']=df['tiv_2011']+df['tiv_2012']
print(df.head())
df1=df.pivot(index='policyID',columns='county',values='construction')
print(df1.head())
df2=df.melt(id_vars='policyID',value_vars=['statecode','county'],value_name='values')
print(df2.head())