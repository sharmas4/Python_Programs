## The default pseudo-random number generator of the random module was
## designed with the focus on modelling and simulation, not on security.
## So, you shouldn't generate sensitive information such as passwords,
## secure tokens, session keys and similar things by using random.
## The SystemRandom class of the random module offers a suitable way to overcome this security
## problem. The methods of this class use an alternate random number generator,
## which uses tools provided by the operating system (such as /dev/urandom
## on Unix or CryptGenRandom on Windows.

## One can also use "secret' module on Python 3.6+

import random
random_number = random.random()
print("Rando Number using random function of random module(not a secure way)",
      random_number)

print("Secure way of generating random number")
from random import SystemRandom
crypto = SystemRandom()
print("Create random float number >=0 and <1 using random function of \
SystemRandom class: ", crypto.random())

print("Generate a list of random numbers")
