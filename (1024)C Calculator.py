c = int(input())
n, m = map(int, input().split())
if c == 1:
    result = n + m
elif c == 2:
    result = n - m
elif c == 3:
    result = n * m
else:
    result = n / m
print(result)