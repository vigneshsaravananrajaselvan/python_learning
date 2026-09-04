s = input().split()
final = []
for i in s:
    if len(i) <= 3:
        final.append(i)
    else:
        first = i[0]       
        last = i[-1]
        midle = i[1:-1]
        new_word = first + midle[::-1] + last
        final.append(new_word)
