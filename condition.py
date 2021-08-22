'''
if-elif-else
conditions can be ==, !=, <, >, <=, >=, and, or, not
'''

temp = 10
if temp > 30:
    print("It's a hot day!")
    print("Drink plenty of water.")
elif temp > 20:
    print("It's a nice day!")
elif temp > 10:
    print("It is bit cold today!")
else:
    print("It's a cold day!")

print("Done")

# Condition with the logical operators
age = 30
if((age >= 1) and (age <= 18)):
    print("You get a Pen in birthday gift")
elif((age == 21) or (age >= 65)):
    print("You get a iPad in birthday gift")
elif not(age == 30):
    print("You don't get a birthday gift")
else:
    print("You get a birthday Party, Yeah!!!")


# Weight conversion example
weight = int(input("Enter your weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kg: " + str(converted))
