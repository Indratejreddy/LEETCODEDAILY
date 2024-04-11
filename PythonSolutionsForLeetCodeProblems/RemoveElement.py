#leet code problem link : https://leetcode.com/problems/remove-element/
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         nums[:]=[i for i in nums if i!=val]
#         return len(nums)

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        NonVal = -1
        for right in range(len(nums) -1,-1,-1):
            if nums[right]!=val:
                nums[NonVal] = nums[right]
                NonVal-=1               
        nums[:] = nums[NonVal+1:]
        return len(nums)

