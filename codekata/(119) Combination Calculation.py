n,k = map(int , input().split())
def find_fact(num):
    fact = 1
    for i in range (1,num+1):
        fact = fact * i
    return fact 
n_fact = find_fact(n)
k_fact = find_fact(k)
n_minus_k_fact = find_fact(n-k)
ans = n_fact // (k_fact * n_minus_k_fact)
print(ans)
    