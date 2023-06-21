def reverse(x):
    MIN = -2 **31
    MAX =(2**31) -1
    sums = 0
    isneg = False
    if x < 0 :
        isneg = True
        x = abs(x)
    while  x > 0:
        rev = x % 10
        x = x // 10
        sums = sums * 10 +  rev
    if sums  < MIN or sums > MAX:
            return 0
    if isneg:
         sums = -sums
         return sums
    return sums
    
print (reverse(-123))


def isPalindrome( x: int) -> bool:
    MIN = -2**31
    MAX= 2**31 -1

    original_num = x
    sums = 0
    if x > MIN  or  x < MAX:
        
    
        if x < 0 :
            return False
        while x > 0:
            reminder = x % 10
            x = x // 10
            sums = sums * 10 + reminder
            
    
    if original_num == sums :
        return True
print(isPalindrome(121))

def arrayString(string):
     ar = string
     firstchar = list(map(lambda ar:ar[:3],ar))
     return firstchar


print(arrayString(["flower","flow","flight"]))