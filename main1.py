print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

calculate = bill * (tip / 100)
bill_per_person = (bill + calculate) / people
total = round(bill_per_person, 2)
total = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${total}")
