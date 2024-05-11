#leet code problem link : https://leetcode.com/problems/concatenation-of-array/

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        j = len(nums)
        p  = [0]*2*j
        i=1
        while(i<=j-2):
            p[j+i]+=nums[i]
            i+=1
        print(p)