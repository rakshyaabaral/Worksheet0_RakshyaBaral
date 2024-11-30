# -*- coding: utf-8 -*-
"""Worksheet01_RakshyaBaral.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dRU3yb6y0uH1cEcrojhS0xEq_F_j6NcO
"""

# Problem1
#1.Initialize an empty array with size 2X2.
import numpy as np
empty_array = np.empty((2,2))
print(empty_array , "\n")

#2. Initialize an all one array with size 4X2.
import numpy as np
ones_array = np.ones((4,2))
print("\n" , ones_array , "\n")

# 3. Return a new array of given shape and type, filled with fill value.
import numpy as np
fill_value =np.full((3,3),2)
print("\n ", fill_value , "\n")

#4. Return a new array of zeros with same shape and type as a given array.
import numpy as np
given_array = np.array([[5, 6], [7, 8]])
zeros_like_array = np.zeros_like(given_array)
print("\n" , zeros_like_array , "\n")

#5. Return a new array of ones with same shape and type as a given array.
import numpy as np
ones_like_array = np.ones_like(given_array)
print("\n" , ones_like_array , "\n")

#6. For an existing list new_list = [1,2,3,4] convert to an numpy array.
import numpy as np
new_list = [1, 2, 3, 4]
numpy_array = np.array(new_list)
print("\n " , numpy_array , "\n")

#Problem 2

import numpy as np
# 1. Create an array with values ranging from 10 to 49.
array_range = np.arange(10, 50)
print("\n " ,array_range , "\n")

#2. Create a 3X3 matrix with values ranging from 0 to 8.
import numpy as np
matrix_3x3 = np.arange(9).reshape(3, 3)
print("\n " ,matrix_3x3 , "\n")

#3. Create a 3X3 identity matrix.
import numpy as np
identity_matrix = np.eye(3)
print("\n" ,identity_matrix , "\n")

#4. Create a random array of size 30 and find the mean of the array.
import numpy as np
random_array = np.random.random(30)
print("\n Random array of size 30: "  , random_array)
mean_value = random_array.mean()
print("\n Mean value: " ,mean_value , "\n")

#5. Create a 10X10 array with random values and find the minimum and maximum values.
import numpy as np
random_10x10 = np.random.random((10, 10))
min_value = random_10x10.min()
max_value = random_10x10.max()
print("\n Random 10X10 array :" ,random_10x10)
print("\n Minimum Value:" ,min_value, "\n Maximum Value:" , max_value, "\n")

#6. Create a zero array of size 10 and replace 5th element with 1.
import numpy as np
zero_array = np.zeros(10)
zero_array[4] = 1
print("\n " ,zero_array , "\n")

#7. Reverse an array arr = [1,2,0,0,4,0].
import numpy as np
arr = np.array([1, 2, 0, 0, 4, 0])
reversed_arr = arr[::-1]
print("\n Reversed array:  " ,reversed_arr , "\n")

#8. Create a 2d array with 1 on border and 0 inside.
import numpy as np
arr=np.zeros((5,5),dtype=int)
arr[0,:]=1 #top
arr[-1,:]=1 #bottom
arr[:,0]=1 #left
arr[:,-1]=1 #right
print("\n",arr)

#9. Create a 8X8 matrix and fill it with a checkerboard pattern.
import numpy as np
checkerboard = np.zeros((8, 8), dtype=int)
checkerboard[1::2, ::2] = 1
checkerboard[::2, 1::2] = 1
print("\n " ,checkerboard , "\n")

#Problem 3
import numpy as np
# 1. Add the two array.
x = np.array([[1, 2], [3, 5]])
y = np.array([[5, 6], [7, 8]])
v = np.array([9, 10])
w = np.array([11, 12])
add_xy = np.add(x, y)
print("\n Addition of x and y:\n", add_xy)

add_vw = np.add(v,w)
print("\n Addition of v + w : \n" ,add_vw)

# 2. Subtract the two array.
import numpy as np
x = np.array([[1, 2], [3, 5]])
y = np.array([[5, 6], [7, 8]])
v = np.array([9, 10])
w = np.array([11, 12])
sub_xy = np.subtract(x, y)
print("\n Subtraction of x and y:\n", sub_xy)

sub_vw = np.subtract(v,w)
print("\n Subtraction of v and w: \n" ,sub_vw)

# 3. Multiply the array with any integers of your choice.
x = np.array([[1, 2], [3, 5]])
y = np.array([[5, 6], [7, 8]])
v = np.array([9, 10])
w = np.array([11, 12])
mul_x = x * 9
print("\n Multiplication of x with 9:\n", mul_x)

mul_y = y * 6
print("Multiplication of y with 6:\n",mul_y)

mul_v = v * 4
print("Multiplication of v with 4 : \n", mul_v)

mul_w = w * 8
print("Multiplication of w with 8:\n" , mul_w)

# 4. Find the square of each element of the array.
x = np.array([[1, 2], [3, 5]])
y = np.array([[5, 6], [7, 8]])
v = np.array([9, 10])
w = np.array([11, 12])
square_x = np.square(x)
print("\nSquare of each element of x:\n", square_x)
square_y = np.square(y)
print("\nSquare of each element of y:\n", square_y)
square_v= np.square(v)
print("\nSquare of each element of v:\n", square_v)
square_w = np.square(w)
print("\nSquare of each element of w:\n", square_w)

import numpy as np
x = np.array([[1, 2], [3, 5]])
y = np.array([[5, 6], [7, 8]])
v = np.array([9, 10])
w = np.array([11, 12])
dot_vw = np.dot(v, w)
dot_xv = np.dot(x, v)
dot_xy = np.dot(x, y)
print("\nDot product of v and w:\n", dot_vw)
print("\nDot product of x and v:\n", dot_xv)
print("\nDot product of x and y:\n", dot_xy)

# 6. Concatenate x(and)y along row and Concatenate v(and)w along column.
import numpy as np
x = np.array([[1, 2], [3, 5]])
y = np.array([[5, 6], [7, 8]])
v = np.array([9, 10])
w = np.array([11, 12])
arr=np.concatenate((x,y),axis=1)
print("\n along row: \n",arr)
array=np.vstack((v,w))
print("\n along column: \n",array)

# 7. Concatenate x(and)v; if you get an error, observe and explain why did you get the error?
import numpy as np
x = np.array([[1, 2], [3, 5]])
y = np.array([[5, 6], [7, 8]])
v = np.array([9, 10])
w = np.array([11, 12])
result = np.concatenate((x, v))
print("Concatenation result:\n", result)

# Problem - 4: Matrix Operations:
# • For the following arrays:
# A = np.array([[3,4],[7,8]]) and B = np.array([[5,3],[2,1]]);
# Prove following with Numpy:
# 1. Prove A.A−1 = I
import numpy as np
A=np.array([[3,4],[7,8]])
B=np.array([[5,3],[2,1]])
A_inv=np.linalg.inv(A)
result=np.dot(A,A_inv)
identity_matrix=np.eye(2)
print("\n Matrix A:\n", A)
print("\n Inverse of A (A^-1):\n", A_inv)
print("\n Product of A and A^-1 (A.A^-1):\n", result)
print("\n Identity Matrix:\n", identity_matrix)
y=np.allclose(result,identity_matrix)
print("\n Is A.A^-1 equal to identity matrix?->",y)

# 2. Prove AB ̸= BA.
import numpy as np
A=np.array([[3,4],[7,8]])
B=np.array([[5,3],[2,1]])
AB = np.dot(A, B)
BA = np.dot(B, A)
print("\n AB (A * B):\n", AB)
print("\n BA (B * A):\n", BA)
are_equal=np.array_equal(AB,BA)
print("\n  Is AB = BA? ",are_equal)

# 3. Prove (AB)^T = B^T*A^T
import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
AB=np.dot(A,B)
AB_T=AB.T
B_T=B.T
A_T=A.T
BT_AT=np.dot(B_T,A_T)
print("\n AB:\n", AB)
print("\n (AB)^T:\n", AB_T)
print("\n B^T:\n", B_T)
print("\n A^T:\n", A_T)
print("\n B^T * A^T:\n", BT_AT)
is_equal=np.array_equal(AB_T,BT_AT)
print("\n Is (AB)^T equal to B^T * A^T? ", is_equal)

# Solve the following system of Linear equation using Inverse Methods.

# 2x − 3y + z = −1
# x − y + 2z = −3
# 3x + y − z = 9
# {Hint: First use Numpy array to represent the equation in Matrix form. Then Solve for: AX = B}

import numpy as np
A=np.array([[2,-3,1], [1,-1,2], [3,1,-1]])
B=np.array([-1,-3,9])
A_inv=np.linalg.inv(A)
x=np.dot(A_inv,B)
print("\n Coefficient Matrix (A):\n", A)
print("\n Constants Vector (B):\n", B)
print("\n Inverse of A (A^-1):\n", A_inv)
print("\n Solution Vector (X):\n", x)

# 4.2 Experiment: How Fast is Numpy?
# In this exercise, you will compare the performance and implementation of operations using plain Python
# lists (arrays) and NumPy arrays. Follow the instructions:
# 1. Element-wise Addition:
# • Using Python Lists, perform element-wise addition of two lists of size 1, 000, 000. Measure
# and Print the time taken for this operation.
# • Using Numpy Arrays, Repeat the calculation and measure and print the time taken for this
# operation.

import numpy as np
import time
list1=list(range(1,1000001))
list2=list(range(1,1000001))
start_time= time.time()
result_list=[a+b for a, b in zip(list1,list2)]
python_time=time.time()-start_time
print("\n Time taken for element-wise addition using Python lists:", python_time, "seconds")
#numpy arrays:
arr1=np.arange(1,1000001)
arr2=np.arange(1,1000001)

start_time=time.time()
result_array=arr1+arr2
numpy_time=time.time()-start_time
print("\n Time taken for element-wise addition using NumPy arrays:", numpy_time, "seconds")

# 2. Element-wise Multiplication

# • Using Python Lists, perform element-wise multiplication of two lists of size 1, 000, 000. Mea-
# sure and Print the time taken for this operation.

# • Using Numpy Arrays, Repeat the calculation and measure and print the time taken for this
# operation.

import numpy as np
import time
list1=list(range(1,1000001))
list2=list(range(1,1000001))
start_time=time.time()
result_list=[a*b for a,b in zip(list1,list2)]
python_time=time.time()-start_time
print("\n Time taken for element-wise multiplication using Python lists:", python_time, "seconds")

# NumPy arrays:
arr1 = np.arange(1, 1000001)
arr2 = np.arange(1, 1000001)

start_time = time.time()
result_array = arr1 * arr2
numpy_time = time.time() - start_time
print("\n Time taken for element-wise multiplication using NumPy arrays:", numpy_time, "seconds")

# 3. Dot Product
# • Using Python Lists, compute the dot product of two lists of size 1, 000, 000. Measure and
# Print the time taken for this operation.
# • Using Numpy Arrays, Repeat the calculation and measure and print the time taken for this
# operation.

import numpy as np
import time

list1 = list(range(1, 1000001))
list2 = list(range(1, 1000001))
start_time = time.time()
dot_product_list = sum(a * b for a, b in zip(list1, list2))
python_time = time.time() - start_time
print("\n Time taken for dot product using Python lists:", python_time, "seconds")
arr1 = np.arange(1, 1000001)
arr2 = np.arange(1, 1000001)

# dot product using NumPy arrays
start_time = time.time()
dot_product_numpy = np.dot(arr1, arr2)
numpy_time = time.time() - start_time
print("\n Time taken for dot product using NumPy arrays: ", numpy_time, "seconds")

# 4. Matrix Multiplication
# • Using Python lists, perform matrix multiplication of two matrices of size 1000x1000. Measure
# and print the time taken for this operation.
# • Using NumPy arrays, perform matrix multiplication of two matrices of size 1000x1000. Mea-
# sure and print the time taken for this operation.

import numpy as np
import time


matrix1 = [[i for i in range(1000)] for j in range(1000)]
matrix2 = [[i for i in range(1000)] for j in range(1000)]


start_time = time.time()

result_matrix = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(1000)) for j in range(1000)] for i in range(1000)]

python_time = time.time() - start_time
print("Time taken for matrix multiplication using Python lists: ", python_time, "seconds")

# Matrix multiplication using NumPy
matrix1_np = np.random.rand(1000, 1000)
matrix2_np = np.random.rand(1000, 1000)

start_time = time.time()

result_matrix_np = np.dot(matrix1_np, matrix2_np)

numpy_time = time.time() - start_time
print("Time taken for matrix multiplication using NumPy arrays: ", numpy_time, "seconds")