def search():
    number=[-2,5,0,-7,8,0,4]
    positive=0
    negative=0
    zero=0
    for i in number:
        if i>0:
            positive +=1
        elif i<0:
            negative +=1
        elif i==0:
            zero +=1
    print(f"postive count :{positive}")
    print(f"negative count : {negative}")
    print(f" zero count : {zero}")

search()

    
