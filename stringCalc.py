import choice


def empty():
    raise NotImplementedError


def str_simple():  # 12
    operations = {
        "+": (empty, "addition"),
        "*": (empty, "multiplication"),
    }
    operation = choice.menu_str(operations)
    if operation == '+':
        line_1 = input('Enter the first line: ')
        line_2 = input('Enter the second line: ')
        print(line_1 + line_2)
    if operation == '*':
        line = input('Enter the line: ')
        number = input('Enter the number: ')
        print(line * number)


def str_showcenter():  # 13
    line = input("Enter the line: ")
    for i in range(12):
        print()
    print(line.center(80))
    for i in range(12):
        print()


def str_words():  # 14
    line = input("Enter the line: ")
    print(len(line), len(line.split()))


def menu_strings():
    operations = {
        1: (str_simple, "simple string operations"),
        2: (str_showcenter, "center string output"),
        3: (str_words, "word and character count")
    }
    operations[choice.menu(operations)][0]()


if __name__ == "__main__":
    menu_strings()
