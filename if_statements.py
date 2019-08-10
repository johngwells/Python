cars = ['audi', 'bmw', 'subaru', 'toyota']

#equality
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#inequality
requested_topping = 'mushrooms'

if requested_topping != 'bell peppers':
    print("Hold the bell peppers")

age_0 = 19
age_1 = 22

print(age_0 >= 21 and age_1 >= 21)

# for readability
print((age_0 >= 1) and (age_1 >= 21))
print((age_0 >= 21) or (age_1 >= 21))

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

available_toppings = ['mushrooms', 'olives', 'pepporoni']

requested_toppings = ['mushrooms', 'french fries']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding ' + requested_topping + '.')
    else:
        print('Sorry, we dont have ' + requested_topping + '.')

print('\nFinish making your pizza!')

# store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
# Summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)