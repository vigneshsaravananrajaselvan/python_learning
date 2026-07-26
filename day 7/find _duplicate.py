def duplicate():
    number=[4,2,5,7,2,8,5]
    find=[]
    for i in number:
        if i==number:
            find.append(i)
    print(f"duplicate :{i}")
duplicate()