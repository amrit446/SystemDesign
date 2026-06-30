class PhoneDisplay:
    def update(self,new_temp):
        print(f"phone display={new_temp}")

class TVDisplay:
    def update(self,new_temp):
        print(f"TV display={new_temp}")

class WeatherStation:
    def __init__(self):
        self.__temprature = 0
        self.__phone_display = PhoneDisplay()
        self.__tv_display = TVDisplay()

    def update_temprature(self,new_temp):
        self.__temprature = new_temp
        self.notify_display()

    def notify_display(self):
        self.__phone_display.update(self.__temprature)
        self.__tv_display.update(self.__temprature)

ws = WeatherStation()
ws.update_temprature(30)