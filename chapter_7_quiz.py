# 7-1 Rental Car
car = input("What kind of rental car would you like? ")
print("Let me see if we can find a " + car.title())

# 7-2 Restaurant Seating
group = input("\nHow many people are in your group? ")
group = int(group)

if group > 8:
    print("You'll have to wait for a table")
else:
    print("Your table is ready now")

# 7-3 Multiples of Ten
number = input("\nGive me any more you choose? ")
number = int(number)

if number % 10 == 0:
    print("Your number is a multiple of ten")
else:
    print("Your number is not a multiple of ten")