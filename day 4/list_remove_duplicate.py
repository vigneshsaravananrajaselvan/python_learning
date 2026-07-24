number=[1,2,4,5,1,2,4,8,1,5,7,]
unique=[]
for i in number:
    if i not in unique:
        unique.append(i)
print(unique)

