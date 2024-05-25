import math
def getMultiplesOfTen(num):
    return 10**int(math.log10(num))

def reversing(n):
    return  n if n%10 ==n else n%10*(getMultiplesOfTen(n)) + reversing(n//10)   

def reverse(n):
    if n<0:
        return n ==-reversing(-n)
    return n ==reversing(n)

print(reverse(1001))