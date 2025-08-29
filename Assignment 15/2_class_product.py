# Create a class Product with members as pid,pname,price and quantity .Add following methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. ShowBook

class Product:
    def __init__(self,pid,pname,price = None, quanitity = 0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quanitity
        
    def __del__(self):
        print(f"resources release for {self.price}")
        
    def showBook(self):
        print("product id is : ",self.pid)
        print("product name : ", self.pname)
        print("product price: ", self.price)
        print("quantity of the product: ", self.quantity)
        
    
p1 = Product("furniture@123","furniture",14000,5)

p1.showBook()
