#################################
from collections import deque		# Required only for Queue
#List as Queue
a= deque([12, 34, 'Swati', 'Sharma'])	## a is deque now, not list
#type(a) = <class 'collections.deque'>
a.append(100)
print('Value of a after pushing/appending in stack' + str(a))
a.popleft()
print('Value of a after popping out value' + str(a))

#Using list as Stack
a= [12, 34, 'Swati', 'Sharma']
a.append(100)
print('Value of a after pushing/appending in stack' + str(a))
a.pop()
print('Value of a after popping out value' + str(a))



