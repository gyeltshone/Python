# def reverse(x):
  
#     reverseNumber = str(x)
#     num = ''
#     while len(reverseNumber) > 0:
        
#         reverseNum = int(reverseNumber)%10
#         reverseNumber = int(reverseNumber)//10
#         num+=str(reverseNum)
        
#     return int(num)
        

    
# print(reverse(123))

def reverse(x):
       MIN_INT = -2**31
       MAX_INT = 2**31 - 1

       if x < 0:
            
            num = str(abs(x) )# return positive number
            reverseNumber = num[::-1]
            reverse_str =  int(reverseNumber) * -1
            if reverse_str < MIN_INT or reverse_str > MAX_INT:
                  return 0
            return reverse_str 
       else:
            num = str(abs(x) )# return positive number
            reverseNumber = num[::-1]
            reverse_str =  int(reverseNumber)
            if reverse_str < MIN_INT or reverse_str > MAX_INT:
                  return 0
            return reverse_str
            
   
    
            
   
print(reverse(1534236469))




# print(123%10)