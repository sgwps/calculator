def menu(operations):
    for i in operations.keys():
        print(f"Enter {i} for {operations[i][1]}")
    action = int(input())
    while True:
        try:
            if action not in operations.keys():
                raise ValueError
            return action
        except ValueError:
            action = int(input("Enter the proper number: "))


def menu_str(operations):
    for i in operations.keys():
        print(f"Enter {i} for {operations[i][1]}")
    action = input()
    while True:
        try:
            if action not in operations.keys():
                raise ValueError
            return action
        except ValueError:
            action = int(input("Enter the proper value: "))


if __name__ == "__main__":
    print()