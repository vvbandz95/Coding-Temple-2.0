# 1.4 

def fahrenheit_to_celsius(temp_fahrenheit):
    try:
        celsius = (temp_fahrenheit - 32) * 5 / 9
        return celsius
    except TypeError:
        print("Error: The input must be a numeric value.")
        return None

def main():
    while True:
        try:
            temp_input = input("Please enter the temperature in Fahrenheit: ")
            temp_fahrenheit = float(temp_input)
        
        except ValueError:
            print("Invalid input. Please enter a numeric value for the temperature.")
        
        else:
            temp_celsius = fahrenheit_to_celsius(temp_fahrenheit)
    
            print(f"{temp_fahrenheit} degrees Fahrenheit is {temp_celsius:.2f} degrees Celsius.")
            break  # Exit the loop once a valid conversion is made
        
        finally:
            print("Thank you for using the weather forecast application!")

if __name__ == "__main__":
    main()
