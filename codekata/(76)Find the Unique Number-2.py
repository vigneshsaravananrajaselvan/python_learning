n=int(input())
arr=list(map(int,input().split()))
count={}
for num in arr:
    if num in count:
        count[num] +=1
    else:
        count[num]=1 
for num in arr:
    if count[num]==1:
        print(num)
        break