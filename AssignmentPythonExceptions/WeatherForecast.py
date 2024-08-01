#1

def get_temperature():
    while True:
        try:
            temp_fahrenheit = input("Please enter the temperature in Fahrenheit: ")

            temperature = float(temp_fahrenheit)
            return temperature
        
        except ValueError:
            print("Invalid input. Please enter a numeric value for the temperature.")

def main():
    temperature = get_temperature()
    print(f"The temperature you entered is {temperature}°F.")

if __name__ == "__main__":
    main()
