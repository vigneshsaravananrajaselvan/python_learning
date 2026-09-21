n,k=map(int,input().split())
element=list(map(int,input().split()))
count=0
for i in element:
    if i==k:
        count +=1
        
if count>0:
    print(count)
else:
    print("-1")
    