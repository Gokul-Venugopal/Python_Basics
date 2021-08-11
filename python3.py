#for loop
list=[1,2,3,4,5,6]
for i in list:
    if(i%2==0):
        print(f'{i} is even') ##printing even numbers from the list
    else:
        print(f'{i} is odd')  ##printing odd numbers from the list

##To print letters in string using for loop
msg="Gokul"
for letter in msg:
    print(letter)   #prints the letters in msg

print(f' $ printed {len(msg)} times')
for _ in msg:
    print('$')    ##printing $ character as many times as the length of msg

#################################################################################################################
#Tuple unpacking
list_tup=[(1, 2), (3, 4), (5, 6)]
for i in list_tup:  ###tuple is printed without unpacking
    print(i)

for i,j in list_tup:  ###tuple is unpacked and printed
    print(i)
    print(j)

#unpacking incase of dictionary
tools={'key1':1,'key2':2}
for i in tools:
    print(i)      #only prints key values

for i in tools.items():   #items() prints the both key and values
    print(i)

for i in tools.values():   #prints only the values
    print(i)


for i,j in tools.items():   #unpacking
    print(i)                ##key values
    print(j)                ##values

################################################################################################################
#break,continue and pass
list=[7,8,9,10]

#pass
for i in list:   ##if we want go to other part we can pass this loop for time being
    pass

#continue
for i in list:
    if i==9:      #skips 9 and prints rest of all the numbers in the list
        continue
    print(i)
#break
for i in list:
    if i==9:      #if i==9 control comes out of the for loop
        break
    print(i)

my_msg="hello"
for index in enumerate(my_msg):
    print(index)

for index,ch in enumerate(my_msg):   ##unpacking of index and character
    print(index,ch)


my_list=[1,2,3,4,5]
for index,ch in enumerate(my_msg):   #except 1st index all othes are printed
    if(index==1):
        my_list.pop()
    print(index,ch)

#################################################################################################################
#zip
list1=[1,2,3]
list2=['a','b','c']

for i in zip(list1,list2):
    print(i)                 ###list1 is zipped to list2

#in operator
print('x' in ['a','b','x'])     ##returns true if x is not there returns false

#min function
print(min(my_list))

###############################################################################################################