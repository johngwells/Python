players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

# Looping through a slice

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# Copying a list
my_foods = ['carrots', 'bananas', 'pickles']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friends favorite foods are:")
print(friend_foods)

my_foods.append('celery')
friend_foods.append('ice cream')

print(my_foods)
print(friend_foods)

print("The first 3 items are " + str(players[:3]))
for player in players[:3]:
    print("The first 3 players are " + player)
