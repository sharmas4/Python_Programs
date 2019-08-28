'''
__init__ is not a constructor. The function __init__() is called immediately
after the object is created and is used to initialize it.
Constructor in Python is __new__()
syntax of __new__:    __new__(cls, *args, **kwargs)
__new__ is always called before __init__()

'''

class Point(object):
    
    def __new__(cls,*args,**kwargs):
        print("\n************ From new")
        print("cls: ",cls)
        print("args:",args)
        print("kwargs:",kwargs)

        #create Point object and return it
        obj = super().__new__(cls)  #super() points to base class "object".
        # Here, __new__ of "object" class is called 
        return obj

    def __init__(self, x=0, y=0):
        print("************ From init")
        self.x=y
        self.y=y

P1 = Point(3,4)
print("Point object P1: ",P1)

'''
One practical use of __new__() however, could be to restrict the number of
objects created from a class. Suppose we wanted a class SqPoint for creating
instances to represent the four vertices of a square. We can inherit from our
previous class Point (first example in this article) and use __new__() to
implement this restriction.
'''
class SquareVertices(Point):
    MAX_Instances = 4
    instances_created = 0

    def __new__(cls,*args,**kwargs):
        if cls.instances_created >= cls.MAX_Instances:
            raise ValueError("Cannot create more objects!!!")
        cls.instances_created += 1
        return super().__new__(cls)     #this will work even if __new__ is not
        # explicitly defined in Point class # inherit either user defined class
        # or "object" 
        
sqrV1 = SquareVertices(0,0)
#print(sqrV1)
sqrV2 = SquareVertices(0,2)
sqrV3 = SquareVertices(2,0)
sqrV3 = SquareVertices(2,2)
#sqrV4 = SquareVertices(2,0)    # this will raise ValueError

