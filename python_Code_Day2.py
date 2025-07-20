import pandas as pd
#************************************* Dictionary Methods **************************************************************
data={'column1':[1,2,3,4],'column2':['A','B','C','D']}
print(data)
df=pd.DataFrame(data)
print(df)
dict1={}  ##empty dictionay
print(type(dict))

dict1={'A':'red',"B":'pink','C':'yellow','D':'white'} ##assign values to dictionary
df['color']=''
df['color']=df['column2'].map(dict1)  ## use map functions
print(df)
print(df['color']) 
print(dict1['A'])  ##using keys
print(dict1.get('A')) ##use getkey method
dict2=dict1.copy()
print(dict2)
print(dict2.items())
print(dict2.keys())
print(dict2.values())
print(dict2.pop('A'))
print(dict2)
exit()
dict1.clear()   ##delete dictionary


##*********************************************************List methods **************************************************

