for value in range(1, 6):
    print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = (list(range(2, 11, 2)))
print(even_numbers)

odd_numbers = (list(range(1, 11, 2)))
print(odd_numbers)

squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

digits = [1, 2, 3, 4, 5, 6, 7]
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value**2 for value in range(2, 11)]
print(squares)

# Try yourself - Quiz
for number in range(1, 21):
    print(number)

# million = []
# for value in range(1, 1000001):
#     print(value)

million = []
for value in range(1, 1000001):
    million.append(value)

print(min(million))
print(max(million ))
print(sum(million))

odd_numbers = []
for odd_number in range(1, 20, 2):
    odd_numbers.append(odd_number)
print(odd_numbers)

cubes = []
for cube in range(1, 11):
    cubes.append(cube**3)
print(cubes)

cubes = [cube**3 for cube in range(1, 11)]
print(cubes)
