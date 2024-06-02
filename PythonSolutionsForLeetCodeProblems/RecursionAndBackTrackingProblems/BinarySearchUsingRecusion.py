# def binarySearch(arr, l, r, ele):
#     mid = (l) + (r-l) // 2
#     if l == r and arr[mid] !=ele:
#         return -1
#     if ele == arr[mid]:
#         return mid
#     elif ele > arr[mid]:
#         return binarySearch(arr, mid + 1, r, ele)
#     else:
#         return binarySearch(arr, l, mid, ele)
        
# b = [6, 7, 8, 9, 10]

# print(binarySearch(b, 0, len(b)-1, 9))



# problem link: https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def rotatedBinarySearch(self,arr,start,end,searchElement):
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
        return self.rotatedBinarySearch(arr,start,end,searchElement)

    
    def search(self, nums: List[int], target: int) -> int:
        return self.rotatedBinarySearch(nums,0,len(nums)-1,target)


