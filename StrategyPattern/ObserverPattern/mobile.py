from observer import Observer

class MobileDisplay(Observer):
    def update(self, temp):
        print(f"mobile temprature updated:{temp}")