print("Welcome to the tip calcuator")
total_bill= input(" What was the total bill?")
percentage= input(" what percentage tip would you like to give?")
person = input(" How many people to split the bill? ")

cal = int(percentage) /100 * int(total_bill) + int(total_bill)
bill = cal / int(person)
# new_bill = round (bill,2)
new_bill = "{:.2f}".formate(bill)
print(new_bill)