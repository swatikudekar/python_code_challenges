#***************** string reverse *******************
str1 = "Analytics Vidhya"
str2 = ""
for i in str1:
    str2 = i + str2
    
print("The original string is: ", str1)
print("The reversed string is: ", str2)
# ***use build in ************
str1 = "Analytics Vidhya"
print(str1[::-1]) #string slicing.
print(str1[0::1]) #original string
print(str1.split(" ")) ##split function
print(str1.upper(),str1.lower(),str1.capitalize(),str1.casefold(),str1.swapcase()) #conversion
lst=[1,2,4,5,3]
sqr_lst=[]
for i in lst:
    sqr_lst.append(i*i)
print(sqr_lst)

print(str1.find("V")) # Returns the index of the first occurrence of sub, or -1
print(str1.rfind("A")) # Returns the last occurrence index
try:
    print(str1.index("X"))# Like find(), but raises an error if not found
except:
    pass
print(str1.rindex("a")) # Like rfind(), but raises an error if not found

print(str1.count("A"))# Counts how many times sub appears
print(str1.startswith("v")) # Checks if string starts with prefix
print(str1.endswith("a"))# Checks if string ends with suffix

str1.strip() # Removes leading/trailing whitespace
str1.lstrip() #Removes leading whitespace
str1.rstrip() # Removes trailing whitespace
str2=str1.replace("na", "ma") # Replaces substring
print(str2)

str2=str1.removeprefix("A") # Removes prefix (Python 3.9+)
print(str2)
str2=str1.removesuffix("ya") # Removes suffix (Python 3.9+)
print(str2)

#Splitting & Joining
str1.split(" ") # Splits string into a list
str1.rsplit(" ") # Splits from the right
str1.splitlines() # Splits string at line breaks

str2=str1.join("str") # Joins elements of an iterable with the string as separator
print("\n"+str2)
str1.partition(" ") # Splits into 3 parts: before, separator, after
str1.rpartition(" ") # Like partition() but from the right
str.isalpha() # Checks if all characters are letters
str.isdigit() # Checks if all characters are digits
str.isalnum() # Checks if all characters are alphanumeric
str.isdecimal() # Checks for decimal characters
str.isnumeric() # Checks for numeric characters
str.islower() # Checks if all characters are lowercase
str.isupper() # Checks if all characters are uppercase
str.isspace() # Checks if all characters are whitespace
str.istitle() # Checks if string follows title case

str.encode() # Encodes string to bytes
str.format() # Formats string using placeholders