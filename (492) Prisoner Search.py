rows,cols = map(int,input().split())
all_prisoners = map(int,input().split())
target_id = int(input())
if target_id in all_prisoners:
    print("yes")
else :
    print("no")

