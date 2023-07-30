height = float (input("enter your heightt in m: "))
weight = float (input("enter your weight in kg: "))

BMI= weight/(height **2)
new_BMI="{:.2f}".formate(BMI)

if new_BMI <= 18.5:
    print("You are underweight")
elif new_BMI <=25:
    print("You have normal weight")
elif new_BMI<=30:
    print("You are overweight")
elif new_BMI <=35:
    print("You are obese")
else:
    print("You are clinically obese")