a,b=input().strip().split()
str1=set(a)
str2=set(b)
if str1.intersection(str2):
    print("yes")
else:
    print("no")