text=input("enter text :").lower()
count=0
for i in text:
    if i in "aeiou":
        count +=1
print("count :",count)

11