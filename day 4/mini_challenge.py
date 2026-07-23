ratings=[5,4,5,3,5,2,4,5]
#count
count={}
for rating in ratings:
    if rating in count:
        count[rating]=1
    else:
        count[rating]=1
print(f"cound of each ratings :{count}")
#unique
unique=set(ratings)
print(f"unique rating:{unique}")
#average
average=sum(ratings)/len(ratings)
print(f"average of ratings : {average}")
#highest
highest=max(ratings)
print(f"hoghest of ratings : {highest}")
#lowest
lowest=min(ratings)
print(f"lowest of ratings : {lowest}")

