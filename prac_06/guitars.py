"""
Estimate: 20 mins
Actual: 18 mins
"""

from prac_06.guitar import Guitar

def main():
    print("My Guitars!")
    guitars = []

    name = input("Name: ").strip
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)

        print(f"{guitar} added.\n")

        name = input("Name: ").strip

    #guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    #guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

if __name__ == "__main__":
    main()