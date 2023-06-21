def printing_arry_recursive(arr):
    if len(arr) == 0:
    
        return 

    return (arr[0],printing_arry_recursive(arr[1:]))

print(printing_arry_recursive([1,2,3,4,5]))