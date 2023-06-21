def product_array(array):
    product = 1
    for i in range(len(array)):
        product*=array[i]
    return product



print(product_array([1,2,3]))

def productOfArray(arr):
    if len(arr) == 0:
        return 1
    return arr[0] * productOfArray(arr[1:])





