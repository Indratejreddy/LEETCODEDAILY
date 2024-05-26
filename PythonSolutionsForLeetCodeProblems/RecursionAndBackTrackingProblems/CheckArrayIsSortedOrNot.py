def checkArrayIsSorted(arr,index=0):
    if len(arr)-1 == index:
        return True
    return arr[index]<arr[index+1] and checkArrayIsSorted(arr,index=index+1)  


print(checkArrayIsSorted([1,2,3,40,5]))