class Vehicle:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    
    def drive(self):
        print(f"The {self.color} {self.make} {self.model} drives past. Vroom vroom!")
    
    def turn(self, direction):
        print(f"The vehicle turns {direction}.")
    
    def stop(self):
        print("The vehicle stops.")

class Car(Vehicle):
    def __init__(self, make, model, year, color, num_doors):
        super().__init__(make, model, year, color)
        self.num_doors = num_doors
    
    def drive(self):
        print(f"The {self.color} {self.make} {self.model} drives past. Vroom vroom! Zoom zoom!")

    def turn(self, direction):
        print(f"The {self.color} {self.make} {self.model} turns {direction} sharply.")

    def stop(self):
        print(f"The {self.color} {self.make} {self.model} screeches to a halt.")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, color, engine_size):
        super().__init__(make, model, year, color)
        self.engine_sez = engine_size
    
    def drive(self):
        print(f"The {self.color} {self.make} {self.model} drives past. Vrrrrrm!")

    def turn(self, direction):
        print(f"The {self.color} {self.make} {self.model} leans into a {direction} turn. They're so cool.")

    def stop(self):
        print(f"The {self.color} {self.make} {self.model} comes to a sudden stop. They check their helmet strap.")

class Truck(Vehicle):
    def __init__(self, make, model, year, color, num_wheels):
        super().__init__(make, model, year, color)
        self.num_wheels = num_wheels
    
    def drive(self):
        print(f"The {self.color} {self.make} {self.model} drives past. Rumble rumble! You can feel the patriotism!")

    def turn(self, direction):
        print(f"The {self.color} {self.make} {self.model} makes a wide {direction} turn. The fake balls hanging from the tow rig swing in the opposite direction.")

    def stop(self):
        print(f"The {self.color} {self.make} {self.model} slowly comes to a stop. You can now read their weirdly aggressive conservative bumper stickers.")

class Bicycle(Vehicle):
    def __init__(self, make, model, year, color, num_gears):
        super().__init__(make, model, year, color)
        self.num_gears = num_gears
    
    def drive(self):
        print(f"The {self.color} {self.make} {self.model} pedals past. Ring ding!")

    def turn(self, direction):
        print(f"The {self.color} {self.make} {self.model} makes a tight {direction} turn. Slow down, Lance Armstrong!")

    def stop(self):
        print(f"The {self.color} {self.make} {self.model} brakes and comes to a stop. This is Nashville, so they've avoided vehicular manslaughter!")


class Bus(Vehicle):
    def __init__(self, make, model, year, color, num_passengers):
        super().__init__(make, model, year, color)
        self.num_passengers = num_passengers
    
    def drive(self):
        print(f"The {self.color} {self.make} {self.model} drives past. Did they hit a skunk?")

    def turn(self, direction):
        print(f"The {self.color} {self.make} {self.model} makes a wide {direction} turn. They're heading to Bonnaroo!")

    def stop(self):
        print(f"The {self.color} {self.make} {self.model} slowly comes to a loud, smoky stop.")

# Create instances of each vehicle
my_car = Car("Toyota", "Yaris", 2020, "black", 4)
my_motorcycle = Motorcycle("Ducati", "Scrambler", 2018, "black", "803 cc")
my_truck = Truck("Ford", "F-150", 2019, "red", 4)
my_bicycle = Bicycle("Trek", "Mountain Bike", 2021, "green", 21)
my_bus = Bus("Volkswagen", "Type 2", 1993, "blue", 9)

my_car.drive()
my_car.turn("right")
my_car.stop()

my_motorcycle.drive()
my_motorcycle.turn("left")
my_motorcycle.stop()

my_truck.drive()
my_truck.turn("right")
my_truck.stop()

my_bicycle.drive()
my_bicycle.turn("left")
my_bicycle.stop()

my_bus.drive()
my_bus.turn("right")
my_bus.stop()
