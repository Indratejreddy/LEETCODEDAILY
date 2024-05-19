#leet code problem link : https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        unique_index = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[unique_index]:
                unique_index += 1
                nums[unique_index] = nums[i]

        del nums[unique_index + 1 :]
        return unique_index + 1
