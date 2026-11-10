
def greet(name):
  print("hello",name)
  print("welcome to data science")
name=input("enter the name:")
greet(name)

#funtion to add two numbers
def sum(a,b):
  return a+b
print("---SUM---")
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
print("the sum is",sum(a,b))

#funtion to find square
def square(a):
  return a*a
print("---SQUARE---")
a=int(input("enter the number :"))
print("the square is",square(a))

#fuction with even or add
def check_even(a):
  if a%2==0:
    return "even"
  else:
    return "odd"
print("--ODD_EVEN---")
a=int(input("enter the number:"))
print(check_even(a))

#largest of three number
def largest(a,b,c):
  if a>=b and a>=c:
    return a
  elif b>=c:
    return b
  else:
    return c
print("---LARGEST OF THREE NUMBER")
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
print("the largest number is",largest(a,b,c))

#second largest of three number
def second_largest(a,b,c):
  return sorted([a,b,c])[1]
print("---SECOND LARGEST NUMBER---")
a=int(input("enter the value value a:"))
b=int(input("enter the value value b:"))
c=int(input("enter the value value c:"))
print("the second largest number is",second_largest(a,b,c))

#total and average of three number using fucntion
def avg_mark(m1,m2,m3):
  total=m1+m2+m3
  average=total/3
  return(total,average)
print("---AVERAGE---")
m1=int(input("enter the mark1:"))
m2=int(input("enter the mark2:"))
m3=int(input("enter the mark3:"))
total,average=avg_mark(m1,m2,m3)
print("total:",total)
print("average :",average)











