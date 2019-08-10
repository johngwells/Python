# 6-7
# make a list of 3 dictionaries in a list
people = []

person = {
    'name': 'sarah',
    'age': 21,
    'city': 'las vegas',
    }
people.append(person)

person = {
    'name': 'johnny',
    'age': 37,
    'city': 'san francisco',
    }
people.append(person)

person = {
    'name': 'misu',
    'age': 7,
    'city': 'san francisco',
    }
people.append(person)

# loop through the list of people & print everything you know about them

for person in people:
    name = person['name'].title()
    age = str(person['age'])
    city = person['city'].title()
    print("\n" + name + " is " + age + " years old " + "and lives in " + city)

# 6-8
pets = []

misu = {
    'type': 'dog',
    'owner': 'johnny',
    }
pets.append(misu)

rocko = {
    'type': 'dog',
    'owner': 'gambit',
    }
pets.append(rocko)

psycha = {
    'type': 'cat',
    'owner': 'justin',
    }
pets.append(psycha)

kyle = {
    'type': 'cat',
    'owner': 'danielle',
    }
pets.append(kyle)

spock = {
    'type': 'bird',
    'owner': 'scotie',
    }
pets.append(spock)

print(pets)

for pet in pets:
    type = pet['type']
    owner = pet['owner']
    print("\n" + owner + " owns a " + type)

# 6-10
favorite_numbers = {
    'sarah': [1],
    'ben': [5, 9, 2],
    'austin': [3],
    'thanh': [1, 7],
    'misu': [9, 99, 999],
}
for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + "'s favorite numbers are:")
    for number in numbers:
        print(" " + str(number))

# 6-11
cities = {
    'san francisco': {
        'country': 'usa',
        'population': 1000000,
        'fact': 'its fun',
    },
    'los angeles': {
        'country': 'usa',
        'population': 10101010,
    },
    'portland': {
        'country': 'usa',
        'population': 500000,
    },
}

for key, city in cities.items():
    print("\nFacts about " + key.title())
    print("\t is in the " + city['country'] + " with a population of " +
        str(city['population']) + ".")
