#Author: Maksym
#Date Modified: Apr 29, 2025
#Description: summative

import random
import math

#Introduction
print("\n=== Trip Cost Calculator ===")
# Trips amount
while True:
    try:
        num_trips = int(input("How many trips do you want to calculate? "))
        for i in range(num_trips):
            print(f"\nTrip {i+1}")
        if num_trips <= 0:
            print("Value must be greater than zero.")
        else:
            break
    except ValueError:
        print("Please enter a number.")

    # Distance choice
    
    print("Do you want to type your own distance, or let the computer pick it for you?")
    distance_choice = (input("(1/2): "))

    #Error check if the user doesn't input anything
    while distance_choice == "":
        print("Type something!")
        distance_choice = (input("(1/2): "))
    #Error check if the user doesn't follow the instructions
    while distance_choice != "1" and distance_choice != "2":
        print("Choose between 1 and 2")
        distance_choice = (input("(1/2): "))

    #Random distance
    if distance_choice == "2":
        distance = random.randint(1, 13000)
        print(distance, "km")

    #Your own distance
    else:
        distance = float(input("Enter the distance in km: "))
        while distance <= 0:
            print("Distance must be greater than 0.")
            distance = float(input("Enter the distance in km: "))

    #Transport preference
    transport = str(input("What's your transport (bike or car): ")).lower()
    if transport == "bike":
        print("Good luck 🚴‍♂️")
        continue  # Skip the rest and go to the next trip

    #fuel consumption (liters/100 km)
    fuel_consumption = float(input("Enter fuel consumption (liters/100 km): "))
    while fuel_consumption <= 0:
        print("Fuel consumption must be greater than 0.")
        fuel_consumption = float(input("Enter fuel consumption (liters/100 km): "))

    #Price_per_liter
    price_per_liter = float(input("Enter the price per liter of fuel: "))
    while price_per_liter <= 0:
        print("Price must be greater than 0.")
        price_per_liter = float(input("Enter the price per liter of fuel: "))

    # Calculation
    liters_needed = (fuel_consumption / 100) * distance
    total_cost = liters_needed * price_per_liter

    # Output
    print(f"\nTrip {i+1} Results:")
    print(f"Fuel needed: {liters_needed:.2f} liters.")
    print(f"Trip cost: ${total_cost:.2f} CAD")

print("Thanks for using the calculator!")