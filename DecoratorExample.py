# Methods and functions are callable. Any object which implements special method __call__() is termed as callable.
# So, in the most basic sense, a decorator is a callable that returns a callable.
# Basically, a decorator takes in a function, adds some functionality and returns it.

def my_decorator(func):
    def wrapper():
        print("Function func getting decorated")
        func()
        print("Function func got decorated")

    return wrapper


def ordinary():
    print("I am ordinary")


just_some_function = my_decorator(ordinary)
just_some_function()

print("="*20)
# Syntactic sugar: Python allows to simplify calling of decorator using @ (this is called "pie" syntax)
@my_decorator
def exampleFunc():
    print("I am another function.")

exampleFunc()
'''
The above statement is equivalent to:
exampleFunc = my_decorator(exampleFunc)
exampleFunc()
'''

# Decorating functions with parameters
print("="*50)
print("-----Example of decorating functions with parameters-----")

def smart_divide(func):

    def wrapper(x, y):
        if y==0:
            print("Whoops! cannot divide")
            return      #returns None
        return func(x,y)
    return wrapper

@smart_divide
def divide(a,b):
    return (a/b)

print(divide(10,2))
print(divide(10,0))         #returns None

# Another way of decorating functions with parameters is using *args abd **kwargs
print("---Real world example of decorator, to calculate time taken to run a function---")
print("----Example of decorating parameterized function using *args and *kwargs----")

import time
def timeDecorator(func):

    def wrapper(*args, **kwargs):
        print("Calling function with variable parameter list.")
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time()
        print("Time it took to run the function: " , t2-t1)

    return wrapper

print("---------------")
@timeDecorator
def sumOfList(len):
    sum=0
    for i in range(0,len):
        sum=sum + i
    print("Output of sumofList function", sum)

sumOfList(10000)
print("---------------")
@timeDecorator
def getVoltage(current, resistance):
    voltage = current*resistance
    print("Voltage = ", voltage)

getVoltage(current=1, resistance=100)

#################################################################################
# Decorator Chaining
print("="*70)
print("--- Example of decorator chaining ---")

def star(func):
    def inner(msg):
        print("*"*30)
        func(msg)
        print("*"*30)
    return inner

def percent(func):
    def inner(msg):
        print("%"*30)
        func(msg)
        print("%"*30)

    return inner

@star
@percent        # The order in which we chain decorators matter.
def printer(msg):
    print(msg)
    
printer("Hello!!!")
## The above statements are equivalent to;
## printer = star(percent(printer("Hello!!!")))
