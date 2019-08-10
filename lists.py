bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())
print(bicycles[-1])
message = "My first bicycle was a " + bicycles[0].title() + "."

print(message)
bicycles[0] = 'stolen'
print(bicycles)
bicycles.append('Odyssey')
print(bicycles)
bicycles.insert(0, 'GT')
print(bicycles)
del bicycles[0]
print(bicycles)
popped_bicycle = bicycles.pop()
print(bicycles)
print(popped_bicycle)
last_owned = bicycles.pop()
print("The last bicycle I owned was a " + last_owned.title() + ".")
too_ugly = 'cannondale'
bicycles.remove(too_ugly)
print(bicycles)
print("\nA " + too_ugly.title() + " is too ugly for me")

guest_list = ['bob', 'joe', 'billy']
print("Would you like to hang out " + guest_list[0].title() + "!")
print("Would you like to hang out " + guest_list[1].title() + "!")
print("Would you like to hang out " + guest_list[2].title() + "!")
guest_removed = guest_list.pop(0)
print(guest_removed.title() + " Cant make it to the hangout")
guest_list.append("sarah")
print("Would you like to hang out " + guest_list[0].title() + "!")
print("Would you like to hang out " + guest_list[1].title() + "!")
print("Would you like to hang out " + guest_list[2].title() + "!")
print("\nWe found a bigger table!")
guest_list.insert(0, 'gemma')
guest_list.insert(3, 'katie')
guest_list.append('disco bunny')
print("Everyone please show up tonight" + str(guest_list))
guest_removed = guest_list.pop(1)
print("Sorry " + guest_removed +
      " you didn't make the cut no room for you buddy")
print(guest_list)
guest_removed = guest_list.pop(1)
print("Sorry " + guest_removed +
      " you didn't make the cut no room for you buddy")

# Organizing a list

print("The total guest coming to the party is " + str(len(guest_list)))

