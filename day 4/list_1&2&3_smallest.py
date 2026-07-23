numbers=[12,54,98,62,34,75,94,63,25,71]
first=second=third=float('inf')
for i in numbers:
    if first>i:
        third=second
        second=first
        first=i
    elif i<second and i!=first:
        third=second
        second=i
    elif i<third and i!= second:
        third=i
print(f"smallest : {first}")
print(f"second smallest : {second}")
print(f"third smaleest : {third}")