
def main():
    numbers = get_numbers() # part 1
    print_numbers_results(numbers) # part 1

    check_username() # part 2

def get_numbers():
    """Ask user for 5 numbers and store them"""
    numbers = []
    for _ in range(5):
        number = float(input("Enter number: "))
        numbers.append(number)
    return numbers

def print_numbers_results(numbers):
    """Print a summary of the numbers given"""
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

def check_username():
    """Checks if the username entered is in the given list"""
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = input("Enter username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")

main()