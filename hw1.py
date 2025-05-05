def decimal_to_binary(decimal):
    if decimal == 0:
        return "0"
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary

# Example usage
try:
    num = int(input("Enter a decimal number: "))
    print("Binary representation:", decimal_to_binary(num))
except ValueError:
    print("Please enter a valid integer.")