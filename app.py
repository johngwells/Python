birth_year = input('Birth year: ')
print(type(birth_year))
age = 2019 - int(birth_year)
print(type(age))
print(age)


user_weight = input('What is your weight (lbs): ')
pounds_kilograms = int(user_weight) * 0.45
print('Your weight in kilograms is ' + str(pounds_kilograms))