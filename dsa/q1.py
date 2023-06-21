



# def indices_sum(nums,target):
#     for i in range(0,len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i]+nums[j] == target: 
#                 print('Flavous',nums[i],'and',nums[j])
# nums=[1,3,4,5,6]
# target=6
# indices_sum(nums,target)
     
   
     
        


    

   
# n = 5




# while(odd):
#      steps = 0 

#      proc = 3 * n  + 1
#      if proc == even:
          
      

# while(even):
#     steps = 0
#     reminder = even / 2
#     steps += 1




def check(number):
    even = number % 2 == 0
    odd = number % 2 == 1
    steps = 0
    if number == 1:
        return 
    
    while odd:
        steps +=1
        num  = 3 * number + 1
        if num == even:

            number = number/2

        print(steps)

    while even:
        if number == 1:
            steps +=1
            break
        number = number /2

        steps += 1
        print(steps)

     
        
        
    
print(check(16))
    
        
       


    


    
    


    


