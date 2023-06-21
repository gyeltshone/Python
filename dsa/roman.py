def Contained(s):
    result =0 
    prev_val = 0
    container = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    for i in reversed(s):
        val = container[i]
        if val >= prev_val:
            result+=val
        else:
            result -=val
        prev_val = val
    return result
      
   

print(Contained("IX"))