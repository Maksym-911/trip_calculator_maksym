#Author: Maksym
#Date Modified: May 2, 2025
#Description: summative

import random

# Introduction
print("\n=== Trip Cost Calculator ===")

# Trips amount
while True:
    try:
        num_trips = int(input("How many trips do you want to calculate? ")) # Input
        if num_trips <= 0:
            print("Value must be greater than zero.")
        # Successfully
        else:
            break
    # Error check on anything exsept numbers
    except ValueError:
        print("Please enter a number.")

# Loop through each trip
for i in range(num_trips):
    print(f"\n--- Trip {i+1} ---")

    # Distance choice
    while True:
        distance_choice = input("Do you want to type your own distance, or let the computer pick it for you? (1 = own / 2 = random): ") # Input
        # Successfully
        if distance_choice in ("1", "2"):
            break
        # Error check on anything exsept 1 or 2
        else:
            print("Please enter either 1 or 2.")

    # Random distance
    if distance_choice == "2":
        distance = random.randint(1, 13000)
        print(f"Randomly selected distance: {distance} km")
    else:
        while True:
            try:
                # Your own distance
                distance = float(input("Enter the distance in km: "))
                if distance <= 0:
                    print("Distance must be greater than 0.")
                # Successfully
                else:
                    break
            # Error check on anything exsept numbers
            except ValueError:
                print("Please enter a number.")

    # Transport preference
    while True:
        transport = input("What's your transport (bike or car): ").lower()
        # Successfully
        if transport in ("bike", "car"):
            break
        # Error check on anything exsept bike or car
        else:
            print("Please enter either 'bike' or 'car'.")
    # Bikes don't require any fuel calculations
    if transport == "bike":
        print("Good luck 🚴‍♂️")
        continue 

    # Fuel consumption (liters/100 km)
    while True:
        try:
            fuel_consumption = float(input("Enter fuel consumption (liters/100 km): "))
            if fuel_consumption <= 0:
                print("Fuel consumption must be greater than 0.")
            # Successfully
            else:
                break
        # Error check on anything exsept numbers
        except ValueError:
            print("Please enter a number.")

    # Price per liter
    while True:
        try:
            price_per_liter = float(input("Enter the price per liter of fuel: "))
            if price_per_liter <= 0:
                print("Price per liter must be greater than 0.")
            # Successfully
            else:
                break
        # Error check on anything exsept numbers
        except ValueError:
            print("Please enter a number.")

    # Calculation
    liters_needed = (fuel_consumption / 100) * distance
    total_cost = liters_needed * price_per_liter

    # Output
    print(f"\nTrip {i+1} Results:")
    print(f"Distance: {distance:.2f} km")
    print(f"Fuel needed: {liters_needed:.2f} liters")
    print(f"Trip cost: ${total_cost:.2f} CAD")

print("\nThanks for using the calculator!")
