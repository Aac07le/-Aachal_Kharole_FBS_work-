# Create a class Product with members as pid,pname,price and quantity .
# Add following methods:
# e. Constructor (Support both parameterized and parameterless)
# f. Destructor
# g. ShowBook
# h. Add static member discount.
# i. Provide methods for applying discount on price of product.

class Product:
    discount = 10
    def __init__(self,pid = 0,pname = " ", price = 0, quantity = 0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
        
    def __del__(self):
        print(f"relese resources of {self.quantity}")
        
    def showProduct(self):
        print(f"product id is {self.pid}")
        print(f"product name {self.pname}")
        print(f"price of the product {self.price}")
        print(f"quantity of the product {self.quantity}")
        
    def applydiscount(self):
        discounted_price = self.price - (self.price * Product.discount / 100)
        return discounted_price
    @staticmethod
    def show_discount():
        print(f"current discount: {Product.discount}")
        
        
P1 = Product(101, "Laptop", 50000, 2)
P2 = Product(102, "Mobile", 20000, 5)        

P1.showProduct()
print(f"Discounted Price: {P1.applydiscount()}%\n")

P2.showProduct()
print(f"Discounted Price: {P2.applydiscount()}%\n")

Product.show_discount()        
        
        
        