import math
def getMultiplesOfTen(self,num):
    return 10**int(math.log10(num))

def reversing(self,n):
    return  n if n%10 ==n else n%10*(self.getMultiplesOfTen(n)) + self.reversing(n//10)   

def reverse(self, n: int) -> int:
    if n<0:
        return -self.reversing(-n)
    return self.reversing(n)

