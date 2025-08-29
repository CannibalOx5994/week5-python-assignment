class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand      # brand name
        self.model = model      # model name
        self.storage = storage  # storage in GB
        self.battery = battery  # battery % remaining

    def charge(self, amount):
        self.battery += amount
        if self.battery > 100:
            self.battery = 100
        print(f"{self.model} charged to {self.battery}%.")

    def use_app(self, app_name, usage):
        self.battery -= usage
        if self.battery < 0:
            self.battery = 0
        print(f"{app_name} used! Battery now at {self.battery}%.")

class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        super().__init__(brand, model, storage, battery)  # call parent constructor
        self.cooling_system = cooling_system

    def activate_cooling(self):
        print(f"{self.model}'s {self.cooling_system} cooling system activated!")

phone1 = Smartphone("Apple", "iPhone 14", 128, 80)
phone1.use_app("Instagram", 10)
phone1.charge(15)

gaming_phone = GamingPhone("Asus", "ROG Phone 6", 256, 60, "Advanced Liquid Cooling")
gaming_phone.activate_cooling()
gaming_phone.use_app("Genshin Impact", 20)



class Vehicle:
    def move(self):
        pass  # base class doesn’t define specific movement

class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying")

class Boat(Vehicle):
    def move(self):
        print("Sailing")

vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()  # Python calls the correct move() for each object

