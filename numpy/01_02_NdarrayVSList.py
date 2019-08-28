import numpy as np

print("-"*50)
print("--------- Numpy ndarray -----------------")
a=np.arange(3)
for it in np.nditer(a,op_flags=["readwrite"]):
    print(type(it))
    print(it[...])  ## as 'it' is of type ndarray, it[...] gives ndarray
    # containing single value (current element pointed by iter)


print("-"*50)
print("--------- Python list -------------------")
l = list(range(3))
for x in iter(l):
    print(type(x))
    #print(x[...])  ## as type of x is int, it cnnot be represented by x[...]


print("="*50)
print("--------- Slicing of ndarray ------------")
B = np.arange(12).reshape(2,3,2)
print("******* Multi-dimensional ndarray B:\n", B)
print("******* B[...]\n",B[...])            ## similar to B[:,:,:]
print("******* B[0,...]\n",B[0,...])        ## similar to B[0,:,:]
print("******* B[0,...,0]\n",B[0,...,0])    ## similar to B[0,:,0]
print("******* B[...,0]\n",B[...,0])        ## similar to B[:,:,0]

## ... is only applicable on numpy arrays, not on Python lists

print("="*50)
print("--------- Update sliced part and see the changes ------------")
C=B[0,:,0]
C[:] = 1000
print("C: ",C)
print("Value of ndarray B after updating sliced part of B\n", B)


D=[10,20,30]
E=D[0:1]
E[:] = [1000,1000]
#print(type(E))
print("Value of Python list D after updating sliced part of D: ",D)
