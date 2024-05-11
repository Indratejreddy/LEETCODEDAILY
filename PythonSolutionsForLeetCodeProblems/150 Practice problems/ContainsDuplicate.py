# problem link: https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    #solution using set in built datastructure
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     if len(set(nums)) != len(nums):
    #         return True
    #     return False 
    #solution using set in built counter
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     numsDic = Counter(nums)
    #     for i in numsDic.values():
    #         if i>1:
    #             return True
    #     return False

    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     myDic = {}
    #     for i in nums:
    #         if i not in myDic:
    #             myDic[i] = i
    #         else:
    #             return True
    #     return False

    def containsDuplicate(self, nums: List[int]) -> bool:
        myDic = {}
        for i in nums:
            if i not in myDic:
                myDic[i] = i
            else:
                return True
        return False