#Line 1 - I was getting a random number between 5 and 20. Smallest number is 5 and largest was 20

#Line 2 - I was getting odd numbers. Smallest number is 3 and the largest is 9

#Line 3 - Random numbers again but not integers. Smallest number would be 2.5 and 5.5 would be the biggest.

import random

MENU = "G - Get random number\nQ- Quit"

def main():
    print(MENU)
    choice = input(">> ").upper()

    while choice != "Q":
        if choice == "G":
            random_number = random.randint(1, 100)
            print(f"Random number is {random_number}")
        else:
            print("Invalid")
        print(MENU)
        choice = input(">> ").upper()
    print("Goodbye")

main()