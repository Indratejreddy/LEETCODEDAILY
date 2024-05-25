def reverseANumber(n):
  if n %10 == n:
    return n
  return str(n%10)+str(reverseANumber(n//10))
print(reverseANumber(3425))