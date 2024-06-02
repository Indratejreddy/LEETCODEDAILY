def rotatedBinarySearch(arr,start,end,searchElement):
    mid = start+(end-start)//2
    if start == end and arr[mid] !=searchElement:
        return -1
    if searchElement == arr[mid]:
        return mid
    if(arr[start]<=arr[mid]): #check whether left half is sorted or not
        if(searchElement>=arr[start] and searchElement<=arr[mid]):
            end = mid-1
        else:
            start = mid+1
    else:
        if(searchElement>=arr[mid] and searchElement<=arr[end]):
            start = mid+1
        else:
            end = mid-1
    return rotatedBinarySearch(arr,start,end,searchElement)


p = [5,6,7,1,2,3,4]

print(rotatedBinarySearch(p,0,len(p)-1,3))
