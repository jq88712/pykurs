# Monospaced

# Wie ich Zeug anlege...
from typing import Union

a = 1
b = 1.234
c = a
c
a = 2
x = "hello ' "
x = 'hello \"\' '
print(x)

a = 1
if (a == 1):
    print("a is equal to 1")
    if b == 2:
        print('asdf')

help(abs)
abs(-2)

# Character
'a', 'b', '3'  # ascii, utf-8
# integer
# float
# String = Zeichenkette

print(c[0])
print(c[1:5])
print(c[-6:])  # if the first or last index is omitted, it defaults to zero)
print(c[:3])
print(c[:8:2]) # a third index defines the step. Here, in every two letters one is selected)
print(c[::-1]) # all charaters in reverse order)

for i in range(0, len(c)):
    print(c[i])

for i in range(0, len(c)):
    print(i)

pi=3.14
print("the value of pi is {}".format(pi))
print("the value of pi is %f" %pi)

example_list=[1,2,3,5,7,11, "string", 5.6]

print(example_list[2:6])
print(example_list[5])
print(example_list[6])

new_list=example_list + ["another", "list"]
print(new_list)
print(example_list*2)

example_list[0] = "new element"
print(example_list)

example_list[3:7]=[234,456]
print(example_list)

example_list.append("last element")
print(example_list)

list2 = ["final element", 'final for real']

example_list.append(list2)
example_list.extend(list2)

print(range(10))
print(range(2, 20, 4))

a=[1,2,[7,2,8]]
print(a[0])
print(a[2])
print(a[2][1])

# Tuple

tup = 23, 45, 45, "last"
print(tup)
print(tup[1])

tup[0] = 3

a, b, c, d = tup
print(a)
print(b)
print(c)
print(d)

### Sets

a_list=[1,2,3,3,2,4,5,6,6,6,4]
a_set = set(a_list)   # a_set=
print(a_set)

# multiset

another_set={4,5,6,7,8,9,10}
print(a_set - another_set) # elements in a_set but not in b_set)
print(a_set | another_set) # union)
print(a_set & another_set) # intersection)
print(a_set ^ another_set) # elements that are exclusive to both sets)
print((a_set | another_set) - (a_set & another_set))

## dictionary / map

a_dic={'artur': 1000, 'josef': 235, 'miguel': 25}
print(a_dic)
print(a_dic['josef'])
print(a_dic['artur'])
a_dic['peter'] = 5660
print(a_dic)
print(a_dic.keys())



print('peter' in a_dic)
print('helder' in a_dic)
print(1 in a_set)
print('last' in tup)
print(2 in [1,2,3])


# Control Structures

## IF

t=10

if t >= 20 and t < 30:
    print("nice!")
elif t>=30:
    print("It's too hot!")
else:
    print("It's cold!")

for elem in example_list:
    print(   (elem, type(elem))     )

## For Schleife

a = 0
for elem in range(5):
    a = a + elem * 2
print(a)
b = 5

## While Schleife

x = 0

# x = 5

while x < 5:
    print(x)
    x = x + 1
    print(x)
print('hello')

0
1
2
3
4
'hello'

# expression

x = 0
while True:
    print(x)

    if x % 2 == 0:
        pass
    else:
        x = x + 1

    if x >= 5:
        break


def myappend(liste, element):
    print(liste)
    liste.append(element)
    print(element)

list_outer = []  # creates empty list
for num in range(1, 5):
    # num = 5
    list_inner = []  # creates another empty list
    # list(range(num))
    for x in range(num):
        if x == 3:
            continue  # when x==3 the program skips to the next step
            # in the loop in x (the lists never include the value 3)
        myappend(list_inner, x)
    list_outer.append(list_inner)
print(list_outer)




for r in range(5):
    x=r*2
    print(x)



a=1
b=2
print( a==b )   # is a equal to b?)
print( a<b )   # is a smaller than b?)
print( a>b )   # is a bigger than b?)
print( a!=b )   # is a not equal to b?)
print( a>=b )   # is a bigger than or equal to b?)
print( a<=b )   # is a bigger than or equal to b?)


a=1
b=2

print( a!=b and b==2*a )
print( a!=b and b==3*a )
print( a==b or b==2*a )
print(  not(a!=b)   )

True and True = True
True and False = False
False and True = False
False and False = False

True or True = True
True or False = True
False or True = True
False or False = False

True xor True = False
True xor False = True
False xor True = True
False xor False = False



def function_name(argument1, argument2):
    result = argument1 * argument2
    return result

a = 5
a = 'string'

def myfunc(a: int, b: int, d=None) -> Union[str, int]:
    print("the arguments of the function are %d and %d"%(a,b))
    c = a + 2 * b
    print(d)
    if d is None:
        return c
    else:
        return str(c)

def myfunc(a: int, b: int, return_type: str) -> Union[str, int, float]:
    print("the arguments of the function are %d and %d"%(a,b))
    c = a + 2 * b
    print(d)
    if return_type == 'int':
        return int(c)
    elif return_type == 'float':
        return float(c)
    elif return_type == 'str':
        return str(c)
    else:
        return None

def run_this_fct(fct, a, b):
    return fct(a, b)

myresult = myfunc(b=2, a=3)
print(myresult)

run_this_fct(myfunc, a, b)


def intdivision(dividend,divisor):
    intval = dividend // divisor
    remainder = dividend % divisor
    return intval, remainder

intdivision(17, 5)


def intdivision(dividend, divisor):
    return dividend // divisor, dividend % divisor

def fav_color(x='blue'):
    print("my favorite color is %s" %x)





def run_this_fct(fct, a):
    print("I'm gonne run like the wind.")
    return fct(a)

run_this_fct(lambda x: x**2, 3)



print(asdf)

asdf = run_this_fct(lambda x: x**2, 3)
g = 4





squares = []
for r in range(5):
    squares.append(r ** 2)

print(squares)

squares2 = [x**2 for x in range(5)]

# list comprehension

print(squares2)

{'paul': 5, 'eva': 156}

{x: x**2 for x in range(5)}

paul = 5
eva = 156

['paul', 'eva']
[5, 156]

nr = 0
for name in ['paul', 'eva', 'saskia']:
    if name == 'eva':
        final_nr = nr
    nr = nr + 1
[5, 156][final_nr]

# runtime complexity

mylist = [x**2+3 for x in range(10) if x % 2 == 0]
print(mylist)

for i, x in enumerate(mylist):
    print(i, x)

mylist = ['paul', 'eva', 'saskia']
for nr, name in enumerate(mylist):
    if name == 'eva':
        final_nr = nr

mylist[final_nr]
mylist[nr]
print(nr, name)

[5, 156][final_nr]



mylist=['Mario', 'Pedro', 'Jean']
hobbies=['spear fishing', 'surfing', 'tennis']
for y, x in zip(mylist, hobbies):
    print("%s's favorite hobby is %s" % (y,x))



mynrlist = [0,1,2]
mylist = ['paul', 'eva', 'saskia']
for nr, name in zip(mynrlist, mylist):
    if name == 'eva':
        final_nr = nr
print(final_nr, name)


