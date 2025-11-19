from unreliable_car import UnreliableCar

def main():
    successful_attempts = 0
    attempts = 1000

    for _ in range(attempts):
        test_car = UnreliableCar("Prius", 10, 75)
        distance_driven = test_car.drive(10)
        # print(test_car)
        if distance_driven > 0:
            successful_attempts += 1

    print(f"Out of {attempts} attempts, {successful_attempts} were successful.")

main()