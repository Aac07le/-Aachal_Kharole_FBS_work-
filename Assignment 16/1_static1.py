# Create a class Book with members as bid,bname,price and author.Add following methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook
# d. Add static variable count and also maintain count of objects created.

class Book:
    count = 0
    def __init__(self,bid = "abc",name = " ", price=0 , author = " "):
        self.bid = bid
        self.name = name
        self.price = price
        self.author = author
        
        Book.count += 1
        
    def __del__(self):
        print(f"Relaese resources {self.price}")
        
        
        Book.count -= 1
    def showbook(self):
        print(f"id of the book {self.bid}")
        print(f"name of book {self.name}")
        print(f"price of the book {self.price}")
        print(f"who is the author of this book {self.author}\n")
        
       
        
    @staticmethod
    def show_count():
        print(f"TOTAL BOOKS CREATED: {Book.count}")
        
    
B1 = Book(123,"The God of Small Things",250,"Arundhati Roy")
B2 = Book(404,"The Gold Of Small Thing",350,"Arunditi roy")
B1.showbook()
B2.showbook()

B1.show_count()
B2.show_count()