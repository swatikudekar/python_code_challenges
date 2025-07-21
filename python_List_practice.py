import os
import copy
import pandas as pd
df=pd.read_excel(r"C:\Users\50000517\Documents\python_daily\Superstore_orders.xls",header=[0],usecols=[10],nrows=110)
df.to_excel(r"C:\Users\50000517\Documents\python_daily\output.xlsx",index=False)
print(df.columns)
state_list=list(set(df))  #make list from df
state_lst=df['State'].to_list()#make list from df
cnt=state_lst.count('Indiana')
print("india count==",cnt)
print(list(set(state_lst)))

##### list sorting #############
salary=[1200,2300,3100,4300,3400,500,1780]
salary.remove(1200)

salary.pop(1)
print("list after pop==",salary)
print("list after clear",salary)
high_salary=list(set(salary))
print(high_salary)
high_salary.sort(reverse=True)  ##sorting
print(high_salary)
print(high_salary[1])
list_salary=[5900,1100,3280,4000,3500]
###########indexing ############# start from 0
high_salary.append(5600) ##append anything list or elementat the last
high_salary.extend(list_salary) ##extend list at the end
print(high_salary)
print("list after remove is==",salary)
salary.clear()

#********** copy.deepcopy() method creates a completely independent copy of the original object, including all nested elements. 
# Changes made to deep_copied do not affect the original list a.
#*********in Shallow copy *Changes made to a copy of an object do reflect in the original object.
#  In python, this is implemented using the "copy.copy()" function. 
import copy

a = [[1, 2, 3], [4, 5, 6]]
# Creating a deep copy of the nested list 'a'
b = copy.deepcopy(a)
c=copy.copy(a)
c[0][0]=98
print(a)
# Modifying an element in the deep-copied list
b[0][0] = 99 
print(b)
print(a)
print(c)
print(a)


