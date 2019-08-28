import numpy as np

## Adding scalar to each element of array
lst = [1,2,3,4]
a = np.array(lst)
a = a + 2
print("a + 2 = ", a)
b=np.array([2, 4, 3.2])
print("b + 2 = ", b+2)
## similarly, a*2, a-2, a**2

c=np.array([1,2,3,4])   ## order of both arrays should be same, else exception
# would be thrown
print("a*c = ", a*c)    # it is not Matrix Multiplication

dotProd = np.dot(a,c)   # For 1-D arrays dot product is the same as the inner product of vectors
print(dotProd)  

## matrix Multiplication can be calculated by doct product
X = np.array([ [11, 12, 13], [21, 22, 23], [31, 32, 33] ])
Y = np.ones((3,3))
print("Matrix multiplication / dot product of X and Y is: \n", np.dot(X,Y))

## Real matrices.
## We get real matrix multiplication by multiplying two matrices, but the
# two-dimensional arrays will be only multiplied component-wise:
print("\n", "*"*75)
print("ndarray vs Matrix")
A = np.array([ [1, 2, 3], [2, 2, 2], [3, 3, 3] ])
B = np.array([ [3, 2, 1], [1, 2, 3], [-1, -2, -3] ])
print("Multiplication of ndarrays: \n", A*B)
MA=np.mat(A)
MB = np.mat(B)
print("Multiplication of matrices: \n", MA*MB)

## For matrix multiplication, one can use np.dot(x,y)

############### Comparision operator ###############
print("\n", "*"*75)
print("Comparision Operator")
print("A==B:\n", A==B)
print("array_equal for comparison: ", np.array_equal(A,B))
