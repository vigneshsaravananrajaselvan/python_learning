ratings=[5,4,5,3,4,5,2,1]
frequency={}
for i in ratings:
    frequency[i] = frequency.get(i,0)+1
print(frequency)
