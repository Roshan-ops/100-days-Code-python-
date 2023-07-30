print("Welcom to python Pizza Deliveries! ")
size = input("What size pizza do you want ? s, m and l")
add_pepperoni = input("Do you want pepperoni? ")
extra_cheese = input("DO you want extra cheese? ")
bill = 0
if size == "s" :
bill +  = 15
elif size == "m":
bill + = 20
else: 
bill + = 25

if add_pepperoni == "y"
if size == "s"
bill + = 2
else:
    bill + = 3

if extra_cheese == "y"
bill + = 1

print(f"The total bill is ${bill}")