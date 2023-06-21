def twoSum( nums, target):
    index = []

    for i in range(len(nums)):
        for j in range(len(nums)):
           
            if nums[i]!=nums[j]:
                
                if nums[i]+nums[j] == target:
                    index.append(i)
                    index.append(j)
                    return index
               
              
print(twoSum(nums=[3,2,4],target=6))