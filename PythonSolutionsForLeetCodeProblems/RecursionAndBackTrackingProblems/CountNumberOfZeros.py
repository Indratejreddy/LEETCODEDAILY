#method1
def countZeros(n,count=0):
    if n%10 == n:
        if n == 0:
            return 1
        return 0    
    count += countZeros(n%10) + countZeros(n//10) 
    return count

#method2 directly updating the count
def countZeros(n,count=0):
    if n%10 == n:
        if n == 0:
            count+=1
        return count  
    count += countZeros(n%10) + countZeros(n//10) 
    return count


print(countZeros(10000000000002))

# 10203
# 3,1020
# 0,102
# 2,10
# 0,1 
# 1


