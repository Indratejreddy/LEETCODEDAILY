def binarySearch(arr, l, r, ele):
    mid = (l) + (r-l) // 2
    if l == r and arr[mid] !=ele:
        return -1
    if ele == arr[mid]:
        return mid
    elif ele > arr[mid]:
        return binarySearch(arr, mid + 1, r, ele)
    else:
        return binarySearch(arr, l, mid, ele)
        
b = [6, 7, 8, 9, 10]

print(binarySearch(b, 0, len(b)-1, 9))


