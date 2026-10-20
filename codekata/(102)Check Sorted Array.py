n = int(input())
arr = list( map(int,input().split()))
is_ascending = True
is_descending = True
for i in range (len(arr)-1):
    if arr[i] > arr[i+1]:
        is_ascending = False
    if arr[i] < arr[i+1]:
        is_descending = False
if is_ascending or is_descending:
    print("yes")
else:
    print("no")