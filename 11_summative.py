import random
import math

print("\n=== Trip Cost Calculator ===")
num_trips = int(input("How many trips do you want to calculate? "))
for i in range(num_trips):
    print(f"\n🚗 Trip {i+1}")
    
    # Distance input
    print("Do you want to type your own distance, or let the computer pick it for you?")
    distance_choice = int(input("(1/2): "))
    while distance_choice != 1 and distance_choice != 2:
        print("Choose between 1 and 2")
        distance_choice = int(input("(1/2): "))
    
    if distance_choice == 2:
        distance = random.randint(1, 13000)
        print(distance, "km")
    else:
        distance = float(input("Enter the distance in km: "))
        while distance <= 0:
            print("Distance must be greater than 0.")
            distance = float(input("Enter the distance in km: "))

    transport = str(input("What's your transport (bike or car): ")).lower()
    if transport == "bike":
        print("Good luck 🚴‍♂️")
        continue  # Skip the rest and go to the next trip

    fuel_consumption = float(input("Enter fuel consumption (liters/100 km): "))
    while fuel_consumption <= 0:
        print("Fuel consumption must be greater than 0.")
        fuel_consumption = float(input("Enter fuel consumption (liters/100 km): "))

    price_per_liter = float(input("Enter the price per liter of fuel: "))
    while price_per_liter <= 0:
        print("Price must be greater than 0.")
        price_per_liter = float(input("Enter the price per liter of fuel: "))

    # Calculation
    liters_needed = (fuel_consumption / 100) * distance
    total_cost = liters_needed * price_per_liter

    # Output
    print(f"\n🔧 Trip {i+1} Results:")
    print(f"Fuel needed: {liters_needed:.2f} liters.")
    print(f"Trip cost: ${total_cost:.2f} CAD.")

print("Thanks for using the calculator! 🚗")