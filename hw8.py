# Define the BMW class
class BMW:
    def start_engine(self):
        print("BMW engine starts with a smooth rrrrr.")

    def drive(self):
        print("Driving the BMW with sportiness meanwhile with luxury.")

# Define the Ferrari class
class Ferrari:
    def start_engine(self):
        print("Ferrari engine roars to life with like a lion.")

    def drive(self):
        print("Driving the Ferrari with speed and smoothness.")

# Define a function that uses polymorphism
def test_drive(car):
    car.start_engine()
    car.drive()
    print("-" * 40)

# Create objects of both classes
bmw_car = BMW()
ferrari_car = Ferrari()

# Use the same function to operate on different objects
test_drive(bmw_car)
test_drive(ferrari_car)
