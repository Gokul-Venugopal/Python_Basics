#using slicing
my_list=['a','b','c','d','e','f']

for i in my_list[::2]:  ###2 steps printing
    print(i)

### appending a string
msg="hello"
my_list=[]
for i in msg:
    my_list.append(i)
print(my_list)

my_list1=[char for char in msg]
print(my_list1)

for i in range(0,5):     ###squares from 0 to 5
    print(i**2)

square_val=[i**2 for i in range(0,5) ]  ###Alternate way  [0, 1, 4, 9, 16]
print(square_val)

###Similarly calculating odd numbers from 1 to 10
my_even=[i  for i in range(1,11) if i%2!=0 ]
print(my_even)

#list comprehension with nested for loop
for i in [4,5,6]:
    for j in [1,2,3]:
        print(i**j)

#Alternate way
res=[i**j for i in [4,5,6] for j in [1,2,3] ]

##################################################################################################################
#functions
name="function"
def sample_fun(self):
    print(f'This is a sample {name}')
sample_fun(name)

def sum_1(a,b):
    print(f'Sum is {a+b}')
sum_1(10,100)

num=[1,2,3,6,7]
def even_odd(num):  #checks the number in num if first number is even it returns true else false
    for i in num:
     if i % 2==0:
        return True
     else:
        return False
print(even_odd(num))

#################################################################################################################