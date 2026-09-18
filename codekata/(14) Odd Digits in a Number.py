num=input().strip()
odd_number=[]
for digit in num:
    if int(digit)%2!=0:
        odd_number.append(digit)
if len(odd_number)>0:
    print(" ".join(odd_number))
else:
    print("-1")