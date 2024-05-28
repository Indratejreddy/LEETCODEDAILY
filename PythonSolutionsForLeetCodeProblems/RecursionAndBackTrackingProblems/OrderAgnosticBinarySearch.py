def binarySearchAscending(arr, l, r, ele):
    mid = (l) + (r-l) // 2
    if l == r and arr[mid] !=ele:
        return -1
    if ele == arr[mid]:
        return mid
    elif ele > arr[mid]:
        return binarySearchAscending(arr, mid + 1, r, ele)
    else:
        return binarySearchAscending(arr, l, mid, ele)


def binarySearchDescending(arr, l, r, ele):
    mid = (l) + (r-l) // 2
    if l == r and arr[mid] !=ele:
        return -1
    if ele == arr[mid]:
        return mid
    elif ele > arr[mid]:
        return binarySearchDescending(arr, l, mid, ele)
    else:
        return binarySearchDescending(arr, mid+1, r, ele)


def orderAgnosticBinarySearch(arr, l, r, ele):
    if arr[l]<arr[r]:
        return binarySearchAscending(arr, l, r, ele)
    return binarySearchDescending(arr, l, r, ele)
    


print(orderAgnosticBinarySearch([6,5,4,3,2,1],0,5,0))
print(orderAgnosticBinarySearch([6,5,4,3,2,1],0,5,1))

print(orderAgnosticBinarySearch([1,2,3,4,5,6],0,5,3))
print(orderAgnosticBinarySearch([1,2,3,4,5,6],0,5,0))






