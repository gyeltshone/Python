# num = [1,1,2,3,44,44,5]

# class RemoveDuplicates:

#     def remove_duplicates(self,values):

#         return (list(dict.fromkeys(values,)))
    
# value  = RemoveDuplicates()
# duplicate = value.remove_duplicates(num)
# print(duplicate)

# my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# class Dictionary:
#     def dectornary (self,data):
#         details = [{key:value} for key,value in data.items() ]
#         return details
    
# datas = Dictionary()
# print(datas.dectornary(my_dict))
    
# print("another method")

# for key,value in enumerate(my_dict):
#     print(key,value)

# print("two sum ")

def two_sum(targe,num):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            diff = targe - num[i]
            newarr =num[j:]
            if diff in newarr:
                return   [i,j]
        

print('longest palindromic substring')

# def palimdromic(s):

#     result = ""
#     maxLength = 0 

#     for i in range(len(s)):
#         # fro odd length of string
#         left, right = i, i,
#         while left >=  0 and right < len(s) and s[left] == s[right]:
#             if (right -left) + 1 > maxLength:

#                 left-= 1
#                 right+=1
#                 result += s[left:right+1]

               
            
#         # for even length of string 
#         left, right = i, i+1
#         while left >= 0 and right < len(s) and s[left] == s[right]:
#             if (right -left) +1 > maxLength:

#                 left-= 1
#                 right+=1
#                 result += s[left:right+1]

                

# s = 'abbd'
# print(palimdromic(s))

def palindromic(s):
    res = ''
    for i in range(len(s)):
        l,r  = i,i

        while l >= 0 and r < len(s) and s[l] == s[r]:
            l-=1
            r += 1
            odd_sub = s[l+1:r]
            
        l,r = i,i+1

        while l >= 0 and r < len(s) and s[l] == s[r]:
            l-=1
            r+=1

            even_sub = s[l+1:r]
    if len(odd_sub) > len(res):

        res = odd_sub
    if len(even_sub) > len(res):
        res = even_sub
    
    return res
# print(palindromic('abbc'))
print ('longest substring')

def longestSubstring(s):
    longest = 0
    map ={}
    for i in range (len(s)):
        count = 0
        for j in range(i,len(s)):
            if s[j] in map:
                break;
            else:

                map[s[j]] = j +1
                count += 1
        map[i] = count
        longest = max(longest, count)

    return longest

            
          
                
                
         
result = longestSubstring('pwwkew')
print(result)
