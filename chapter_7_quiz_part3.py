# 7-8 & 7-9
sandwich_orders = ['tuna', 'pastrami', 'coldcut', 'salami', 'pastrami', 'meatball', 'pastrami',]
finished_sandwiches = []
# Out of pastrami
print("The deli has ran out of pastrami, sorry. . .")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    
    print("\nYour " + current_sandwich + " sandwich is ready!")
    finished_sandwiches.append(current_sandwich)

print("\nSandwiches that have been made are: ")
for finished_sandwich in finished_sandwiches:
    print("\t" + finished_sandwich)
