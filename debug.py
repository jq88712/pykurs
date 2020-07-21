
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
