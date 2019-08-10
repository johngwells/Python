alien_color = 'yellow'

if alien_color == 'green':
    print('You earn 5 points for shooting the alien')
elif alien_color == 'yellow':
    print('You earn 7 point')
elif alien_color == 'red':
    print('You earn 9 points')
else:
    print('You earn 15 points for shooting a ufo')

# A Simple Dictionary
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# starting from an empty dictionary
alien_1 = {}

alien_1['color'] = 'purple'
alien_1['points'] = 7

print(alien_1)

alien_1 = {'color': 'blue'}
print("The alien changed to " + alien_1['color'] + ".")

# track the speed of the alien
alien_1['speed'] = 'medium'
alien_1['x_position'] = 0
alien_1['y_position'] = 24
print(alien_1)

if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

# new position is the old position plus the increment
alien_1['x_position'] = alien_1['x_position'] + x_increment

print("New x-position: " + str(alien_1['x_position']))

# Removing key value pairs
del alien_0['points']
print(alien_0)

# alien.py

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# make a list for storing aliens
aliens = []

# make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created
print("Total number of aliens: " + str(len(aliens)))

# as the game progresses, the aliens change color an speed
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15