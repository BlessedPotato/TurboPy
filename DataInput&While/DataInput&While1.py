# 7.1

print("What car would you like to rent, brother?")
car_rent = input()
print(f"Yo, i really want to ride this awesome {car_rent.title()}!")

print("\n")

# 7.2

print("Hello, good sir, and welcome to the Max's Finest restaurant!")
print("Would you like to make a reservation? How many people you brought today with you?")

people_quantity = int(input())

input(f"Good day to you, sir, there are {people_quantity} hungry mouths with me today!")

if people_quantity > 8:
    print("I'm so sorry, gentleman, but I've got no such big tables right now. I'm afraid you need to wait a little bit"
          "")

else:
    print(f"The table for {people_quantity} guests is done and ready! Have a nice evening!")

print("\n")

# 7.3

print("Anon, write your number here, please")

user_num = int(input())

print(f"The number is {user_num}")

if user_num % 10 == 0:
    print("Your number is divisible by 10")

else:
    print("Your number is not divisible by 10")


# Well done, buddy


