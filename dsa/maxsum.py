class MaxSumList:

    def __init__(self) -> None:
        pass

    def arr(self,lst):
        # max_num = 0

        # for i in range(len(lst)):
        #     if lst[i] > max_num:
        #         max_num = lst[i]
        # output = 0
        sums = 0
        for j in range(len(lst)):
            sums += lst[j]
        print(sums)
                        

lst = MaxSumList()
lst.arr([1,45,2,1,35])
            
    
