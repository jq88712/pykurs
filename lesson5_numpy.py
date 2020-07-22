import numpy as np

##################################################
# Creating Arrays - Part 1

a = np.array([1, 2, 3])
a[0]

np.array(  [   [1, 2],    [3, 4],    [5, 6]    ]   )

# ndim specifies the minimum number of dimensions that the resulting array should have.
# Ones will be pre-pended to the shape as needed to meet this requirement.
a = np.array([1, 2, 3, 4, 5, 6], ndmin = 2)
a = np.array([[1, 2], [3, 4], [5, 6]], ndmin = 4)

a = np.array([[1, 2, 3], [1, 2, 3]], dtype = float)

##################################################
# Array Attributes

a = np.array([[1,2,3],[4,5,6]])
a.shape
a.reshape(3, 2)

a = np.arange(24)
a.reshape(2, 4, 3).ndim

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

