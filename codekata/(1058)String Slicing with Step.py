text = input()
start,end,step = list(map(int,input().split()))
if step == 0:
    print("Zero")
else:
    if step > 0 and end > 0 :
        result = text[start:end+1:step]
    else:
        result = text[start:end:step]
    print(result)