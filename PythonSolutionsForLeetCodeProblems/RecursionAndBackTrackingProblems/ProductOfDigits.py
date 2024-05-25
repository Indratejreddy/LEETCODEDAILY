def sumOfDigits(n):
  if n%10 == n:
    return n
  return n%10*sumOfDigits(n//10)
print(sumOfDigits(3425))