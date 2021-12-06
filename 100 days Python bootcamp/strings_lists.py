#given string
string1="Python is great"
 
#printing the string
print("Actual String: ",string1) 
   
#gives us the type of string1
print("Type of string: ",type(string1))  
 
print("String converted to list :",string1.split()) 
#prints the list given by split()

# String converted to list : ['Python', 'is', 'great']

#type-casting the string into list using list()
print("String converted to list :\n",list(string1))

# String converted to list :
#  ['P', 'y', 't', 'h', 'o', 'n', ' ', 'i', 's', ' ', 'g', 'r', 'e', 'a', 't']

#**********************************************************
#converting string1 into a list of strings
string1=string1.split()
 
#applying list method to the individual elements of the list string1
list1=list(map(list,string1))
 
#printing the resultant list of lists
print("Converted to list of character list :\n",list1)

# Converted to list of character list :
#  [['P', 'y', 't', 'h', 'o', 'n'], ['i', 's'], ['g', 'r', 'e', 'a', 't']]   

#**********************************************************
#given string
string1="abc,def,ghi"
print("Actual CSV String: ",string1)
print("Type of string: ",type(string1))
 
#spliting string1 into list with ',' as the parameter
print("CSV coverted to list :",string1.split(','))

csvlist = string1.split(',')
print(csvlist[-3])
#**********************************************************

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
    
dirty_dozen = [fruits, vegetables]
    
print(dirty_dozen[1][1])

