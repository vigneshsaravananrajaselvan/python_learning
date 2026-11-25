R = int(input())
for i in range(1, R + 1):
  print(" " * (R - i), end="")
  for j in range(i, 2 * i):
    print(j, end="")
  for j in range(2 * i - 2, i - 1, -1):
    print(j, end="")
  print()