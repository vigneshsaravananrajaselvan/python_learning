n=input().strip().lower()
vowel=set('aeiou')
if vowel.intersection(n):
    print("yes")
else:
    print("no")