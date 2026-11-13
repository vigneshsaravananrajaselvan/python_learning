ratings = [5,4,5,3,2,5,4,1,5,3,2,4,5]


def amazon_rating_analyzer(ratings):

    total = sum(ratings)

    average = total / len(ratings)


    highest = max(ratings)

   
    lowest = min(ratings)

    frequency = {}

    for r in ratings:

        if r in frequency:

            frequency[r] += 1

        else:

            frequency[r] = 1

   
    count_5 = 0

    for r in ratings:

        if r == 5:

            count_5 += 1

    percentage_5 = (count_5 / len(ratings)) * 100

    below_3 = []

    for r in ratings:

        if r < 3:

            below_3.append(r)

    
    print("Ratings :", ratings)

    print()

    print("Total Ratings :", len(ratings))

    print("Average Rating :", round(average,2))

    print("Highest Rating :", highest)

    print("Lowest Rating :", lowest)

    print()

    print("Frequency Counter :")

    for key, value in frequency.items():

        print(key, "Star :", value)

    print()

    print("5-Star Ratings :", count_5)

    print("Percentage of 5-Star Ratings :",
          round(percentage_5,2), "%")

    print()

    print("Ratings Below 3 :", below_3)

    print("Count :", len(below_3))


amazon_rating_analyzer(ratings)