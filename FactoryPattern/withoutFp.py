from abc import ABC, abstractmethod

class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass


class Pizza:
    def prepare(self):
        print("Preparing pizza")


class Burger:
    def prepare(self):
        print("Preparaing burger")


# Responsible for making objects
class RestrauntService:
    def create_order(self, food_type:str):
        if food_type=="pizza":
            f = Pizza()
            f.prepare()
            return f

        elif food_type=="burger":
            f = Burger()

        else:
            print("Invalid food type")
            return None

        f.prepare()
        return f


restraunt_service = RestrauntService()
restraunt_service.create_order("pizza")