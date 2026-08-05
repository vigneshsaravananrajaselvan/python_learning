class employee :
    def login (self):
        print("Employee logged in ")
class manager(employee):
    def data_management(self):
        print("Analyzing data")
class software_engineer(employee):
    def software_devloper(self):
        print("develpoing apps")
e1=manager()
e2=software_engineer()
e1.login()
e1.data_management()
e2.login()
e2.software_devloper()

 