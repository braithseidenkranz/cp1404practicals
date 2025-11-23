from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():

    print("Let's Drive!")
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    current_taxi = None
    bill_to_date = 0.0

    print(MENU)
    choice = input(">>>").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            current_taxi = choose_taxi(taxis, current_taxi)
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                trip_cost = drive_taxi(current_taxi)
                bill_to_date += trip_cost
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
        else:
            print("Invalid option")

        print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU)
        choice = input(">>>").lower()

    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def choose_taxi(taxis, current_taxi):
    try:
        taxi_choice = int(input("Choose taxi: "))
        current_taxi = taxis[taxi_choice]
    except (ValueError, IndexError):
        print("Invalid taxi choice")
    return current_taxi

def drive_taxi(current_taxi):
    if current_taxi.fuel == 0:
        print(f"{current_taxi.name} has no fuel left!")
        return 0.0

    try:
        distance = float(input("Drive how far? "))
    except ValueError:
        print("Invalid distance, driving 0km")
        return 0.0

    current_taxi.start_fare()
    current_taxi.drive(distance)
    return current_taxi.get_fare()

main()