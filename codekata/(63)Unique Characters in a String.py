s=input()
freq={}
for char in s:
    if char in freq:
        freq[char]=freq[char]+1
    else:
        freq[char]=1
unique_count=0
for char in s:
    if freq[char]==1:
        unique_count=unique_count+1

if unique_count>0:
    print(unique_count)
else:
    print("-1")