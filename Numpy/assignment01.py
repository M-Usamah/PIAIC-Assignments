
#1.Import the numpy package under the name np
import numpy as np

#1.Create a null vector of size 10
arr1_1 = np.zeros(10)

#1.Create a vector with values ranging from 10 to 49
arr1_2 = np.arange(10, 50)

#1.Find the shape of previous array in question 3
print(arr1_2.shape)

#1.Print the type of the previous array in question 3
print(arr1_2.dtype)

#1.Print the numpy version and the configuration
print(np.__version__)

#1.Print the dimension of the array in question 3
print(arr1_2)

#1.Create a boolean array with all the True values
arr1_3 = np.ones(10)

#1.Create a two dimensional array
arr1_5 = np.ones((2,2))

#1.Create a three dimensional array
arr1_5 = np.ones((3,3,3))

#2.Reverse a vector (first element becomes last)
arr2_1 = np.array([1,2.4,6])
reversed_arr = arr2_1[::-1]

#2.Create a null vector of size 10 but the fifth value which is 1
arr2_2 = np.zeros(10)
arr2_2[4]=1

#2.Create a 3x3 identity matrix
arr2_3 = np.identity(3)

'''
#2.arr = np.array([1, 2, 3, 4, 5])
Convert the data type of the given array from int to float
'''
arr = np.array([1, 2, 3, 4, 5])
new_arr = arr.astype(float)

'''
#2.arr1 = np.array([[1., 2., 3.],
                   [4., 5., 6.]])

arr2 = np.array([[0., 4., 1.],
                [7., 2., 12.]])

Multiply arr1 with arr2
'''
arr1 = np.array([[1., 2., 3.],
                [4., 5., 6.]])
arr2 = np.array([[0., 4., 1.],
                [7., 2., 12.]])
mul_arr = np.multiply(arr1,arr2)

'''
#2.arr1 = np.array([[1., 2., 3.],
                    [4., 5., 6.]])
arr2 = np.array([[0., 4., 1.],
                [7., 2., 12.]])
Make an array by comparing both the arrays provided above
'''
arr1 = np.array([[1., 2., 3.],
                    [4., 5., 6.]])
arr2 = np.array([[0., 4., 1.],
                [7., 2., 12.]])
comparing_arr = arr1 == arr2
equal_arr = comparing_arr.all()

#2.Extract all even numbers from arr with values(0-9)
arr2_4 = np.arange(10)
odd_arr = (arr2_4%2==1)

#2.Replace all odd numbers to -1 from previous array
arr2_4[odd_arr] = -1

'''
2.arr = np.arange(10)
Replace the values of indexes 5,6,7 and 8 to 12
'''
arr = np.arange(10)
arr[5]=12
arr[6]=12
arr[7]=12
arr[8]=12

#2.Create a 2d array with 1 on the border and 0 inside
arr2_5 = np.ones((5,5))
arr2_5[1:-1,1:1] = 0

'''
3.arr2d = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

Replace the value 5 to 12
'''
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
arr2d[1,1] = 12

'''
3.arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
Convert all the values of 1st array to 64
'''
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr3d[0:1] = 64

#3.Make a 2-Dimensional array with values 0-9 and slice out the first 1st 1-D array from it
arr2_6 = np.array([[0,1,2,3,4],[5,6,7,8,9]])
print(arr2_6[0:1])

#3.Make a 2-Dimensional array with values 0-9 and slice out the 2nd value from 2nd 1-D array from it
arr2_6 = np.array([[0,1,2,3,4],[5,6,7,8,9]])
print(arr2_6[1:2])

#3.Make a 2-Dimensional array with values 0-9 and slice out the 2nd value from 2nd 1-D array from it
arr2_6 = np.array([[0,1,2,3,4],[5,6,7,8,9]])
print(arr2_6[0:2,0:1])

#3.Create a 10x10 array with random values and find the minimum and maximum values
arr2_7 = np.random.random((10,10))
arr_max, arr_min = arr.max(),arr.min()
print(arr_max, arr_min)

'''
3.a = np.array([1,2,3,2,3,4,3,4,5,6]) b = np.array([7,2,10,2,7,4,9,4,9,8])
Find the common items between a and b
'''
a = np.array([1,2,3,2,3,4,3,4,5,6]) 
b = np.array([7,2,10,2,7,4,9,4,9,8])
comparing_arr = a == b
print(comparing_arr)


