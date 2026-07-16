# A simple calculator that performs basic arithmetic operations

def execute(a, b, choice):
    """Performs the arithmetic operation based on the user's choice."""
    a = int(a)
    b = int(b)
    choice = choice.strip()   # Fixed assignment

    if choice == '1':
        return f'{a} + {b} = {a + b}'

    elif choice == '2':
        return f'{a} - {b} = {a - b}'

    elif choice == '3':
        return f'{a} × {b} = {a * b}'

    elif choice == '4':
        if b == 0:
            return "Error: Cannot divide by zero."
        elif a % b == 0:
            return f'{a} ÷ {b} = {a // b}'
        else:
            return f'{a} ÷ {b} = {a / b}'

    else:
        return f'Error: "{choice}" is an invalid choice'


def is_valid(user_input):
    """Checks whether the input is a valid integer."""
    try:
        int(user_input.strip())
        return True
    except ValueError:
        print(f'"{user_input}" is not valid')
        return False


def valid_choice(choice):
    choice = choice.strip()
    return choice in {'1', '2', '3', '4'}


def quit_program(response):
    return response.strip().lower() not in ['y', 'yes']


def main():
    while True:
        print('\nPERFORM SIMPLE CALCULATIONS')

        a = input('Enter the first number: ')
        if not is_valid(a):
            print('Calculator stopped')
            break

        b = input('Enter the second number: ')
        if not is_valid(b):
            print('Calculator stopped')
            break

        operand = input(
            f'Pick a number:\n'
            f'1 for {a} + {b}\n'
            f'2 for {a} - {b}\n'
            f'3 for {a} × {b}\n'
            f'4 for {a} ÷ {b}\n'
            f'Your choice: '
        )

        if not valid_choice(operand):
            print(f'"{operand}" is not a valid choice.')
            break

        print(execute(a, b, operand))

        response = input(
            "\nEnter 'y' or 'yes' to perform another calculation, "
            "or anything else to quit.\nYour response: "
        )

        if quit_program(response):
            print("Bye!")
            break


if __name__ == "__main__":
    main()