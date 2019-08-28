def palindrome(testCase):
    forwardPtr = 0
    backwardPtr = len(testCase) - 1
    while (forwardPtr >= backwardPtr):
        if testCase[forwardPtr] is not testCase[backwardPtr]:
            return False
        forwardPtr+=1
        backwardPtr-=1
    return True

print(palindrome("madam"))

        
