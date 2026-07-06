from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass


class Starter(ABC):
    @abstractmethod
    def prepare(self):
        pass


class MainCourse(ABC):
    @abstractmethod
    def prepare(self):
        pass


class Dessert(ABC):
    @abstractmethod
    def prepare(self):
        pass




#================= North Indian Dishes=======
class PaneerTikka(Starter):
    def prepare(self):
        print("Prepaing Paneer Tikka (North Indian Starter)")




    
class ButterChicken(MainCourse):
    def prepare(self):
        print("Prepaing Butter Chicken (North Indian Starter)")




class GulabJamun(Dessert):
    def prepare(self):
        print("Prepaing Gulab Jamun (North Indian Starter)")




# =================== SOUTH INDIAN DISHES ===================================
class MeduVada(Starter):
    def prepare(self):
        print("Preparing Medu Vasa (South Indian Startrt)")



class Dosa(MainCourse):
    def prepare(self):
        print("Preparing Dosa (South Indian Main Course)")



class Payasam(Dessert):
    def prepare(self):
        print("Preparing Payasam (South Indian Dessert)")





#=========================== Chinese Dishes ================

class SoringRolls(Starter):
    def prepare(self):
        print("Preparing Sping Rolls (Chiness Starter)")


class FriedRice(MainCourse):
    def prepare(self):
        print("Preparing Fried  Rice (Chiness Starter)")


class FortuneCookie(Dessert):
    def prepare(self):
        print("Preparing Fortune Cookie (Chiness Starter)")




class CuisineFactory(ABC):
    @abstractmethod
    def create_starter(self)->Starter:
        pass

    @abstractmethod
    def create_main_course(self)->MainCourse:
        pass

    @abstractmethod
    def create_dessert(self)->Dessert:
        pass


class NorthIndianCuisine(CuisineFactory):
    def create_starter(self)->Starter:
        return PaneerTikka()

    def create_main_course(self)->MainCourse:
        return ButterChicken()

    def create_dessert(self)->Dessert:
        return GulabJamun()


    



class RestrauntService:
    def __init__(self,factory:CuisineFactory):
        self.__factory = factory


    def create_meal(self):
        start = self.__factory.create_starter()
        main_course = self.__factory.create_main_course()
        dessert = self.__factory.create_dessert()




        start.prepare()
        main_course.prepare()
        dessert.prepare()


north_indian_cuisine = NorthIndianCuisine()
restautrant_service  = RestrauntService(north_indian_cuisine)
restautrant_service.create_meal()



        

