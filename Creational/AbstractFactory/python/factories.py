from interfaces import AbstractFactory
from concrete_classes import *

class WinterClothes(AbstractFactory):
    
    def create_bottoms(self) -> BottomWear:
        return Jeans()
        
    def create_tops(self) -> TopWear:
        return Jacket()

class SummerClothes(AbstractFactory):
    
    def create_bottoms(self) -> BottomWear:
        return Shorts()
    
    def create_tops(self) -> TopWear:
        return CottonShirt()
    
