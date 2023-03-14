print("Welcome to the tip calculator")
bill = float(input("What was the total bill? "))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100
people = int(input("How many people are splitting this bill? "))
tip_percent = tip_percent + 1
bill_total = round(bill * tip_percent, 2)
bill_total_by_person = "{:.2f}".format(bill_total / people)
# make sure we have two 0 ^^
print(f"Each person should pay {bill_total_by_person}")
