order_value=int(input("enter the final order value :"))
if order_value >= 5000:
    print("congratilations you recived 10% discount for your order")
    after_dicount=order_value - 5000
    print("the final amount  after the discount :",after_dicount)
else :
    print("the final amount :",order_value)