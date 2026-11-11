scores=[65,80,92,78,85,95,70,60,85,90]
def emp_performence_scores(scores):
    average = sum(scores)/len(scores)
    best_emp = max(scores)
    worst_emp = min (scores)
    emp_above_average =[]
    emp_below_avarage =[]
    for s in scores:
        if s > average:
            emp_above_average.append(s)
        if s < average:
            emp_below_avarage.append(s)
        top_performers =[]
        for s in scores:
            if s >=90:
                top_performers.append(s)
    print("Scores :",scores)
    print()
    print("Average score :",average)
    print("Best employeee score :",best_emp)
    print("Worst employee score :",worst_emp)
    print("Employees above average:",emp_above_average)
    print("Employees below average score",emp_below_avarage)
    print()
    print("Employees above 90+ :",top_performers)
    print("Count =",len(top_performers))
emp_performence_scores(scores)
