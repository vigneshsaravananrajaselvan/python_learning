n=int(input())
collect=[]
for digit in range (1,n+1):
    if n%digit==0:
        collect.append(digit)
if len(collect)>0:
    print(" ".join(map(str,collect)))
    