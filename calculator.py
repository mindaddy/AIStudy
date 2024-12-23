import os

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Error! Division by zero.")
    return x / y

def get_user_choice():
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    return input("Enter choice(1/2/3/4): ")

def get_numbers():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1, num2

def main():
    while True:
        choice = get_user_choice()

        if choice in ('1', '2', '3', '4'):
            num1, num2 = get_numbers()

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))
            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))
            elif choice == '4':
                try:
                    result = divide(num1, num2)
                    print(num1, "/", num2, "=", result)
                except ValueError as e:
                    print(e)

            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()
