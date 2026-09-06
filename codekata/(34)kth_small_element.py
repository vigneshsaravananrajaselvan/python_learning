n, k = map(int, input().split())
element = list(map(int, input().split()))
unique = sorted(set(element))
if k <= len(unique) and k > 0:
    target_element = unique[k - 1]  
    final = []
    for i in element:
        if i == target_element:
            final.append(i)
            break  
    print(final[0])
else:
    print(-1)