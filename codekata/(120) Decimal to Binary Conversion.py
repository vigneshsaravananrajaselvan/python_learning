n = int(input())
if n == 0:
    print("0")
else:
    remainder = []
    while n > 0:
        remainder.append(str(n % 2))
        n = n // 2 
    remainder.reverse()
    print("".join(remainder))
