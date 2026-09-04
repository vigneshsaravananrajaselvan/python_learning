n,k=map(int,input().split())
arr=list(map(int,input().split()))
position=-1
for i in range(n):
    if arr[i]==k:
        position = i + 1
        break
print(position)