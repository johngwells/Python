name = input("Please enter your name: ")
print("Hello, " + name.title() + "!")

prompt = "If you tell me who you are, " + name.title() + \
         " we can personalize the message you see."
prompt += "\nWhat is your first name? "

age = input("How old are you: ")
age = int(age)
age >= 18