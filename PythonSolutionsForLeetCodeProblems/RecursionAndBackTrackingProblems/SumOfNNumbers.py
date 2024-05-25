def sumOfNNumbers(n):
    if n<=1:
        return 1
    return n+sumOfNNumbers(n-1)


print(sumOfNNumbers(5))