l,r=map(int,input().split())
a=l
b=r
while b>0:
    a,b = b,a%b
lcm=(l*r)//a
print(lcm)