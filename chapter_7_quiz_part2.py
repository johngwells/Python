# 7-4 Pizza Toppings
prompt = "\nWhat would you like on your pizza: "
add_to_pizza = "\nWe'll add that to your pizza!"

active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
        break
    else:
        print(add_to_pizza)

# 7-5 Movie Tickets
prompt = "what is your age: "
active = True
while active:
    age = int(input(prompt))

    if age <= 3:
        print("Your ticket is free")
    elif age > 3 and age <= 12:
        print("Your ticket is $10")
    else:
        print("Your ticket is $15")