s,k=input().strip().split()
length=len(s)
found_index=-1
for i in range (length):
    if s[i]==k:
        found_index=i+1
        break
if found_index != -1:
    print(found_index)
else:
    print("-1")