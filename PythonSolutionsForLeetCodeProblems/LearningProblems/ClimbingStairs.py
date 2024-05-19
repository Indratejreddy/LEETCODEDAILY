# leet code problem link : https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        zero = count = 0
        one = 1
        while(n>=1):
            count = zero+one
            zero = one
            one = count
            n-=1
        return count
