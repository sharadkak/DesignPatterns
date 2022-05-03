from abc import ABC, abstractmethod

# abstract class for TopWear
class TopWear(ABC):
    
    @abstractmethod
    def price(self):
        pass
    
    @abstractmethod
    def durability(self):
        pass

# abstract class for BottomWear
class BottomWear(ABC):
    @abstractmethod
    def price(self):
        pass
    
    @abstractmethod
    def durability(self):
        pass

# abstract class for factory
class AbstractFactory(ABC):
    @abstractmethod
    def create_bottoms(self) -> BottomWear:
        pass
    
    @abstractmethod
    def create_tops(self) -> TopWear:
        pass