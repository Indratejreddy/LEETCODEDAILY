def binarySearch(arr, l, r, ele):
    mid = (l) + (r-l) // 2
    if l == r and arr[mid] !=ele:
        return -1
    if ele == arr[mid]:
        return mid
    elif ele > arr[mid]:
        return binarySearch(arr, mid + 1, r, ele)
    elif ele < arr[mid]:
        return binarySearch(arr, l, mid, ele)
        
b = [6, 7, 8, 9, 10]

b = [10, 9, 8, 7, 6]
print(binarySearch(b, 0, len(b)-1, 10))


