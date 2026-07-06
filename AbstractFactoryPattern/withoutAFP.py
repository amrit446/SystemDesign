from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass



class PaneerTikka(Food):
    def prepare(self):
        print("Prepaing Paneer Tikka (North Indian Starter)")




    
class ButterChicken(Food):
    def prepare(self):
        print("Prepaing Butter Chicken (North Indian Starter)")




class GulabJamun(Food):
    def prepare(self):
        print("Prepaing Gulab Jamun (North Indian Starter)")




# =================== SOUTH INDIAN DISHES ===================================
class MeduVada(Food):
    def prepare(self):
        print("Preparing Medu Vasa (South Indian Startrt)")



class Dosa(Food):
    def prepare(self):
        print("Preparing Dosa (South Indian Main Course)")



class Payasam(Food):
    def prepare(self):
        print("Preparing Payasam (South Indian Dessert)")





#=========================== Chinese Dishes ================

class SoringRolls(Food):
    def prepare(self):
        print("Preparing Sping Rolls (Chiness Starter)")


class FriedRice(Food):
    def prepare(self):
        print("Preparing Fried  Rice (Chiness Starter)")


class FortuneCookie(Food):
    def prepare(self):
        print("Preparing Fortune Cookie (Chiness Starter)")



class RestrauntService:
    def create_meal(self, cuisine_type:str):
        if cuisine_type == "north_indian":
            starter = PaneerTikka()
            main_course = ButterChicken()
            desert = GulabJamun()
 
        elif cuisine_type == "south_indian":
            starter = MeduVada()
            main_course = Dosa()
            desert = Payasam()


        elif cuisine_type == "chinese":
            starter = SoringRolls()
            main_course = FriedRice()
            desert = FortuneCookie()

        else:
            print("Cuisine not available!")
            return None


        starter.prepare()
        main_course.prepare()
        desert.prepare()
        


restaurant = RestrauntService()
restaurant.create_meal("north_indian")
restaurant.create_meal("south_indian")