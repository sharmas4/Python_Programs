######### Usage of lookAround regex

## You want to ensure that a password meets a set of criteria.
# The password should be between 8 and 15 characters,
#contain at least one upper-case alpha character,
#contain at least one lower-case alpha character, contain at least one digit,
#and contain at least one of the following:  $, %, #, @, &.
import re

reg = r'^(?=.*[A-Z])(?=.*[0-9])(?=.*[$%#@&])(?=.*[a-z]).{8,15}$'

matchStr = "1e@jdAASD"

print(re.match(reg, matchStr).group())


##### You want to find the integer portion of a decimal number within text. You
#have a peculiar requirement that you only want values if they have a decimal part.
intVal = "12.34"
reg2 = r'\d+(?=\.\d+)'

print(re.match(reg2, intVal).group())




