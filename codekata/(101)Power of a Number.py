n,k=map(int,input().split())
if n == 1:
    print("yes")  
      
if k <= 0 or n <= 0:
    print("no")
 
if k == 1:
    print("no")
        
while n % k == 0:
    n //= k
if n ==1:
    print("yes")
else:
    print("no")
        
 
