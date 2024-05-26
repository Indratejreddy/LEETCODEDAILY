# def linearSearchUsingRecursion(arr,val,index=0,):
#     if len(arr) == index:
#         return False
#     return arr[index]==val or linearSearchUsingRecursion(arr,val,index=index+1)  


# print(linearSearchUsingRecursion([1,2,3,4,5],6))


def linearSearchUsingRecursion(arr,val,index=0,):
    if len(arr) == index:
        return -1
    return index if arr[index]==val else linearSearchUsingRecursion(arr,val,index=index+1)  


print(linearSearchUsingRecursion([1,2,3,4,5],8))