from abc import ABC, abstractmethod

class Beverage(ABC):
    @abstractmethod
    def get_description(self)->str:
        pass

    
    @abstractmethod
    def get_cost(self)->int:
        pass

class Coffee(Beverage):
    def get_description(self):
        return "Plain coffee"


    def get_cost(self):
        return 20

class CoffeeWitMilk(Coffee):
    def get_description(self):
        return "Plain coffe with Milk"


    def get_cost(self):
        return 30

class AddOnDecotor(Beverage):
    def __init__(self, coffee:"Coffee"):
        self._coffee = coffee
    def get_description(self):
        pass


    def get_cost(self):
        pass

class MilkDecorator(AddOnDecotor):
    def get_description(self):
        return self._coffee.get_description()+",Milk"


    def get_cost(self):
        return self._coffee.get_cost()+20

class WhipCreamDecorator(AddOnDecotor):
    def get_description(self):
        return self._coffee.get_description()+", Whip Cream"


    def get_cost(self):
        return self._coffee.get_cost()+ 50

class SugarDecorator(AddOnDecotor):
    def get_description(self):
        return self._coffee.get_description()+", Sugar"


    def get_cost(self):
        return self._coffee.get_cost()+ 5


coffee = Coffee()

coffee = MilkDecorator(coffee)
coffee = WhipCreamDecorator(coffee)
print(coffee.get_description())
print(coffee.get_cost())