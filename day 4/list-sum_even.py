numbers=[2,5,47,58,5,96,4,1,2,3,5,4,58,214]
even_sum=0
odd_sum=0
even=[]
odd=[]
for i in numbers:
    if i % 2 ==0:
        even_sum += i 
        even.append(i)
    else:
        odd.append(i)
        odd_sum +=i

print(even)
print(f"sum of even numbers : {even_sum}")
print(odd)
print(f"sum of odd numbers : {odd_sum}")
