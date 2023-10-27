def getprice(discount,price):
    return price*(1-discount)
netprice=getprice(0.1,100)
print(netprice)

def netprice(price,tax=0.08,discount=0.06):
    return price*(1+tax-discount)
on_net_price=netprice(200)
print(on_net_price)

def count_down(start):
    print(start)
    count_down(start-1)
    count_down(50)