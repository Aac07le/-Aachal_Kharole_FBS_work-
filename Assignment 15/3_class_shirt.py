# Create a class Shirt with members as sid,sname,type(formal etc), price and size(small,large etc) .Add following methods:
# g. Constructor (Support both parameterized and parameterless)
# h. Destructor
# i. ShowBook

class Shirt:
    def __init__(self,sid,sname,type,price,size):
        self.sid = sid
        self.sname= sname
        self.type = type
        self.price = price
        self.size = size
        
    def __del__(self):
        print(f"resources relese for \nName {self.sname} \nType {self.type} \nPrice {self.price} \nSize {self.size}")
        
    def showBook(self):
        print("id of shirt: ",self.sid)
        print("name of shirt: ",self.sname)
        print("types of shirt: ",self.type)
        print("price of shirt: ",self.price)
        print("size of shirt: ",self.size)
        
shirt1 = Shirt(123,"avi","formal",300,"large")

shirt1.showBook()
    