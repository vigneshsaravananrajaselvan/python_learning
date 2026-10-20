amount = int(input())
denomination = [1000,500,100,50,10,1]
total_notes = 0
for bill in denomination:
    count = amount // bill
    total_notes += count
    amount = amount % bill
print (total_notes)