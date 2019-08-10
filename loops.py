magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show")

pizzas = ['supreme', 'new york', 'deep dish']
for pizza in pizzas:
    print('I like ' + pizza + ' pizza')

print("I really Like pizza, I could eat all " + str(len(pizzas)))

friends_pizzas = pizzas[:]

pizzas.append('chicago')
friends_pizzas.append('pineapple')
print(pizzas)
print(friends_pizzas)

print('\nThese are my favorite')
for pizza in pizzas:
    print(pizza)

print("\nFriends favorite are:")
for pizza in friends_pizzas:
    print(pizza)

