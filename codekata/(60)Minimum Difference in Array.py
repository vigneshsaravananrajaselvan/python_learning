n = int(input())
arr = list(map(int,input().split()))
if len(arr)<2:
    print(0)
else:
     arr.sort()
min_diff = float("inf")
for i in range (1,n):
    current_diff = arr[i] - arr[i-1]
    if current_diff < min_diff:
        min_diff = current_diff
print(min_diff)