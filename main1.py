print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

tip = bill * (tip_percentage / 100)
total_per_person = (bill + tip) / people

print(f"Each person should pay: ${total_per_person:.2f}")
