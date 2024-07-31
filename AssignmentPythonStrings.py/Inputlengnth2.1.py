# 2.1 

def valid_name(name, field_name):
    "Check if the name is at least 2 characters long and return True if valid."
    if len(name) < 2:
        print(f"Error: {field_name} must be at least 2 characters long.")
        return False
    return True

def main():
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()
    
    if valid_name(first_name, "First name") and valid_name(last_name, "Last name"):
        print("Both names are valid.")
    else:
        print("Please provide valid names.")

if __name__ == "__main__":
    main()
