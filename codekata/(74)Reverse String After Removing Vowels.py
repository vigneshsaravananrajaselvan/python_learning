s=input().lower()
vowels="aeiou"
final=""
for i in s:
    if i not in vowels:
        final += i
if final=="":
    print("-1")
else:
    print(final[::-1])