s=input()
max_count=0
for char in s:
    count=s.count(char)
    if count > max_count:
        max_count=count
if max_count<=1:
    print("0")
else:
    print(max_count)