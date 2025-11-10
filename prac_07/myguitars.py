
from guitar import Guitar

MENU = "D - Display Guitars\nA - Add Guitars\nQ - Quit"

def main():
    guitars = read_guitars_file("guitars.csv")
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "D":
            display_guitars(guitars)
        elif choice == "A":
            guitars = add_guitars(guitars)
        else:
            print("Invalid menu option")
        print(MENU)
        choice = input(">>>").upper()
    save_guitars("guitars.csv", guitars)



def read_guitars_file(file_name):
    guitars = []
    with open(file_name, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)
    return guitars

def save_guitars(file_name, guitars):
    with open(file_name, 'w') as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)
    print(f"\nGuitars have been saved to {file_name}")

def display_guitars(guitars):
    guitars.sort()
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")

def add_guitars(guitars):
    return guitars

main()


