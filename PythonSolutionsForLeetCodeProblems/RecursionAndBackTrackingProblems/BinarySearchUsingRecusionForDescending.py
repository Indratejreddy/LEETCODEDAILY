def binarySearchForDescending(arr, l, r, ele):
    mid = (l) + (r-l) // 2
    if l == r and arr[mid] !=ele:
        return -1
    if ele == arr[mid]:
        return mid
    elif ele > arr[mid]:
        return binarySearchForDescending(arr, l, mid, ele)
    else:
        return binarySearchForDescending(arr, mid+1, r, ele)
        

b = [10, 9, 8, 7, 6]
print(binarySearchForDescending(b, 0, len(b)-1, 8) )






