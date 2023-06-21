def binary_search(lst,n):
    l = 0
    u = len(lst)-1

    while u>=l:
        mid = (l+u)//2

        if lst[mid] ==n:
            print('found',mid, "value", lst[mid])
            return True
        else:

            if lst[mid]>n:
                u = mid
            else:
                l = mid
        
binary_search([1,2,3,4,5,6,7,8],7 )
