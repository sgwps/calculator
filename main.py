import stringCalc
import numberCalc
import choice


def menu():
    print("Hello, User")
    while True:
        operations = {
            1: (numberCalc.menu_numbers, "numbers calculator"),
            2: (stringCalc.menu_strings, "string calculator"),
        }
        operations[choice.menu(operations)][0]()


menu()
