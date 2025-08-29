# Create a class Shirt with members as sid,sname,type(formal etc), price and size(small,large etc) .
# Add following methods:
# j. Constructor (Support both parameterized and parameterless)
# k. Destructor
# l. ShowBook
# m. For each size of shirt price should change by 10%.
# (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
# xlarge=1300) Use static concept.
 
class Shirt:
    size_price_increase = {"small": 0, "medium": 10, "large": 20, "xlarge": 30}
    
    def __init__(self,sid = 0,sname = " ",shirt_type = " ",price = 0,size = 0):
        self.sid = sid
        self.sname = sname
        self.shirt_type = shirt_type
        self.price = price
        self.size = size
        
    def __del__(self):
        print(f"Release resources {self.size}")
        
    def showShirt(self):
        final_price = self.apply_size_price()
        print(f"id of the shirt {self.sid}")
        print(f"shirt name {self.sname}")
        print(f"type of shirt formal or other {self.shirt_type}")
        print(f"price of the shirt {self.price}")
        print(f"size of the shirt small or large or other {self.size}")
        print(f"Final Price : {final_price}")
        
    def apply_size_price(self):
        increase = Shirt.size_price_increase.get(self.size, 0)
        return self.price + (self.price * increase / 100)
    
S1 = Shirt(101, "Casual Check", "Casual", 1000, "medium")
S2 = Shirt(102, "Office Wear", "Formal", 1500, "xlarge")

S1.showShirt()
print()
S2.showShirt()
        
        
                 
        