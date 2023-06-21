
# def expo(base,exp):
#     if exp == 0:
#         return 1
#     return(base* expo(base,exp-1))
# print(expo(2,3))


# iterative way

def iterative_way(base,exp):
    if exp == 0:
        return 1
    else:
        sol = 1
        while exp > 0:
            sol  *= base
            exp-=1
        return sol
          
print(iterative_way(2,3))