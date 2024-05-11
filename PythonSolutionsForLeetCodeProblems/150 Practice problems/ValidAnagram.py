# problem link: https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S = {}
        T = {}
        sLen = len(s)
        i = 0
        if(sLen != len(t)):
            return False
        else:
            while(i < sLen):
                S[s[i]] = 1 if s[i] not in S else S[s[i]] + 1
                T[t[i]] = 1 if t[i] not in T else T[t[i]] + 1
                i += 1
            if S == T:
                return True    
        return False