import pandas as pd
#******Series*******************
data = [1, 3, 5, 7, 9]
s = pd.Series(data)
print(s)
#***********dataframe*************
data={ 'name':['neha','swati','tazeen'],
      'age':['30','29','50'],
      'salary':['1L','50K','70K']}
df=pd.DataFrame(data)
print(df)
#*******Empty dataframe
df1=pd.DataFrame()
df1=df
print(df)
# Create an empty DataFrame with column names
empty_df_with_columns = pd.DataFrame(columns=['Name', 'Age', 'City'])
print(empty_df_with_columns)
# Create an empty DataFrame with an index
empty_df_with_index = pd.DataFrame(index=['Row1', 'Row2'])
print(empty_df_with_index)
# Create an empty DataFrame with columns and index
empty_df_with_columns_and_index = pd.DataFrame(columns=['Name', 'Age', 'City'], index=['Row1', 'Row2'])
print(empty_df_with_columns_and_index)
# Create an empty DataFrame with columns
df = pd.DataFrame(columns=['Name', 'Age', 'City'])

# Add a new row to the DataFrame
df.loc[0] = ['Alice', 25, 'New York']
df.loc[1] = ['Bob', 30, 'Los Angeles']

print(df)

#***********readcsv file****
