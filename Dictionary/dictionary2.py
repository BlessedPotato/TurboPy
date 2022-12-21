# dictionary2
# 6.4
py_glossarium = {'list': "\nPython's list is awesome thing, it's like a freaking box for every kind of data. You can "
                         "add and delete random stuff to/from that box LUL",
                 'function': "\nAwesome sht, you can tell Python what to do. It's an instruction with compilation of"
                             "certain actions. Very useful.",
                 'string': "\nAnother data type. it's used to print this text, so, it's like an average text, like in"
                           "your notebook LUL",
                 'float': "\nData type, which is a number with floating point LUL",
                 'dictionary': "Another box, but with keys and values. You can imagine it like a bookshelf"
                 }

print('\n')

List = (py_glossarium['list'])
Function = (py_glossarium['function'])
Float = (py_glossarium['float'])

print('\n')

for key, value in py_glossarium.items():
    print("\n")
    print(f"What is {key} in Python?")
    print(f"The answer is: {value}")


# 6.5

rivers = {
    'nile': "egypt",
    'volga': "russia",
    'mississippi': "u.s.a"
}
print("\n")

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

print('\n')

for river in rivers.keys():
    print(f"The {river.title()} is big!")

print('\n')

for country in rivers.values():
    print(f"The {country.title} is big country!")

print('\n')

fav_languages = {
    'jen': "python",
    'sarah': "c",
    'edward': "ruby",
    'phil': "python"
}

fav_languages_new = {
    'jen': "python",
    'sarah': "c",
    'edward': "ruby",
    'phil': "python",
    'max': "python",
    'evelyn': "C#",
    'noah': "java",
    'mary': "pascal"
}


for name, language in fav_languages_new.items():
    print(f"I like {language.title()} too!")

    if name in fav_languages:
        print(f"Thank you for your participation in our survey, {name.title()}!")


# Zaeboba, Maxon, well done!




import this


