def rotate (arr,index,l=0):
    while(index<len(arr)):
        temp = arr[index]
        arr[index] = arr[l]
        arr[l] = temp
        index+=1
        l+=1
    return arr


a = [1,2,3,4,5,6]
print(rotate(a,1))

