#8.3/1

def make_shirt(shirt_size , shirt_text):
    print(f"Your shirt's size is: {shirt_size}")
    print(f"Yours shirt print is: {shirt_text}")

make_shirt("L" , "Cool t-shirt")

print("\n")

#8.3/2

def make_shirt(shirt_size = "L" , shirt_text = "Cool t-shirt"):
    print(f"Your shirt's size is: {shirt_size}")
    print(f"Yours shirt print is: {shirt_text}")

make_shirt()

#8.4

def make_shirt(shirt_text, shirt_size = "L"):
    print(f"Your shirt's size is: {shirt_size}")
    print(f"Yours shirt print is: {shirt_text}")

make_shirt("I love Python")

#8.5

def describe_city(city_name, country_name = "Russia"):
    print(f"{city_name} is in {country_name}.")

describe_city("Moscow")
describe_city("St.Petersburg")
describe_city("Beijing", country_name = "China")



