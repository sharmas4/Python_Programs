'''
Masked arrays are arrays that may have missing or invalid entries.
In many circumstances, datasets can be incomplete or tainted by the presence
of invalid data. For example, a sensor may have failed to record a data, or
recorded an invalid value. The numpy.ma module provides a convenient way to
address this issue, by introducing masked arrays.

A masked array is the combination of a standard numpy.ndarray and a mask. A
mask is either nomask, indicating that no value of the associated array is
invalid, or an array of booleans that determines for each element of the
associated array whether the value is valid or not. When an element of the
mask is False, the corresponding element of the associated array is valid and
is said to be unmasked. When an element of the mask is True, the corresponding
element of the associated array is said to be masked (invalid).

The package ensures that masked entries are not used in computations.
Masked array is introduced by numpy.ma module
'''

import numpy as np
import numpy.ma as ma
x=np.array([1, 2, 3, -1, 5])
# we wish to mark 4th entry as invalid. Easiest way to create a masked array:

mx=ma.masked_array(x,mask=[0, 0, 0, 1, 0])

# another way to construct masked array
y = ma.array([1, 2, 3], mask=[0,1,0])
print("y: " , y, "------ typeof y is ", type(y) )
#now, when we compute mean of the dataset, invalid data (4th element) will be ignored
print("Mean of masked array: ",mx.mean())   # mean() is ndarray object's method
# print(np.array([1,2,3,5]).mean())

# numpy.ma module has class maskedArray which is subclass of ndarray


#################################################################
#####masked arrays can also be created using following functions:

# fix-invalid returns input with invalid data masked and replaced by a fill value.
print("--------- Example 1: use of fix_invalid() ---------")
x=ma.array([1, 2, np.nan, np.inf], mask = [1] + [0]*3)
print("Masked array is: ",x)
print("x.data: ",x.data," ---- x.mask: ", x.mask, " ---- x.fill_value: ",x.fill_value)
y = ma.fix_invalid(x)       ## it masks all invalid data like inf and nan along with original mask
print("ma.fix_invalid(x) : " , y)
z=ma.fix_invalid(x,fill_value=1000)
print("z.data: ",z.data," ---- z.mask: ", z.mask, " ---- z.fill_value: ",z.fill_value)


##masked_equal(): mask array when equal to a given value
a = np.arange(4)
m_equal = ma.masked_equal(a,2)
print("--------- Example 2: use of masked_equal() ---------")
print("a: ",a, "------- ma.masked_equal(a): ",m_equal)


##masked_greater(): mask array where greater than a given value
a = np.arange(5)
m_greater = ma.masked_greater(a,2)
print("--------- Example 3: use of masked_greater() ---------")
print("a: ",a, "------- ma.masked_greater(a): ",m_greater)


##masked_greater_equal(): mask array where greater than a given value
a = np.arange(5)
m_greater_equal = ma.masked_greater_equal(a,2)
print("--------- Example 4: use of masked_greater_equal() ---------")
print("a: ",a, "------- ma.masked_greater_equal(a): ",m_greater_equal)



'''
Other methods are:
1. masked_inside(x, v1, v2[, copy])	Mask an array inside a given interval (v1,v2), including v1 and v2
copy is a boolean. True: to use copy of x. False: to fix x in place.
copy variable is available in each of the above methodsa and in the following method too

2. masked_invalid(a[, copy]): Mask an array where invalid values occur (NaNs or infs)


3. masked_less(x, value[, copy])	Mask an array where less than a given value.
4. masked_less_equal(x, value[, copy])	Mask an array where less than or equal to a given value.
5. masked_not_equal(x, value[, copy])	Mask an array where not equal to a given value.
6. masked_outside(x, v1, v2[, copy])	Mask an array outside a given interval, excludng v1 and v2

'''
# 7. numpy.ma.masked_object
print("--------- Example 5: use of masked_object() ---------")

food = np.array(['green_eggs', 'ham'], dtype=object)
## it is required to specify type as object to perform masked_object
eat = ma.masked_object(food, "green_eggs")
print("result of masked_object is : ",eat)
                       
'''
8. numpy.ma.masked_values(x, value, rtol=1e-05, atol=1e-08, copy=True, shrink=True)
Mask using floating point equality.
Return a MaskedArray, masked where the data in array x are approximately
equal to value.
9. masked_where(condition, a[, copy])	Mask an array where a condition is met.
'''

x = ma.array([1, 2, 3])
x[0] = ma.masked
print("*"*50)
print("--------- Example 6: masking an entry ---------")
print("masked x is ",x)
x.mask = True
print("mask all values:",x)

print("--------- Example 7: masking an entry ---------")
y = ma.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Values to be masked: ",y[(0,1,2),(1,2,0)])
y[(0,1,2),(1,2,0)] = ma.masked
print("Masked array:\n",y)
print("mask all values: ")


print("*"*50)
print("--------- Example 8: Unmasking an entry ---------")
x=ma.array([1,2,3], mask=[0,1,1])
print("Masked array:",x)
# To unmask one or several specific entries, we can just assign one or
# several new valid values to them
x[1] = 5
print("Unmasked array:",x)
'''
Unmasking an entry by direct assignment will silently fail if the masked array
has a hard mask, as shown by the hardmask attribute. This feature was introduced
to prevent overwriting the mask. To force the unmasking of an entry where the
array has a hard mask, the mask must first to be softened using the soften_mask
method before the allocation. It can be re-hardened with harden_mask
'''
x = ma.array([1, 2, 3], mask=[0, 1, 1], hard_mask=True)
x[-1] = 1
print("Unmasking hard mask:", x)
x.soften_mask()
x[-1] = 1
print("Unmasking soft mask:",x)
x.harden_mask()


# To check if a value of an masked_array is masked or not
print("Is x[1] masked:", x[1] is ma.masked)
print("Is x[1] masked:", x[-1] is ma.masked)
if x[1] is ma.masked:
    print("Example to fill a value in place of all masked values in array x")
    x= x.filled(100)
print("After filling, x is ",x)
y = ma.masked_array([(1,2), (3, 4)]
                    ,mask=[(0, 0), (0, 1)]
                    ,dtype=[('a', int), ('b', int)])
print(y[-1])


x = ma.array([1., -1., 3., 4., 5., 6.], mask=[0,0,0,0,1,0])
y = ma.array([1., 2., 0., 4., 5., 6.], mask=[0,0,0,0,0,1])
print("Squareroot after division",np.sqrt(x/y))     #gives setup warning, not exception
'''
Numerical operations can be easily performed without worrying about missing
values, dividing by zero, square roots of negative numbers, etc.
Four values of the output are invalid: the first one comes from taking the
square root of a negative number, the second from the division by zero, and the
last two where the inputs were masked.
'''





