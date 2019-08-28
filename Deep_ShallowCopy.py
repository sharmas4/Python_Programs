##### Example 1 #######
x=[1,2,3,4]
y=x			#the statement is used to copy. It copies the reference to object, pointed by x to name y. So, new variable y and old x shares the reference. Both points to same memory location. And as x is mutable, any change made to x will still be stored at the same location (unlike for immutable objects), change will be reflected to y also. Similarly, any change made to y will be reflected to xrange
x.append(100)
print("x = ",x)
print("y = ",y)
y.append(200)
print("x = ",x)
print("y = ",y)
print("y is x: ", (y is x))		# The ‘is’ operator compares the identity of two objects; the id() function returns an integer representing its identity.
################################################################################
#To avoid the above scenario
z=x[:]				### First way to create shallow copy	##works fine with single dimensional list but fails with multi dimensional list as shown in the below example of shallow list
print("z is x: ", z is x)
x.append(300)
print(x)

L=100
M=L
L=L+1
print("L = " , L)
print("M = ",  M)		#Value of L and M won't be same because L is storing immutable object. Therefore, after L=L+1, L is stored at different location. But M still points to the earlier location.
##################################################################################
##################################################################################


################################# SHALLOW COPY ###################################
# A shallow copy creates a new object which stores the reference of the original elements. So, a shallow copy doesn't create a copy of nested objects, instead it just copies the reference of nested objects.
# Making a shallow copy of an object won’t clone child objects. Therefore, the copy is not fully independent of the original.
import copy

oldL = [1,2,3,4]
newL = copy.copy(oldL)		#second way of creating shallow copy
oldL.append(100)
oldL[1] = 1000
print("OldL = ", oldL)
print("newL = ",newL)		#newL remains unchanged

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)

print("Old list:", old_list)
print("New list:", new_list)

old_list.append([4, 4, 4])

print("Old list after appending old_list :", old_list)			# [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
print("New list after appending old_list :", new_list)			# [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

old_list[1][1] = 'AA'
print("Old list after updating an element of old_list :", old_list)			# [[1, 1, 1], [2, 'AA', 2], [3, 3, 3], [4, 4, 4]]
print("New list after updating an element of old_list :", new_list)			# [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]]

### Third way of creating shallow copy
newL = list(oldL)
# newDict = dict(oldDict)
# newSet = set(oldSet)

################################# DEEP COPY ######################################
# A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.
# A deep copy of an object will recursively clone child objects. The clone is fully independent of the original, but creating a deep copy is slower.
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

old_list[1][0] = 'BB'

print("Old list:", old_list)
print("New Deep copy list:", new_list)



#################################################################################################################################
#################################################################################################################################
# copy custom class example
print('############################## Copy of custom Class Example ###############################')
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def __repr__(self):			
		return 'Output of __repr__ of Point: Point(%s, %s)' %(self.x, self.y)
	
	def __str__(self):
		return 'Output of __str__ of Point: (%s, %s)' %(self.x, self.y)

obj1Point = Point(10, 20)
obj2Point = copy.copy(obj1Point)
print(obj1Point)		# prints output of __str__. If __str__ is not present, prints return value of __repr__. If both are not present, something like this will be printed <__main__.Point object at 0x0000000004CD9278>
print(obj2Point)
print('obj2Point is obj1Point: ', obj2Point is obj1Point)		# The output is as expected in case of shallow copy because Point object uses primitive types (ins) for its coordinates. There’s no difference between a shallow and a deep copy in this case.


class Rectangle:
	def __init__(self, topLeft, bottomRight):
		self.topLeft = topLeft
		self.bottomRight = bottomRight
	
	def __repr__(self):
		return 'Rectangle({0}, {1})'.format(self.topLeft, self.bottomRight)
		
obj1Rec = Rectangle(Point(0,5), Point(5,0))
obj2Rec = copy.copy(obj1Rec)
print(obj1Rec)
print(obj2Rec)
print('obj2Rec is obj1Rec', obj2Rec is obj1Rec)
print('Changing one of the coordinate of obj1Rec')
obj1Rec.topLeft.y = 10		#changes reflect to obj2Rec too
print('obj1Rec after changing y coordinate of topLeft point: ',obj1Rec)
print('obj2Rec after changing y coordinate of topLeft point: ', obj2Rec)	
		
		