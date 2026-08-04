class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("Employee name : ",self.name)
        print("Salary : ",self.salary)
e1=employee("raja",54000)
e2=employee("venkat",62000)
e3=employee("jeeva",52000)
e1.display()
e2.display()
e3.display()