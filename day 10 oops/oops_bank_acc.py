class bank :
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw (self,amount):
        self.balance -=amount
    def show_balance(self):
        print("Balance : ",self.balance)
n1=bank("salim",10000)
n1.deposit(1500)
n1.withdraw(5000)
n1.show_balance()