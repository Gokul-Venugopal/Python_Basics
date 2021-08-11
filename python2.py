#list
list=['sam',98,10.2] ##list can take heterogenous values
print(list)

#Indexing and Slicing
print(list[2])
print(list[:2])  #for slicing syntax list[start:end:steps]
list=[0,1,2,3,4.5]

print(list[1:4:2]) # [1, 3] from index 1 to 4 in 2 steps
print(list[::-1]) # start to end in reverse
list[0]='a'   ##lists are mutable
print(list)
list=[1,1,2,2,2,2,3]
print(list.count(2)) #returns count of 2 in list
print(list.pop())  #pops last element

#Dictionaries
dict={'key1':20,'key2':'a','key3':10.2}
print(dict)
print(dict['key2'])
print(dict.keys(),dict.values())
dict={'key1':20,'key2':'a','key3':[10,20,30]}
print(dict)    #{'key1': 20, 'key2': 'a', 'key3': [10, 20, 30]}
print(dict['key3'][2]) #third index of key3


#Tuples
#similar to list but immutable
tup=(1,2,3,4)
print(tup)
print(tup[1:3])

#Sets
#sets are similar to dictionary without key values
set1={'hi','hello','amigo'}
print(set1) #arrangment in memory {'amigo', 'hi', 'hello'}
set1={1,1,1,3,4,4,4,5,6,6}
print(set1)    ##{1, 3, 4, 5, 6} unique elements only

#Boolean
print(5>3)
print(1==2)
print(5>1 or 1<0)

#control Flow
a=3
if(a>0):
    print('Go')
elif(1==0):
    print('stop')
else:
    print('run')

#Loops
x=5
while(x>0):
    print(x)
    x=x-1

for x in range(0,5):
    print(x)
##################################################################################################################