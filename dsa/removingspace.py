def removingSpace(s):
    # removespace = s.replace(' ', '')
    removespace = ''.join(s.split(' '))
    return removespace

  
  


print(removingSpace("hello world"))