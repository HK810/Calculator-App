#!/usr/bin/env python3

def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

def power(x, y):
    """Raise x to the power of y"""
    return x ** y

def display_menu():
    """Display the calculator menu"""
    print("\n" + "="*40)
    print("          SIMPLE CALCULATOR")
    print("="*40)
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Exit")
    print("="*40)

def get_number(prompt):
    """Get a valid number from user input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def main():
    """Main calculator function"""
    print("Welcome to the Simple Calculator!")
    
    while True:
        display_menu()
        
        # Get user choice
        try:
            choice = input("Enter your choice (1-6): ").strip()
        except KeyboardInterrupt:
            print("\n\nCalculator closed. Goodbye!")
            break
        
        # Handle menu choices
        if choice == '6':
            print("Thank you for using the calculator. Goodbye!")
            break
        elif choice in ['1', '2', '3', '4', '5']:
            # Get two numbers from user
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            
            # Perform calculation based on choice
            if choice == '1':
                result = add(num1, num2)
                operation = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "*"
            elif choice == '4':
                result = divide(num1, num2)
                operation = "/"
            elif choice == '5':
                result = power(num1, num2)
                operation = "^"
            
            # Display result
            print(f"\nResult: {num1} {operation} {num2} = {result}")
            input("\nPress Enter to continue...")
        else:
            print("Invalid choice! Please enter a number between 1-6.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
