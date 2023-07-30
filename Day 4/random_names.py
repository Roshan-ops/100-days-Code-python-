import random


names_string = input(" Give me everybody name seperated by comma. ")
names = names_string.split(",")
num_items = len (names)

random_choise = random.randint(0, num_items - 1)
# print(random_choise)
person_buy = names[random_choise]
print(person_buy + " is going to pay for the meal toaday. ")