def factorial(num):
  ret = 1
  for i in range(1, num+1):
    ret *= i
  return ret

size = int(input())

for _ in range(size):
  n, m = map(int, input().split())
  answer = factorial(m) // (factorial(n) * factorial(m - n))
  print(answer)