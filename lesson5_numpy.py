import numpy as np

##################################################
# Creating Arrays - Part 1

a = np.array([1, 2, 3])
a[0]

np.array(  [   [1, 2],    [3, 4],    [5, 6]    ]   )

# ndim specifies the minimum number of dimensions that the resulting array should have.
# Ones will be pre-pended to the shape as needed to meet this requirement.
a = np.array([1, 2, 3, 4, 5, 6], ndmin = 1)
a = np.array([[1, 2], [3, 4], [5, 6]], ndmin = 4)

a = np.array([[1, 2, 3], [1, 2, 3]], dtype = float)

##################################################
# Array Attributes

a = np.array([[1,2,3],[4,5,6]])
a.shape
a.reshape(3, 2)

a = np.arange(24)
a.reshape(2, 4, 3).ndim
a.reshape(2, 4, 3).shape

##################################################
# Creating Arrays - Part 2

np.empty(shape=(2,2), # Shape of an empty array in int or tuple of int
         dtype = float, # Desired output data type. Optional
         order = 'C' # 'C' for C-style row-major array, 'F' for FORTRAN style column-major array
        )

np.empty([3,2], dtype = int)
np.zeros(5)
np.zeros((5,), dtype = np.int)
np.zeros((2,2))
np.ones(5)
np.ones([2, 2], dtype = int)

x = [1,2,3]
np.asarray(x)

x = [1,2,3]
np.asarray(x, dtype = float)

x = [(1,2,3), (4,5)]
np.asarray(x)

np.arange(5)
np.arange(5, dtype = float)  # dtype set
np.arange(10,20,2)  # start and stop parameters set

np.linspace(10,20,5)
np.linspace(10,20, 5, endpoint = False)
x, step = np.linspace(1,2,5, retstep = True)

np.logspace(1.0, 2.0, num = 10)  # default base is 10
np.logspace(1, 10, num = 10, base = 2)  # set base of log space to 2

##################################################
# Basic Indexing & Slicing

a = np.arange(10)
s = slice(2, 7, 2)
a[s]
a[2:7:2]
a[5]  # slice single item
a[2:]  # slice items starting from index
a[2:5]  # slice items between indexes

a = np.array([[1, 2, 3], [3, 4, 5],[4,5,6]])
a[1:]  # slice items starting from index
a[..., 1]  # this returns array of items in the second column
a[1,...]  # Now we will slice all items from the second row
a[..., 1:]  # Now we will slice all items from column 1 onwards

##################################################
# Boolean Array Indexing

x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]])
condition = x > 5
x[condition]
condition = x % 2 == 0
x[condition]

a = np.array([np.nan, 1,2,np.nan,3,4,5])
a[~np.isnan(a)]

##################################################
# Broadcasting

a = np.array([1,2,3,4])
b = np.array([10,20,30,40])
c = a * b

a = np.array([[0.0,0.0,0.0],[10.0,10.0,10.0],[20.0,20.0,20.0],[30.0,30.0,30.0]])
b = np.array([1.0,2.0,3.0])
b * 2

a + b
a + b.reshape((1, -1))
a + np.concatenate([b.reshape((1, -1)),
                    b.reshape((1, -1)),
                    b.reshape((1, -1)),
                    b.reshape((1, -1))])

##################################################
# Iterating Over Array

a = np.arange(0,60,5).reshape(3,4)
for x in a:
    print(x,)

for x in np.nditer(a):
    print(x,)

a = np.arange(0,60,5)
a = a.reshape(3,4)
b = a.copy(order = 'C').T
for x in np.nditer(b):
    print(x,)

# leackage of abstraction

# Iteration Order
a = np.arange(0,60,5).reshape(3,4)
b = a.T
c = b.copy(order = 'C')
for x in np.nditer(c):
    print(x,)

# Broadcasting Iteration
a = np.arange(0,60,5).reshape(3,4)
b = b.reshape((3, 4)).copy(order = 'C')
for x, y in np.nditer([a, b]):
   print("%d : %d" % (x, y),)

# Array Manipulation

a = np.arange(8)
a = a.reshape(4,2)
a.flat
a.flatten()

### OPTIONAL
a.flatten(order = 'F')
a.ravel()  # returns a flattened one-dimensional array. A copy is made only if needed.
a.ravel(order = 'F')
### OPTIONAL

np.transpose(a)
a.T

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
np.concatenate((a,b))
np.concatenate((a,b), axis = 1)
np.stack((a,b),0)
np.stack((a,b),1)
np.hstack((a,b))
np.vstack((a,b))

a = np.arange(12)
np.split(a,3)
np.split(a,[4,7])

a = np.array([[1,2,3],[4,5,6]])
a.shape
b = np.resize(a, (3,2))
b.shape

a = np.array([[1,2,3],[4,5,6]])
np.append(a, [7,8,9])
np.append(a, [[7,8,9]],axis = 0)
np.append(a, [[5,5,5],[7,8,9]],axis = 1)

# BAD:
my_total_array = np.array([])
for i in range(100):
    myarray = ...
    my_total_array = my_total_array.append(myarray)

# GOOD:
array_list = []
for i in range(100):
    myarray = ...
    array_list.append(myarray)
my_total_array = np.concatenate(array_list)

a = np.array([5,2,6,2,7,5,6,8,2,9])

# 'Return the count of repetitions of unique elements:'
u, counts = np.unique(a, return_counts = True)

# 'Unique array and Indices array:'
u, indices = np.unique(a, return_index = True)

# 'We can see each number corresponds to index in original array:'
print(a)

# 'Indices of unique array:'
u, indices = np.unique(a, return_inverse = True)

# 'Reconstruct the original array using indices:'
u[indices]

def complex_operation(x):
    return x * 2 + 3

result_a = complex_operation(a)  # what we want
result_u = complex_operation(u)
result_u[indices]  # ist gleich result_a
