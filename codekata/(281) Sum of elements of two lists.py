n = int(input())
a = list(map(int,input().split()))
b =  list(map(int,input().split()))
c = []
for i in range(n):
    total = a[i] + b[i]
    c.append(total)
print(*c)
 