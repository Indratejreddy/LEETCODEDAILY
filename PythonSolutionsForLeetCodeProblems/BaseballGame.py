# leet code problem link : https://leetcode.com/problems/baseball-game/description/

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        print(operations)
        newArr = []
        count = -1
        for i in range(len(operations)):
            if (operations[i].isdigit) and (operations[i]!="+" and operations[i]!="C" and operations[i]!="D"):
                newArr.append(int(operations[i]))
                count+=1
            elif operations[i] =='+':
                newArr.append(int(newArr[count])+int(newArr[count-1]))
                count+=1
            elif operations[i] =='D':
                newArr.append(int(newArr[count])*2)
                count+=1
            elif operations[i] =='C':
                newArr.pop()
                count-=1      
        return sum(newArr)


    