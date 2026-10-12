print("****calculator***")
a=int(input("Enter the value 1 :"))
b=int(input("Enter the value 2 :"))
print("----MENU----")
print(""" 
1.Addition
2.Difference
3.Multiplication
4.Division
      """)
choice=int(input("Enter the choice 1-4:")) 
def add(a,b):
  return a+b
def sub(a,b):
 return a-b
def product(a,b):
  return a*b
def div(a,b):
  return a/b
if choice==1 :
  print("Addition ")
  print("Result =",add(a,b))
elif choice==2:
  print("Difference")
  print("Result =",sub(a,b))
elif choice==3:
  print("Multipication")
  print("Result =",product(a,b))
elif choice==4:
  print("Division")
  print("Result=",div(a,b))
else:
  print("Invalid input")







