import numpy as np

x=np.array([10,20])
y=np.array([30,40])

z= np.concatenate((x,y))
#Cannot concatenate over axis=1 for one dimensonal array
print("Concatenate : ",z)

m = np.array([[1,2],[3,4]])
n = np.array([[100,200],[300,400]])

print("Concatenate over axis 0 : ",np.concatenate((m,n),axis=0))
print("Concatenate over axis 1 : ",np.concatenate((m,n),axis=1))

print("*"*75)
print("reshape array: \n",m," to 1*4 : ",m.reshape((1,4)))

print("*"*75)
print("============Vector Stacking===============")
A = np.array([3, 4, 5])
B = np.array([1,9,0])
print("Row Stack: ",np.row_stack((A, B)),
      "\nWhereas, concatenate will result in :", np.concatenate((A,B)))
#print(np.column_stack((A, B)))
print("Column Stack : \n",np.column_stack((A,B)))


## to create a new matrix by repeating an existing matrix multiple times
## to create a new matrix with a different shape or even dimension.

l = np.array([[1,2],[3,4]])
print("TIle : \n",np.tile(l,(3,4)))
