n = input().strip()
decimal_num = 0
power = 0
for digit in reversed(n):
    if digit == '1':
        decimal_num += (1 << power)
    power += 1
print(decimal_num)