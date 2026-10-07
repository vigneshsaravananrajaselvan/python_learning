numbers=[15,54,98,62,64,78,54,21,35,15]
largest=numbers[0]
second=numbers[0]
third=numbers[0]
for i in numbers:
    if i >= largest:
        third=second
        second=largest
        largest = i
    elif i > second and  i!= largest:
        third = second
        second = i
    elif i > third and i!=second and i != first :
        third = i
print(f"Largest : {largest}")
print(f"Second largest : {second}")
print (f"Third largest : {third}")
        

