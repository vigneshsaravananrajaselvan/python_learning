n=int(input())
element=list(map(int,input().split()))
unique=list(set(element))
unique.sort()
if len(unique)>=2:
    print(unique[1])
else:
    print("-1")