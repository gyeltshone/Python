def usingrecursive(base,exp):
    if exp == 0 :
        return 1
    else:
        return (base * usingrecursive(base,exp-1))
print(usingrecursive(2,3))