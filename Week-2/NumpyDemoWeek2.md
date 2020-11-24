```python
import numpy as np
```

# Create Numpy Array - I


```python
arr_1d = np.array([4,2,3])
```


```python
type(arr_1d)
```




    numpy.ndarray




```python
arr_2d = np.array([[3,1,2], [5,4,6]])
arr_2d
```




    array([[3, 1, 2],
           [5, 4, 6]])




```python
arr_3d = np.array([
    [
        [2,3], [4,1], [3,1]
    ], 
    [
        [33,1], [9,5], [4,2]
    ], 
    [
        [2,3], [4,1], [2,1]
    ], 
    [
        [33,1], [9,5], [3,1]
    ]
])
arr_3d
```




    array([[[ 2,  3],
            [ 4,  1],
            [ 3,  1]],
    
           [[33,  1],
            [ 9,  5],
            [ 4,  2]],
    
           [[ 2,  3],
            [ 4,  1],
            [ 2,  1]],
    
           [[33,  1],
            [ 9,  5],
            [ 3,  1]]])



# Array Atrributes


```python
print(arr_1d.shape)
print(arr_2d.shape)
print(arr_3d.shape)
```

    (3,)
    (2, 3)
    (4, 3, 2)
    


```python
# The first argument of shape
print(len(arr_1d), np.size(arr_1d, 0))
print(len(arr_2d), np.size(arr_2d, 0))
print(len(arr_3d), np.size(arr_3d, 0))
```

    3 3
    2 2
    4 4
    


```python
# The number of elements along a given axis.
# If axis = None, return number of element of array.
print(arr_1d.size, np.size(arr_1d))
print(arr_2d.size, np.size(arr_2d))
print(arr_3d.size, np.size(arrr_3d))
```

    3 3
    6 6
    24 24
    


```python
# Return data type object
print(arr_1d.dtype)
print(np.array(["Hello", "World"]).dtype)
print(np.array([1, 2, 3], dtype="f").dtype)
```

    int32
    <U5
    float32
    


```python
# Return dimension of narray
print(arr_1d.ndim)
print(arr_2d.ndim)
print(arr_3d.ndim)
```

    1
    2
    3
    

# Create Numpy Array - II


```python
# arange([start,] stop[, step,], dtype=None)
even_arr = np.arange(1, 10, 2)
print(even_arr)
```

    [1 3 5 7 9]
    


```python
# np.linspace(start, stop, num=50, endpoint=True,retstep=False,dtype=None,axis=0,)
# If endpoint = True
print(np.linspace(1, 99, 50))
# If endpoint = False
print(np.linspace(1, 101, 50, endpoint=False))
```

    [ 1.  3.  5.  7.  9. 11. 13. 15. 17. 19. 21. 23. 25. 27. 29. 31. 33. 35.
     37. 39. 41. 43. 45. 47. 49. 51. 53. 55. 57. 59. 61. 63. 65. 67. 69. 71.
     73. 75. 77. 79. 81. 83. 85. 87. 89. 91. 93. 95. 97. 99.]
    [ 1.  3.  5.  7.  9. 11. 13. 15. 17. 19. 21. 23. 25. 27. 29. 31. 33. 35.
     37. 39. 41. 43. 45. 47. 49. 51. 53. 55. 57. 59. 61. 63. 65. 67. 69. 71.
     73. 75. 77. 79. 81. 83. 85. 87. 89. 91. 93. 95. 97. 99.]
    


```python
# Return numbers spaced evenly on a log scale.
print(np.logspace(1, 5, 10))
np.logspace
```

    [1.00000000e+01 2.78255940e+01 7.74263683e+01 2.15443469e+02
     5.99484250e+02 1.66810054e+03 4.64158883e+03 1.29154967e+04
     3.59381366e+04 1.00000000e+05]
    




    <function numpy.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None, axis=0)>




```python
# zeros(shape, dtype=float, order='C')
# Return a new array of given shape and type, filled with zeros.
print(np.zeros((2,3,4), int))
# ones
print(np.ones((2,3,4), int))
# full
print(np.full((2,3,4), 5))
# eyes
print(np.eye(4))
```

    [[[0 0 0 0]
      [0 0 0 0]
      [0 0 0 0]]
    
     [[0 0 0 0]
      [0 0 0 0]
      [0 0 0 0]]]
    [[[1 1 1 1]
      [1 1 1 1]
      [1 1 1 1]]
    
     [[1 1 1 1]
      [1 1 1 1]
      [1 1 1 1]]]
    [[[5 5 5 5]
      [5 5 5 5]
      [5 5 5 5]]
    
     [[5 5 5 5]
      [5 5 5 5]
      [5 5 5 5]]]
    [[1. 0. 0. 0.]
     [0. 1. 0. 0.]
     [0. 0. 1. 0.]
     [0. 0. 0. 1.]]
    

# Create random number array


```python
from numpy import random
```


```python
# randint(low, high=None, size=None, dtype=int)
print(random.randint(1, 10, (2,3)))
# rand : Random values in a given shape
print(random.rand(2, 3))
```

    [[6 7 5]
     [3 8 2]]
    [[0.48131667 0.42971598 0.15752261]
     [0.63592677 0.03942901 0.06625143]]
    


```python
arr = np.arange(10)
# Shuffle:  makes changes to the original array.
random.shuffle(arr)
print(arr)
# Permutation: returns a re-arranged array (and leaves the original array un-changed).
arr = np.arange(10)
permutation_arr = random.permutation(arr)
print("origin: ", arr)
print("permutation: ", permutation_arr)
```

    [2 9 5 8 0 3 6 4 1 7]
    origin:  [0 1 2 3 4 5 6 7 8 9]
    permutation:  [9 2 3 4 5 7 6 1 8 0]
    

# Numpy Indexing & Slicing

# Array Broadcasting


```python
arr1 = np.arange(1, 17).reshape((4,4))
arr2 = np.copy(arr1)
```


```python
# Plus
print(arr1 + arr2)
# Minus
print(arr1 - arr2)
# Multiple
print(np.multiply(arr1, arr2))
print(arr1 * 2)
# Division
print(arr1 / 2)
```

    [[ 2  4  6  8]
     [10 12 14 16]
     [18 20 22 24]
     [26 28 30 32]]
    [[0 0 0 0]
     [0 0 0 0]
     [0 0 0 0]
     [0 0 0 0]]
    [[  1   4   9  16]
     [ 25  36  49  64]
     [ 81 100 121 144]
     [169 196 225 256]]
    [[ 2  4  6  8]
     [10 12 14 16]
     [18 20 22 24]
     [26 28 30 32]]
    [[0.5 1.  1.5 2. ]
     [2.5 3.  3.5 4. ]
     [4.5 5.  5.5 6. ]
     [6.5 7.  7.5 8. ]]
    

# Array manipulation


```python
print(arr1.reshape(-1))
# Flatten return a copy
arr1.flatten()
# Ravel return a view of the original array.
arr1.ravel()
```

    [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16]
    




    array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16])




```python
# Transpose
arr1.transpose()
arr1.T
```




    array([[ 1,  5,  9, 13],
           [ 2,  6, 10, 14],
           [ 3,  7, 11, 15],
           [ 4,  8, 12, 16]])




```python
arr1
```




    array([[ 1,  2,  3,  4],
           [ 5,  6,  7,  8],
           [ 9, 10, 11, 12],
           [13, 14, 15, 16]])




```python
# Join a sequence of arrays along an existing axis.
# concatenate((a1, a2, ...), axis=0, out=None)
vstack_arr = np.vstack((arr1, arr2))
print(np.concatenate((arr1, arr2)))
print(vstack_arr)

hstack_arr = np.hstack((arr1, arr2))
print(np.concatenate((arr1, arr2), axis = 1))
print(hstack_arr)
```

    [[ 1  2  3  4]
     [ 5  6  7  8]
     [ 9 10 11 12]
     [13 14 15 16]
     [ 1  2  3  4]
     [ 5  6  7  8]
     [ 9 10 11 12]
     [13 14 15 16]]
    [[ 1  2  3  4]
     [ 5  6  7  8]
     [ 9 10 11 12]
     [13 14 15 16]
     [ 1  2  3  4]
     [ 5  6  7  8]
     [ 9 10 11 12]
     [13 14 15 16]]
    [[ 1  2  3  4  1  2  3  4]
     [ 5  6  7  8  5  6  7  8]
     [ 9 10 11 12  9 10 11 12]
     [13 14 15 16 13 14 15 16]]
    [[ 1  2  3  4  1  2  3  4]
     [ 5  6  7  8  5  6  7  8]
     [ 9 10 11 12  9 10 11 12]
     [13 14 15 16 13 14 15 16]]
    


```python
# Split
print(np.split(vstack_arr, 2))
print(np.vsplit(vstack_arr, 2))

print(np.split(hstack_arr, 2, axis = 1))
print(np.hsplit(hstack_arr, 2))
```

    [array([[ 1,  2,  3,  4],
           [ 5,  6,  7,  8],
           [ 9, 10, 11, 12],
           [13, 14, 15, 16]]), array([[ 1,  2,  3,  4],
           [ 5,  6,  7,  8],
           [ 9, 10, 11, 12],
           [13, 14, 15, 16]])]
    [array([[ 1,  2,  3,  4],
           [ 5,  6,  7,  8],
           [ 9, 10, 11, 12],
           [13, 14, 15, 16]]), array([[ 1,  2,  3,  4],
           [ 5,  6,  7,  8],
           [ 9, 10, 11, 12],
           [13, 14, 15, 16]])]
    [array([[ 1,  2,  3,  4],
           [ 5,  6,  7,  8],
           [ 9, 10, 11, 12],
           [13, 14, 15, 16]]), array([[ 1,  2,  3,  4],
           [ 5,  6,  7,  8],
           [ 9, 10, 11, 12],
           [13, 14, 15, 16]])]
    [array([[ 1,  2,  3,  4],
           [ 5,  6,  7,  8],
           [ 9, 10, 11, 12],
           [13, 14, 15, 16]]), array([[ 1,  2,  3,  4],
           [ 5,  6,  7,  8],
           [ 9, 10, 11, 12],
           [13, 14, 15, 16]])]
    

# Binary Operations

# Math Operations


```python
print(np.add(arr1, arr2))
print(np.subtract(arr1, arr2))
print(np.multiply(arr1, arr2))
print(np.divide(arr1, arr2))
```

    [[ 2  4  6  8]
     [10 12 14 16]
     [18 20 22 24]
     [26 28 30 32]]
    [[0 0 0 0]
     [0 0 0 0]
     [0 0 0 0]
     [0 0 0 0]]
    [[  1   4   9  16]
     [ 25  36  49  64]
     [ 81 100 121 144]
     [169 196 225 256]]
    [[1. 1. 1. 1.]
     [1. 1. 1. 1.]
     [1. 1. 1. 1.]
     [1. 1. 1. 1.]]
    


```python
print(np.power(arr1, 2))
print(np.mod(arr1, 2))
```

    [[  1   4   9  16]
     [ 25  36  49  64]
     [ 81 100 121 144]
     [169 196 225 256]]
    [[1 0 1 0]
     [1 0 1 0]
     [1 0 1 0]
     [1 0 1 0]]
    

# Statiscal Function


```python
# np.max is just an alias for np.amax. This function only works on a single input array and finds the value of maximum element in that entire array (returning a scalar
print(np.max(arr1, 0))
# The default behaviour of np.maximum is to take two arrays and compute their element-wise maximum
```

    [13 14 15 16]
    


```python
np.ptp(arr1, axis=1)
```




    array([3, 3, 3, 3])




```python
print(np.mean(arr1))
print(np.sum(arr1) / arr1.size)
```

    8.5
    8.5
    


```python
np.median(arr1)
```




    8.5



# Sorting and Searching


```python
arr3 = random.randint(-5, 5, 16)
print(arr3)
```

    [-1  3  4  0 -2 -4  2  0  0  0  2 -3  2 -2 -1 -5]
    


```python
print(np.sort(arr3))
```

    [-5 -4 -3 -2 -2 -1 -1  0  0  0  0  2  2  2  3  4]
    


```python
np.nonzero(arr3)
```




    (array([ 0,  1,  2,  4,  5,  6, 10, 11, 12, 13, 14, 15], dtype=int64),)




```python
arr4 = arr3 > 1
arr4
```




    array([False,  True,  True, False, False, False,  True, False, False,
           False,  True, False,  True, False, False, False])



# Copy and view


```python
copy_arr = arr1.copy()
view_arr = arr1.view()
print("origin: ", id(arr1))
print("copy: ", id(copy_arr))
print("view: ", id(view_arr))
```

    origin:  2859663134768
    copy:  2859663040384
    view:  2859663037424
    

# Linear Algebra


```python
arr1
```




    array([[ 1,  2,  3,  4],
           [ 5,  6,  7,  8],
           [ 9, 10, 11, 12],
           [13, 14, 15, 16]])



# I/O with Numpy


```python
np.save("out.txt", arr1)
```


```python
np.load("out.txt.npy")
```




    array([[ 1,  2,  3,  4],
           [ 5,  6,  7,  8],
           [ 9, 10, 11, 12],
           [13, 14, 15, 16]])




```python
np.savetxt("outtxt.txt", arr1)
```


```python
np.loadtxt("outtxt.txt")
```




    array([[ 1.,  2.,  3.,  4.],
           [ 5.,  6.,  7.,  8.],
           [ 9., 10., 11., 12.],
           [13., 14., 15., 16.]])


