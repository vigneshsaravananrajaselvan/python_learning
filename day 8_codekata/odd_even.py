num_str=input().strip()
even_digit=[]
odd_digit=[]
for digit in num_str:
    d=int(digit)
    if d%2==0:
        even_digit.append(digit)
    else:
        odd_digit.append(digit)
even_digit.sort()
odd_digit.sort()
print(" ".join(even_digit))
print(" ".join(odd_digit))