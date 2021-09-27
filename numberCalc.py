import math
import choice


def empty():
    raise NotImplementedError


def calc_simple():  # 1
    number_1 = int(input("Enter the first number: "))
    number_2 = int(input("Enter the second number: "))
    operations = {
        "+": (empty, "addition"),
        "-": (empty, "subtraction"),
        "*": (empty, "multiplication"),
        "/": (empty, "division")
    }
    operation = choice.menu_str(operations)
    if operation == "+":
        print(number_1 + number_2)
    elif operation == "-":
        print(number_1 - number_2)
    elif operation == "*":
        print(number_1 * number_2)
    elif operation == "/":
        while True:
            try:
                if number_2 != 0:
                    print(number_1 / number_2)
                else:
                    raise ValueError
                break
            except ValueError:
                number_2 = int(input("Division by zero is impossible, enter the second number again: "))
    else:
        raise ValueError


def exponentiation():  # 2
    number = int(input("Enter the number: "))
    power = int(input("Enter the power for the number: "))
    print(number ** power)


def reminder():
    number_1 = int(input("Enter the first number: "))
    number_2 = int(input("Enter the second number: "))
    while True:
        try:
            if number_2 != 0:
                print(number_1 % number_2)
            else:
                raise ValueError
            break
        except ValueError:
            number_2 = int(input("Division by zero is impossible, enter the second number again: "))


def square_root():
    number = int(input("Enter the number: "))
    while True:
        try:
            if number >= 0:
                print(math.sqrt(number))
            else:
                raise ValueError
            break
        except ValueError:
            number = int(input("Getting the square root of a negative number is impossible, enter the number again: "))


def calc_extended():
    operations = {
        1: (exponentiation, "exponentiation"),
        2: (reminder, "finding the reminder of division"),
        3: (square_root, "finding the square root")
    }
    operations[choice.menu(operations)][0]()


def sine_deg(angle):
    angle %= 360
    coeff = 1
    if angle in range(180, 360):
        coeff = -1
    if abs(angle % 180 - 90) == 90:
        return 0
    elif abs(angle % 180 - 90) == 60:
        return 0.5 * coeff
    elif abs(angle % 180 - 90) == 45:
        if coeff == 1:
            return '√2/2'
        else:
            return '-√2/2'
    elif abs(angle % 180 - 90) == 30:
        if coeff == 1:
            return '√3/2'
        else:
            return '-√3/2'
    elif angle == 90:
        return 1
    else:
        return math.sin(math.radians(angle))


def cosine_deg(angle):
    angle %= 360
    if angle == 180:
        return -1
    if angle == 0:
        return 1
    angle %= 180
    if angle in range(90, 180):
        coeff = -1
    if abs(angle % 180 - 90) == 0:
        return 0
    elif abs(angle % 180 - 90) == 30:
        return 0.5 * coeff
    elif abs(angle % 180 - 90) == 45:
        if coeff == 1:
            return '√2/2'
        else:
            return '-√2/2'
    elif abs(angle % 180 - 90) == 60:
        if coeff == 1:
            return '√3/2'
        else:
            return '-√3/2'
    elif angle == 90:
        return 1
    else:
        return math.cos(math.radians(angle))


def calc_degrees():  # 3
    angle = int(input('Enter the angle in degrees: '))
    operations = {
        1: (sine_deg, "sine"),
        2: (cosine_deg, "cosine"),
    }
    print(operations[choice.menu(operations)][0](angle))


def calc_radians():  # 4
    angle = float(input('Enter the angle in radians: '))
    operations = {
        1: (math.sin, "sine"),
        2: (math.cos, "cosine"),
    }
    print(operations[choice.menu(operations)][0](angle))


def calc_logic():  # 5
    operations = {
        1: (empty, "conjunction"),
        2: (empty, "disjunction"),
        3: (empty, "denial")
    }
    action = choice.menu(operations)
    if action == 1:
        value_1 = int(input('Enter the first value: '))
        value_2 = int(input('Enter the second value: '))
        if value_1 and value_2:
            print(1)
        else:
            print(0)
    elif action == 2:
        value_1 = int(input('Enter the first value: '))
        value_2 = int(input('Enter the second value: '))
        if value_1 or value_2:
            print(1)
        else:
            print(0)
    else:
        value = int(input('Enter the value: '))
        if value:
            print(0)
        else:
            print(1)


def calc_10_2():  # 6 - 9
    a = int(input("Input number in dec: "))
    print(bin(a)[2:])


def calc_10_16():
    a = int(input("Input number in dec: "))
    print(hex(a)[2:])


def calc_10_8():
    a = int(input("Input number in dec: "))
    print(oct(a)[2:])


def menu_logic():
    operations = {
        1: (calc_10_2, "conversion to binary"),
        2: (calc_10_8, "conversion to octal"),
        3: (calc_10_16, "conversion to hexadecimal")
    }
    operations[choice.menu(operations)][0]()


def check_brackets():  # 10
    line = input("Enter the formula: ")
    c = 0
    for i in line:
        if i == '(':
            c += 1
        elif i == ')':
            c -= 1
            if c < 0:
                break
    if c == 0:
        print("YES")
    else:
        print("NO")


def menu_numbers():
    operations = {
        1: (calc_simple, "simple operations"),
        2: (calc_extended, "extended operations"),
        3: (calc_degrees, "trigonometric degree operations"),
        4: (calc_radians, "trigonometric operations with radians"),
        5: (calc_logic, "logical operations"),
        6: (menu_logic, "converting numbers to different scale of notation"),
        7: (check_brackets, "brackets check")
    }
    operations[choice.menu(operations)][0]()


if __name__ == "__main__":
    menu_numbers()
