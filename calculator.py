def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error: You cannot divide by Zero. Try again!"
    else:
        return x / y

def modulus(x, y):
    if y == 0:
        return "Error: You cannot calculate modulus by Zero. Try again!"
    else:
        return x % y

def calcu():
    
    print("Select operation: \n1. Add \n2. Subtract \n3. Multiply \n4. Divide \n5. Modulus")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice in ("1", "2", "3", "4", "5"):
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print(f"{num1} + {num2} = {addition(num1, num2)}")
            elif choice == "2":
                print(f"{num1} - {num2} = {subtraction(num1, num2)}")
            elif choice == "3":
                print(f"{num1} * {num2} = {multiplication(num1, num2)}")
            elif choice == "4":
                print(f"{num1} / {num2} = {division(num1, num2)}")
            elif choice == "5":
                print(f"{num1} % {num2} = {modulus(num1, num2)}") 
                               
        except ValueError:
            print("Error: Please enter valid numbers. Try again!")
            
    else:
        print("Invalid! Try again by choosing a number (1/2/3/4/5).")

calcu()

# MD. Habibul Basher
# Ostad : Assignment | Module 5 | 15th September