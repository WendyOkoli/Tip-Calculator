print( "Welcome to the tip calculator." )
total_bill = float(input("What was the total bill?  $"))
tip = int(input("How much tip will you like to give? 10, 12, 15? "))
num_people = int(input("How many people will split the bill? "))
                 
percentage_tip = tip / 100
total_amount_to_tip = total_bill * percentage_tip
total_bill_as_amount = total_bill + total_amount_to_tip
individual_bill = total_bill / num_people
final_amount = round(individual_bill, 2)
print(f"Each person should pay: ${final_amount}")

