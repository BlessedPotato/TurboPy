# 7.4

print("Welcome to \"Pizza Maximiliano\", which toppings would you like to add to your pizza? ")

custom_topp = "I would like to add an/a..."
custom_topp += "\n(Enter 'quit' when you're done)"

while True:
    order = input(custom_topp)

    if order == 'quit':
        break

    else:
        print(f"I'd love to add {order}.")


# 7.5

print("Welcome to CinemaCringe, please, enter your age.")

age = int(input())

while True:
    if age < 3:
        print("Children under age of 3 for free")

    elif 3 < age < 12:
        print("one ticket is for 10$")

    else:
        print("your ticket costs 15$")

    break


# 7.7

# while True:
#     print("OH SHIT YOU BROKE MY PC")
#     pass



