
favorite_languages_1 = {
    'jen': ['python', 'ruby'],
    'sarah' : 'c',
    'edward' : ['ruby', 'go'],
    'phil' : ['python', 'haskell'],
    }

for name, languages in favorite_languages_1.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

favorite_languages = {
    'jen': 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    }

print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      ".")

# see who took the poll. Key value loop. * .keys returns the keys
for name in favorite_languages.keys():
    print(name.title())

friends = ['sarah', 'phil']
for name in sorted(favorite_languages.keys()):
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() + ", your favorite language is " +
              favorite_languages[name].title() + "!")
    if 'erin' not in favorite_languages.keys():
        print("Erin, please take our poll!")

print("\nThe following languages have been mentioned:")
for language in set(sorted(favorite_languages.values())):
    print(language.title())

person_i_know = {
    'name' : 'sarah',
    'age' : 21,
    'city' : 'las vegas',
}

# Quiz 1
print(person_i_know['name'].title() + ' who is ' + str(person_i_know['age']) +
      ' lives in ' + person_i_know['city'].title() + ".")

# Quiz 2
favorite_numbers = {
    'sarah': 1,
    'ben': 5,
    'austin': 3,
    'thanh': 7,
    'misu': 9,
}

for favorite_number in favorite_numbers:
    print(favorite_number.title() +
          "'s favorite number is "  +
          str(favorite_numbers[favorite_number]))

# Quiz 3
programming_glossaries = {
    'for loop': 'an iteration over data',
    'if, elif and else': 'a true or false conditional',
    '{}': 'a dictionary to store key value pairs',
    '()': 'a tuple which is immutable',
    '[]': 'a list',
}

for programming_glossary in programming_glossaries:
    print(programming_glossary + " means: " +
          programming_glossaries[programming_glossary] + '\n')

# key value loop * .items returns key value pairs
for question, answer in programming_glossaries.items():
    print(question + ' means: ' + answer)