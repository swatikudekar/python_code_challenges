## write code to join two columns with left join

import pandas as pd
df1=pd.DataFrame({'col1':[3,4,8,10,12]})
df2=pd.DataFrame({'col1':[3,7,5,9,0]})
df3=pd.merge(df1,df2,on='col1',how='left')
print(df3)


##find out 2nd highest number from the list of numbers
def second_highest(list2):
   list1=list(set(list2))
   list1.sort(reverse=True) 
   return list1[1] #list start from 0
   
list2=[9,5,8,10,12,5,7,15]
num=second_highest(list2)
print("second highest number==",num)

##sort list in increasing order and decreasing order
list1=[2,6,7,1,0,9,4,6,19,43,86,34,98,2]
list1=list(set(list1)) # remove  dublicates
list1.sort()
print(list1)
list2=list1
list2.sort(reverse=True)
print(list2)

## to find second highest number from list without using inbuild functions
import pandas as pd
def second_number(numbers):
   maxnum=max(numbers)
   number=numbers[0]
   for num in numbers:
     if number<num and maxnum!=num:
        print(number,num)
        number=num
   return number

list1=[3,8,3,7,5,10,9,32,24,52]
number=second_number(list1)
print(number)



