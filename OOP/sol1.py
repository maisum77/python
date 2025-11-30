class Car:
    def input(self,name,model):
        self.__name=name
        self.model=model
    def show(self):
        print(f"name of the car is {self.__name}, model is {self.model}")
    def get_name(self):
        return self.__name
    @staticmethod
    def description():
        return "cars are moving fastt!! really really fast"
class Eclectric(Car):
    def __init__(self, name, model, battery):
        self.battery=battery
        super().input(name, model)
        super().get_name()
    def show(self):
        print(f"name of the car is {self.get_name()}, model is {self.model},battery oof the car is {self.battery}")


my=Car()
my.input("bmw",2025)
my.show() 
print(Car.description())
e1=Eclectric("tesla", 2024, 123)
e1.show()