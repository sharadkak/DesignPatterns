from interfaces import BottomWear, TopWear

##### Concrete classes for BottomWear #######
class Jeans(BottomWear):
    
    def __init__(self):
        
        self.brand_name = "Zara"
        
    def price(self):
        return "50€"
    
    def durability(self):
        return 3

class Shorts(BottomWear):
    def __init__(self):
        self.brand_name = "Levis"
        
    def price(self):
        return "5"
    
    def durability(self):
        return 0.5


##### Concrete classes for TopWear #######
class CottonShirt(TopWear):
    def __init__(self):
        self.brand_name = "Gucci"
        
    def price(self):
        return "15€"
    
    def durability(self):
        return 1

class Jacket(TopWear):
    def __init__(self):
        self.brand_name = "North face"
        
    def price(self):
        return "100€"
    
    def durability(self):
        return 6