from silver_service_taxi import SilverServiceTaxi


my_car = SilverServiceTaxi("Prius", 200, fanciness=2)
my_car.start_fare()
my_car.drive(18)
fare = my_car.get_fare()
print(my_car)
print(f"Fare for 18 km trip: ${fare}")
#assert fare - 48.78 == 0.0, "Fare should be $48.78" (before rounding)
assert fare - 48.80 == 0.0, "Fare should be $48.80" #after rounding

