#with function body variable
def linearSearchUsingRecursionReturnAllndexes(arr,val,index=0):
    newArr = []
    if len(arr) == index:
        return newArr
    if arr[index]==val:
        newArr.append(index)
    return newArr+linearSearchUsingRecursionReturnAllndexes(arr,val,index=index+1)  


print(linearSearchUsingRecursionReturnAllndexes([1,2,3,4,5,1],1))


#without function body variable using parameters
def linearSearchUsingRecursionReturnAllndexes(arr,val,index=0,newArr=[]):
    if len(arr) == index:
        return newArr
    if arr[index]==val:
        newArr.append(index)
    return linearSearchUsingRecursionReturnAllndexes(arr,val,index=index+1,newArr=newArr)  


print(linearSearchUsingRecursionReturnAllndexes([1,2,3,4,5,1],1))
