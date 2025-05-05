import math

def calculate_circumference(radius):
    return 2 * math.pi * radius

# Example usage
try:
    r = float(input("Enter the radius of the circle: "))
    circumference = calculate_circumference(r)
    print(f"The circumference of the circle is: {circumference:.2f}")
except ValueError:
    print("Please enter a valid number.")