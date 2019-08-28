import numpy as np

# The array data structure provided by Numpy has advantages over Python lists,
# such as: being more compact, faster access in reading and writing items,
# being more convenient and more efficient
# numpy arrays are also called ndarray

np.set_printoptions(legacy="1.13")

# To create uninitialized array
print(np.empty((2,3)))  #will create array initialized with garbage (many a times similar to np.zeros())
# empty() is seldom used bcz we need to set all of its values again

#np.idenity() creates identity atrix
#print("np.eye(3,3,-1)----------\n",np.eye(3,3,-1))   #with eye diagonal can be made offset (-1 is offset)
#print("np.eye(4,3,-1)----------\n",np.eye(4,3,-1))
#print("np.dentity(3)-----------\n",np.identity(3))

#x=np.ones((2,3),dtype=int), x=np.zeros((2,3),dtype=int)
## There is another interesting way to create an array with Ones or with Zeros,
## if it has to have the same shape as another existing array 'a'.
## Numpy supplies for this purpose the methods ones_like(a) and zeros_like(a)

#x=np.array([1,2,3,4,5])
#E=np.ones_like(x)   ## similarly, Z=np.zeros_like(x)
#print(E)



##a slicing operation on an array creates a view on the original array. So we
##get another possibility to access the array, or better a part of the array.
##From this follows that if we modify a view, the original array will be
##modified as well.

print("*"*75)
print("Slicing of a Numpy array")
A=np.array([1,2,3,4,5,6])
print("Original A is ", A)
B=A[1:4]
B[0]=10
print("B (sliced from A) is ", B)
print("On updating a value in B, now A is ", A)
print("Does B share memory with A? ",np.may_share_memory(A,B))#returns True, if they overlap, they may or may not be same.


#####################  Copying arrays  ###################
x=np.array([[42,22,12],[44,53,66]])
y=x.copy()
## x.copy(order="C") is for C type formatting which is ROW MAJOR
## x.copy(order="F") is for Fortran type formatting which is COLUMN MAJOR
print("x = ", x)
print("y = ", y)
x[0,0] = 1000
print("updated x = " , x)
print("y after update in x = ", y)

## Boolean array indexing: Boolean array indexing lets you pick out
## arbitrary elements of an array
a = np.array([[1,2], [3, 4], [5, 6]])
bool_idx = (a>2)
print("bool_idx", bool_idx)
print("Elements of array a which fulfils condition of bool_idx: ",a[bool_idx])

print("full() function usage: ", np.full((2,2), 7)) #creates a constant array
print("Array filled with random values: ", np.random.random((2,2)))

