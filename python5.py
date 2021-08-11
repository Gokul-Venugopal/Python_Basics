#Tuple Unpacking With Functions:
name_salary=[('Raj',1000),('John',3000),('Tina',6000)]
for name,salary in name_salary:
    print(name)
    print(salary)


###finding which employee has max salary
def max_sal(name_sal):
    max_curr=0
    emp_name=''
    for n,s in name_sal:
        if max_curr<s:
            max_curr=s
            emp_name=n
    return emp_name, max_curr


n1,s1=max_sal(name_salary)
print(f'{n1} has the maximum salary of rupees {s1}')

###Args and Kwargs:
#args
def sum1(*args):       #takes any number of parameters
    return(sum(args))
print(sum1(100,200,300,500))

#kwargs
def check(**kwargs):
    if 'food' in kwargs:
        print('food found')
    else:
        print('No food')
check(fruit='orange',food='noodles',object='chair')
#####################################################################################################################
#3 cups monte game
from random import shuffle
list_cups=['','0','']
shuffle(list_cups)
print(list_cups)   ###this is how shuffle works ['', '', '0']

def shuff(list_cups):      ###shuffle the list
    shuffle(list_cups)
    return list_cups
res=shuff(list_cups)

def guess_inp():     ####ask for the guess from user
    guess=input('Input 0,1 or 2 position')
    return int(guess)
guess=guess_inp()
def game( res,guess):     ###check if guess is right
    if(res[guess]=='0'):
        print("correct answer")
        print(list_cups)
    else:
        print('Wrong guess')
        print(list_cups)
game(list_cups,guess)


#map(function,iterables)
list1=[1,2,3,4]
def square(num):
    return(num**2)

print(list(map(square,list1)))   ###maps all the items in list with square()

#filter
def even_check(num):
    return num%2==0
print(list(filter(even_check, list1)))  #only even numbers

#lambda method
square= lambda num: num**2
print(square(4))
print(square(25))                #prints square of num
###############################################################################################################

