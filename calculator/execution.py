from functions import *
import time

print("Welcome to the Simple Calculator!")
print("Choose an operation:")
print("1 - Multiply")
print("2 - Add")
print("3 - Subtract")

while True:
    ask_unit = input("Please select an operation (1, 2, or 3) or type 'exit' to quit: ").strip()
    
    if ask_unit.lower() == 'exit':
        print("Thank you for using the calculator! Goodbye!")
        break

    time.sleep(1)

    if ask_unit == "1":
        ask_number = float(input("Great choice! Please enter the first number: "))
        ask_numbers = float(input("Now, please enter the second number: "))
        result = multiply(ask_number, ask_numbers)
        print(f"{ask_number} multiplied by {ask_numbers} equals {result}.")

    elif ask_unit == "2":
        ask_number = float(input("Awesome! Enter the first number: "))
        ask_numbers = float(input("And the second number: "))
        result = add(ask_number, ask_numbers)
        print(f"{ask_number} plus {ask_numbers} equals {result}.")

    elif ask_unit == "3":
        ask_number = float(input("Alright! Please provide the first number: "))
        ask_numbers = float(input("Now, enter the second number: "))
        result = subtract(ask_number, ask_numbers)
        print(f"{ask_number} minus {ask_numbers} equals {result}.")

    else:
        print("Oops! That doesn't seem like a valid option. Please choose 1, 2, or 3.")

        
        

