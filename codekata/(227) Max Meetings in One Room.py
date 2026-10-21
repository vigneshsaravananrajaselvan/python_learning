n = int(input())
s = list(map(int,input().split()))
f = list(map(int,input().split()))
meeting = []
for i in range (n):
    meeting.append([f[i],s[i]])
meeting.sort()
count = 0
last_finish_time = -1
for i in range (n):
    finish = meeting[i][0]
    start = meeting[i][1]
    if start >= last_finish_time:
        count  += 1
        last_finish_time = finish
print(count)
