import calculations_external as calculations_external
import time


def main():
    try:

        while True:

            user_operation = input("Enter an operation +, - , *, / , % , ^ or q to quit: ")
            while user_operation not in ["+", "-", "*", "/", "%", "^", "q"]:
                print("Enter a valid input.")
                user_operation = input("Enter an operation +, - , *, / , %, ^ or q to quit: ")
            if user_operation == 'q': break
            number1 = float(input("enter 1st value: "))
            number2 = float(input("enter 2nd value: "))
            result = calculations_external.calculate(user_operation, number1, number2)

            print(number1, user_operation, number2, " = ", format(result, '.2f'))

        calculations_external.greetings()
    except ZeroDivisionError:
        print("You cannot divide by zero. Try Again")
        main()
    except ValueError:
        print("Please enter a number. Try Again")
        main()
    except:
        print("Something went wrong. Program will restart.")
        time.sleep(4)
        main()

main()