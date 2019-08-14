# name = input("Please enter your name: ")
# print("Hello, " + name.title() + "!")

# prompt = "If you tell me who you are, " + name.title() + \
#          " we can personalize the message you see."
# prompt += "\nWhat is your first name? "

# age = input("How old are you: ")
# age = int(age)
# age >= 18

# function
def greet_user(username):
    """Display a simple greeting"""
    print("Hello, " + username.title() + "!")
    
greet_user('jesse')

def greet_users(names):
    """Print a simple reeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)