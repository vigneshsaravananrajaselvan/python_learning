s1,s2=input().strip().split()
s2_set=set(s2)
result=[char for char in s1 if char not in s2_set]
final=("".join(result)) 
print( final if final !=""else ("-1"))