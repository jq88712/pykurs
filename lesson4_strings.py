
names= list(mtcars2.index)

example_string=names[1]
example_string
example_string.lower()
example_string.upper()
lower=example_string.lower()
lower.capitalize()
example_string.swapcase()

[x.upper() for x in names][:5]

example_string.split()
example_string.split("a")
example_string.split()[0]
[x.split()[0] for x in names][:5]

'Mazda' in example_string

list_merc=[x for x in names if "Merc" in x]
list_merc
mtcars2.loc[list_merc,:]

a=['a','b','c']
b=['A','B','C']
"|".join(a)

example_string.replace('RX4', 'replacement text')
example_string.replace('RX4 ', "")

another_string="Hello Python, goodbye Python! Nice to meet you Python."
another_string.replace("Python", "Guido", 2)

import re

re_result = re.search('RX[0-9]', example_string)
re_result.group()

re.search('RX[0-9]*', 'Mazda 124 Wag').group()
re.search('RX[0-9]*', 'Mazda RX Wag').group()
