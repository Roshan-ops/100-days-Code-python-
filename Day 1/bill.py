print("Welcome to the tip calculator")
input_bill=float(input("What was the total bill? $ \n"))
input_tip= float(input("What percentage tip would you like to give?Type any percentage. \n"))
input_people=int(input("How many people to split the bill? \n"))
tip=input_bill*input_tip/100
totyal_bill=input_bill+tip
bill_per_person=totyal_bill/input_people

print(f"Each person should pay: ${bill_per_person:.2f}")
