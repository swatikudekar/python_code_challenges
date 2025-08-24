import pandas as pd
import os
import datetime
import sys
import openpyxl
df=pd.read_excel(r"D:\MHRIL_SOFI_Data\Consumption_Report\Consumption Report_December_2024.xlsx",header=[0],usecols=[0,1,2,3,4,5])
df.to_excel("D:\MHRIL_SOFI_Data\Consumption_Report\out.xlsx",index=False)
print(df.columns)
print(df.info())
print(df.describe())
df1=df.groupby('Plnt')[' Amount in LC'].sum().reset_index()
df1.to_excel("D:\\MHRIL_SOFI_Data\\Consumption_Report\\output.xlsx",index=False)
print(df1.head())
print(df1.tail())
count1=df.value_counts()
print(count1)
print(df.size)

print(df1.shape)
exit()
print(df.iloc[5,5])
print(df1.iloc[2:4,0])

