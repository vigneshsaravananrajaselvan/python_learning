numbers=[10,25,7,80,35,46]
largest=numbers[0]
smallest=numbers[0]
for num in numbers:
    if largest <= num:
        largest=num
print(f"largest : {largest}")
for i in numbers:
    if smallest >= i:
        smallest = i 
print(f'smallest : {smallest}')