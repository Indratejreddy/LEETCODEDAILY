# leet code problem link : https://leetcode.com/problems/valid-parentheses/description/
class Solution: 
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        else:
            closeToOpen = {')':'(','}':'{',']':'['}
            openArray = []
            for i in s:
                if openArray and i in closeToOpen:
                    if closeToOpen[i] == openArray[-1]:
                        openArray.pop()
                    else:
                        return False
                else:
                    openArray.append(i)
            return False if openArray else True
