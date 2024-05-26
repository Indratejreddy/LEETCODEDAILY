
def linearSearchUsingRecursionReturnIndex(arr,val,index=0,):
    if len(arr) == index:
        return -1
    return index if arr[index]==val else linearSearchUsingRecursionReturnIndex(arr,val,index=index+1)  


print(linearSearchUsingRecursionReturnIndex([1,2,3,4,5],8))