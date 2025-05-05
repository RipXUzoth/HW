import math

def calculate_trig_values():
    try:
        angle_deg = float(input("Enter angle in degrees: "))
        angle_rad = math.radians(angle_deg)  # Convert degrees to radians

        sin_val = math.sin(angle_rad)
        cos_val = math.cos(angle_rad)
        try:
            tan_val = math.tan(angle_rad)
        except:
            tan_val = "undefined"

        print(f"sin({angle_deg}) = {sin_val:.4f}")
        print(f"cos({angle_deg}) = {cos_val:.4f}")
        print(f"tan({angle_deg}) = {tan_val if abs(cos_val) > 1e-10 else 'undefined (cos is zero)'}")

    except ValueError:
        print("Error: Please enter a valid number.")

# Run the function
calculate_trig_values()