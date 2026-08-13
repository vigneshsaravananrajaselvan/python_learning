a,b=map(int,input().split())
s=min(a,b)
hcf=1
for i in range (1,s+1):
    if (a%i==0) and (b%i==0):
        hcf=i
print(hcf)