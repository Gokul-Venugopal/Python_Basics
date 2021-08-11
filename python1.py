             #Basics of Python Programming-1

#printing output using print()
print("hello world")

#printing arithmatic operation on numbers
print(10+5)   #addition
print(5-2)    #subtraction
print(10/5)   #division
print(10*5)   #multiplication
print(9%2)    #modulo

print(3**2)   #3 power 2


print((10+2)*5) #paranthesis given first preference
################################################################################################################
#variables
## variable should begin with a letter or underscore
## variable should not begin with a number
## no special character not even space should be used
a =10
b =50
sum_ab =a*b
print(sum_ab)
##################################################################################################################
#dynamic typing :values assigned can be changed dynamically
name="Sam"
print(name)
name=10
print(name)
print(type(name))  #type of variable

#################################################################################################################
#strings
## Strings are immutable
name="RAM"
print(name)
#name[0]='s'       ##gives an error :TypeError: 'str' object does not support item assignment
new_name='S'+ name[1:3]   #concatination can be done with '+' and sliced arr name[1:3] is concatinated
print(new_name)
print(name[2]) #string characters can be accessed using its index
str1='a'
print(str1*10)    #concatination of str1 10 times ie,aaaaaaaaaa

str="I am good"
print(str.split()) ## splits into ['I', 'am', 'good']
print(str.split('m')) ## ['I a', ' good']  splits at m into 2 parts 'I a' and ' good'
print(str.upper()) #I AM GOOD converts into uppercase , similarly lower() to lower case

#printing using f' string
name="Gokul"
age=22
print(f'Hi my name is {name} and my age is {age}') ## Hi my name is Gokul and my age is 22

#################################################################################################################



