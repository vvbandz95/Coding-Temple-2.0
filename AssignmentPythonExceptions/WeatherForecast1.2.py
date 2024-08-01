# 1.2

def fahrenheit_to_celsius(temp_fahrenheit):
    try:
        celsius = (temp_fahrenheit - 32) * 5/9
        return celsius
    except TypeError:
        print("Error: The input must be a numeric value.")
        return None

def main():
    while True:
        try:
            temp_input = input("Please enter the temperature in Fahrenheit: ")
            
            temp_fahrenheit = float(temp_input)
            
            temp_celsius = fahrenheit_to_celsius(temp_fahrenheit)
            
            if temp_celsius is not None:
                print(f"The temperature in Celsius is {temp_celsius:.2f}°C.")
                break
        
        except ValueError:
            print("Invalid input. Please enter a numeric value for the temperature.")

if __name__ == "__main__":
    main()
78