def sum_number(num):
    if num == 0:
        return 0

    return (num%10 + sum_number(num//10))
print(sum_number(112))


def num(n):
    sum_number  = 0
    while n > 0:
         lastnum = n % 10
         n = n//10
         sum_number += lastnum
         return sum_number
   
            

   
print((num(124)))

