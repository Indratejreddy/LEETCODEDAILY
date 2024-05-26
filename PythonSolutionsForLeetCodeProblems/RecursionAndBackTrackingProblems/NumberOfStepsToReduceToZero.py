class Solution:
    def checker(self,num,count):
        if num == 0:
            return num, count
        if num%2 == 0:
            num//=2
            count+=1
        else:
            num-=1
            count+=1
        return self.checker(num,count)

    def numberOfSteps(self, num: int, count = 0) -> int:
        return self.checker(num,count)[1]
    



class Solution:
    def checker(self,num,count):
        if num == 0:
            return num, count
        if num%2 == 0:
            num//=2
            count+=1
        else:
            num-=1
            count+=1
        return self.checker(num,count)

    def numberOfSteps(self, num: int, count = 0) -> int:
        return self.checker(num,count)[1]

#method2  
class Solution:
    def checker(self,num,count):
        if num == 0:
            return count
        if num%2 == 0:
            return self.checker(num//2,count=count+1)
        return self.checker(num-1,count=count+1)
    def numberOfSteps(self, num: int, count = 0) -> int:
        return self.checker(num,count)
    
k = Solution()
print(k.numberOfSteps(123,0))

