class product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def display(self):
        print("product name : ",self.name)
        print("product price : ",self.price)
        print ("qunantity : ",self.quantity)
    def total_price(self):
        return self.price * self.quantity
p1=product("mouse",200,3)
p1.display()
print("Total price :",p1.total_price())

