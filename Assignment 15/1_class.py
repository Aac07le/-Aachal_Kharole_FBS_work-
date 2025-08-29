# Create a class Book with members as bid,bname,price and author.Add following methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook

class Book:
    def __init__(self,bid = 234 ,bname= None,price= 0,author= None):
        
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        
        
    def __del__(self):
        print(f"resources release for {self.bname}")
        
    def showBook(self):
        print("bookid: ", self.bid)
        print("bname: ", self.bname)
        print("price: ", self.price)  
        print("author: ", self.author)      

b1 = Book(101,"gently falls the bakula",200,"SudhaMurti")
b2 = Book(102,"Rich Dad Poor Dad",400)

# bname=input("enter book name")
b1.showBook()
b2.showBook()
# b1.display()
