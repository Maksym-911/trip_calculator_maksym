#Trip Cost Calculator

This program helps users calculate the fuel cost of multiple trips.

Here's how it works step-by-step:

1. Trip Count:  
   The user is first asked how many trips they want to calculate.

2. Trip Loop (`for i in range(num_trips)`): 
   The program repeats the trip calculation for the number of times the user entered.

3. Distance Input Choice:
   - The user decides if they want to **manually enter the distance** or let the **computer randomly choose** a distance between 1 and 13,000 km.

4. Transport Type:
   - The user is asked whether they are using a **bike** or a **car**.
   - If they choose "bike", the program skips the fuel calculation (because bikes don't need fuel).

5. Fuel Consumption & Fuel Price:
   - If the transport is a car, the user enters:
     - How much fuel their car uses per 100 km (`liters/100 km`)
     - The current **fuel price per liter**

6. Cost Calculation:
   - The program calculates how many liters are needed using the formula:  
     `(fuel consumption / 100) * distance`
   - Then it multiplies the liters needed by the fuel price to get the total cost.

7. Results:
   - It displays the amount of fuel needed and the total cost of the trip in Canadian dollars.

8. End:
   - After all trips are calculated, the program says thank you and ends.
