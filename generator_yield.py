### yield and generator
'''
The yield keyword in Python is used to create generators. #
A generator is a type of collection that produces items on-the-fly
and can only be iterated once. By using generators you can improve
your application's performance and consume less memory
as compared to normal collections, so it provides a nice boost in performance.
'''
### Difference between list and generator
squared_List = [x**2 for x in range(5)]
print("type(squared_List) ---- " , type(squared_List))
print("Iterate over list --- ")
for i in squared_List:
    print("list value- " , i)

squared_gen = (x**2 for x in range(5))
print("type(squared_gen) ---- " , type(squared_gen))
print("Iterate over generator --- ")
for i in squared_gen:
    print("gen value- " , i)

print("Trying to print generator again!!!")
for i in squared_gen:
    print("gen value 2 - " , i)
## Generator can be iterated over only once.
#It didn't iterate again whne we tried to do so

#print(len(squared_gen))    #throws an error that a generator has no length
'''
The output is the same as that of the list.
One of the main differences lies in the way the list and generators
store elements in the memory. Lists store all of the elements in memory at once,
whereas generators "create" each item on-the-fly, displays it, and then
moves to the next element, discarding the previous element from the memory.
'''

################### Turn regular function into a generator  ###############
def cube_generator(nums):
    for i in nums:
        yield(i**3)

cubes = cube_generator([1,2,3,4,5])
print("Ouput of cube_generator function --- " , cubes)  #  function returns a generator instead of list of cubed number
# yield is used to create generator

"""
Even though we called the cube_numbers function, it doesn't actually execute
at this point in time, and there are not yet any items stored in memory.
To get the function to execute, and therefore the next item from generator,
we use the built-in next method. When you call the next iterator
on the generator for the first time, the function is executed until the
yield keyword is encountered. Once yield is found the value passed to it
is returned to the calling function and the generator function is paused
in its current state.
"""
print("iterate over first value of generator - ",next(cubes))
'''
Now when you call next again on the generator, the cube_numbers function will
resume executing from where it stopped previously at yield. The function will
continue to execute until it finds yield again. The next function will keep
returning cubed value one by one until all the values in the list are iterated.

cubes generator doesn't store any of these items in memory, rather the cubed
values are computed at runtime, returned, and forgotten. The only extra
memory used is the state data for the generator itself, which is usually
much less than a large list. This makes generators ideal for memory-intensive
tasks.
'''
##iterate over generator
for i in cubes:
    print("Value by generator function --" , i)
