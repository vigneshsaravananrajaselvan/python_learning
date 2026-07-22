ratings=[4,5,3,5,4,2,5,1,4,3]
average=sum(ratings)/len(ratings)
highest=max(ratings)
lowest=min(ratings)
five_star=ratings.count(5)

positive=0
for rating in ratings:
    if rating >= 4:
        positive +=1

possitive_percentage=(positive/len(ratings))*100
print(f"Average Rating :{average}")
print(f"Highest Rating : {highest}")
print(f"Lowest Rating : {lowest}")
print(f"Number of 5 STAR Ratings : {five_star}")
print(f"Positive rating Percentage : {possitive_percentage}%")

