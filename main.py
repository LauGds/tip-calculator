print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
tip_new = float((tip + 100) / 100)

people = int(input("How many people to split the bill? "))
result = round((bill / people) * tip_new, 2)

result_end = "{:.2f}".format(result)
print(f"Each person should pay: ${result_end}")
