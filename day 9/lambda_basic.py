add=lambda a,b : a+b
print("add :",add(10,25))
difference=lambda a,b:a-b
print("difference :",difference(45,21))
sqauare= lambda a:a*a
print("square :",sqauare(10))
cube=lambda b: b**3
print("cube :",cube(2))
largest=lambda a,b:a if a>b else b
print("largest:",largest(20,12))
odd_even=lambda a: "even" if a%2==0 else "odd"
print(odd_even(15))