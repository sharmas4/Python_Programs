class MyClass:
    @staticmethod   ## static method can be called from an instance or a class
    def stat_meth():
        print("Look no self was passed")
    a = 10		# class variable shared by all instances
	
    def fn(self):   # self is representaion of object inside class
        print("Hello");


		
print(MyClass.a)
## print(MyClass.fn())		# will throw error as no object of MyClass is
#specified for self. Rather use MyClass obj to call this method like below
x = MyClass()
x.fn()						## x.fn is a method object
x.stat_meth()
y = MyClass()
y.stat_meth()

# Each value is an object, and therefore has a class (also called its type,
## obtained by type(x)). It is stored as "object.__class__"
print('x.__class__ = ' + str(x.__class__))	#Same is obtained by str(type(x))		#OUTPUT: <class '__main__.MyClass'>
print('type(MyClass) = ' + str(type(MyClass)))			#OUTPUT: <class 'type'>

print('value of x.a ' + str(x.a))
print('value of y.a ' + str(y.a))
x.a=100
print('value of x.a after update ' + str(x.a))
print('value of y.a after update ' + str(y.a))  ## only value of x.a is changed

MyClass.fn(MyClass)			## MyClass.fn is a function object
print(MyClass.__doc__)

print('type(MyClass.fn): ',type(MyClass.fn))
objMyClass = MyClass()
print('type(objMyClass.fn): ',type(objMyClass.fn))
## A peculiar thing about methods (in Python) is that the object itself is
# passed on as the first argument to the corresponding function. 
## we can write anything "xyz" in place of "self", to represent object inside classs
class ComplexNumber:
	def __init__(self,x=0,y=0):
		self.x = x
		self.y = y
	def displayData(self):
		print('{0} + {1}j is the complex number'.format(self.x, self.y))
		
obj = ComplexNumber()
obj.displayData()
obj1 = ComplexNumber(2, 5)
obj1.displayData()
obj.attr = 100		# attributes of an object can be created on the fly.
                        # But this attribute is only for obj, not for obj1
print(obj.x, obj.y,obj.attr)

# attributes (variable or method) of an object can be deleted
del obj1.x			# deletes attribute x for obj1 only
# print(obj1.x)  	# this statement will throw error
print(obj.x, obj.y)

# can delete object also
del obj1
# obj1.displayData() 		# throws error




#### Mutable objects are better not to be used as shared variable 
class Dog:
	tricks = []
	z = 30
	def __init__(self, name):
		self.name = name
	
	def add_tricks(self,tricks, z):
		self.tricks.append(tricks)
		self.z = self.z + z
	
d = Dog('Fido')
print("-- --d (before calling init() over it)",d.name, id(d))
ret = d.__init__("TESTING")   ## __init__() can be called separately too. 
print("-----d (after calling init over it)",d.name,id(d))
print("---------------- ret ", type(ret))       ## init() returns None (always)
d.add_tricks('roll over', 100)

e = Dog('Buddy')
e.add_tricks('play dead', 200)

print('Value of mutable list tricks for dog d ' + str(d.tricks))
print('Value of immutable z for dog d ' + str(d.z))
print('Value of immutable z for dog e ' + str(e.z))

# In the above example, mutable attribute tricks is unexpectedly shared by all Dog instances

# to avoid this,
"""
class Dog:
	z = 30
	def __init__(self, name):
		self.name = name
		self.tricks = []		### initailise tricks inside constructor

"""


# Class can be defined in a shorter way using namedtuple
from collections import namedtuple
car = namedtuple("CarClass", "Color1 Mileage2")
carObj = car("Red", "100")              #Notice that object is created using "car" name. But on printing carObj, CarClass is considered as class
print(carObj)           #prints CarClass(Color1='Red', Mileage2='100') 
print("carObj Color: ", carObj.Color1)
print("carObj Mileage: ", carObj.Mileage2)


class A:
    def fn(self,b=0):
        self.b=b
        print("I am in A: ", b)

a = A()
a.fn(100)
