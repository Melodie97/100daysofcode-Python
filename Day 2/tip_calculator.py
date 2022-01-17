print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
no_of_people = int(input("How many people to split the bill? "))

tip = total_bill * (tip_percent/100)
to_pay_each = (total_bill + tip) / no_of_people
rounded_bill = round(to_pay_each, 2)
print(f"Each person should pay: {rounded_bill}")
