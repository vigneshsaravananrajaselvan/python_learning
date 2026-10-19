first_line = input().split()
n = int(first_line[0])
q = int(first_line[1])
string_count = {}
for _ in range (n):
    current_string = input().strip()
    if current_string in string_count:
        string_count[current_string] +=1
    else:
        string_count[current_string] = 1
for _ in range (q):
    query_string = input().strip()
    if query_string in string_count:
        print(string_count[query_string])
    else:
       print(0)
