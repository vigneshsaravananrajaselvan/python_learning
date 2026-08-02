students=[
    ("rahul",86),
    ("ankit",81),
    ("rajesh",96),
    ("balu",68)
    ]
print(sorted(students,key=lambda x:x[1],reverse=True))
print(sorted(students,key=lambda x :(x[0],x[1])))