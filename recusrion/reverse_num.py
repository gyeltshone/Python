def reverse_num(x):
    reverse= 0
    if x==0:
        return

    return reverse*10,reverse_num(x//10)
print(reverse_num(123))