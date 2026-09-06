s=input()
result=[]
for char in s:
    if char.isupper():
        result.append(char.lower())
    elif char.lower():
        result.append(char.upper())
    else:
        result.append(char)
print("".join(result))