# Hello Admin

user_names = ['johnny', 'sarah', 'michael', 'austin', 'ben']

# user_names = [] #test no users

if user_names:
    for username in user_names:
        if username == 'johnny':
            print('Hello Admin! Would you like to see a status report')
        elif username != 'johnny':
            print('Hello ' + username + ' thanks for logging in')
        else:
            print('please register')
else:
    print('list is empty')

# Check current_users against new_users

current_users = ['Johnny', 'sarah', 'michael', 'austin', 'ben']
new_users = ['johnny', 'Sarah', 'neo', 'kate', 'gene']

current_users_lower = [x.lower() for x in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print('username already taken')
    else:
        print('username is available')

# Ordinal Numbers
ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for ordinal_number in ordinal_numbers:
    if ordinal_number == 1:
        print('1st')
    elif ordinal_number == 2:
        print('2nd')
    elif ordinal_number == 3:
        print('3rd')
    else:
        print(str(ordinal_number) + 'th')
