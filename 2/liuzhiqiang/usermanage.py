import getpass
import time


SYSTEM_DESC = """
*** UserManage System **********************************************

Action Cmd:

add,    to add a user;
delete, to delete the specified user;
update, to update specified user information;
find,   to find the specified user;
list,   to display all users information;
exit,   to exit system
********************************************************************
"""

usersData = {
    'tester01': [27, 15200000009, '111111'],
    'tester02': [20, 15200000005, '222222'],
    'tester03': [29, 15200000003, '333333']
}
adminsData = {
    'admin01': 'admin01',
    'admin02': 'admin02'
}
usersform = list(usersData.keys())
adminsform = list(adminsData.keys())

def add_user(username):
    """add function, to add a userinfo"""

    if username not in usersform:
        age, contact = input("Please add the age/contact, and separated by space >>>").split()
        pwd = getpass.getpass(prompt="Please add user password >>>")
        usersData[username] = [int(age), int(contact), pwd]
        print("user added successfully.")
    else:
        print("Sorry, user %s already exists." % username)

def delete_user(username):
    """delete function, to delete the specified userinfo"""

    if username in usersform:
        usersData.pop(username, None)
    elif username in adminsform:
        adminsData.pop(username, None)
    else:
        print("Sorry, user %s already exists." % username)

def update_user(username):
    """update function, to update specified userinfo"""

    if username not in (usersform + adminsform):
        print("Sorry, user %s already exists." % username)
    elif username in usersform:
        age, contact = input("Please update the age/contact, and separated by space >>>").split()
        pwd = getpass.getpass(prompt="Please update user password >>>")
        usersData[username] = [int(age), int(contact), pwd]
    else:
        pwd = getpass.getpass(prompt="Please update user password >>>")
        adminsData[username] = pwd

def find_user(username):
    """find function, to find the specified userinfo"""

    if username in usersform:
        print("{:<15}{:<15}{:<15}{:<15}".format(username, usersData[username][0], usersData[username][1], '*'*len(usersData[username][2])))
    elif username in adminsform:
        print("{:<15}{:<15}".format(username, '*'*len(adminsData[username])))
    else:
        print("Sorry, user %s already exists." % username)

def display():
    """list function, to display all usersinfo"""
    
    key_sort = input("User information is displayed in ascending order by name/age/contact? >>>")
    if key_sort == 'age':
        users_sorted = sorted(usersData, key=lambda x:usersData[x][0])
    elif key_sort == 'contact':
        users_sorted = sorted(usersData, key=lambda x:usersData[x][1])
    else:
        users_sorted = sorted(usersData)
    
    print("{:<15}{:<10}{:<20}{:<15}".format('Username', 'Age', 'Contact', 'Password'))
    print("-"*60)
    for i in range(len(users_sorted)):
        print("{:<15}{:<10}{:<20}{:<15}".format(users_sorted[i], usersData[users_sorted[i]][0],\
                usersData[users_sorted[i]][1], '*'*len(usersData[users_sorted[i]][2])))

def admin_auth(username):
    if username not in adminsform:
        print("Sorry, user %s isn't exist." % username)
        return 0
    else:
        pwd = input('Please enter the password >>>')
        if pwd == adminsData[username]:
            return 1
        else:
            print("Verification failed, password error.")
            return 0

def user_auth(username):
    if username not in adminsform:
        print("Sorry, user %s isn't exist." % username)
        return 0
    else:
        pwd = input('Please enter the password >>>')
        if pwd == adminsData[username]:
            return 1
        else:
            print("Verification failed, password error.")
            return 0

def login(username, password):    
    if username in usersform and usersData[username][2] == password:
        print("Login successful.")
        return 1
    elif username in adminsform and adminsData[username] == password:
        print("Login successful.")
        return 1
    else:
        print("username or password error, try again.")
        return 0

def sleep_prompt(secs):
    print("Continue after %d seconds >>>" % secs, end='')
    while int(secs):
        print(".", end=' ')
        time.sleep(1)
        secs -= 1
    print()

def user_action(username):
    while True:
        sleep_prompt(3)
        print(SYSTEM_DESC)
        keyword = input('Please enter the Cmd >>>')

        if keyword == 'add':
            if username in adminsform:
                u = input("Please enter the added username.")
                add_user(u)
            else:
                print("Administrator Access, %s isn't administrator." % username)

        elif keyword == 'delete':
            if username in adminsform:
                u = input("Please enter the deleted username.")
                delete_user(u)
            else:
                print("Administrator Access, %s isn't administrator." % username)
        
        elif keyword == 'update':
            update_user(username)
        
        elif keyword == 'find':
            find_name = input("Please enter finded username >>>")
            find_user(find_name)
        
        elif keyword == 'list':
            display()
        
        elif keyword == 'exit':
            print("UserManage System exit!")
            break
        
        else:
            print("Cmd error, try again.")

if __name__ == '__main__':
    print("Welcome to the UserManage System, and login first, please.")

    while True:
        islogin = input("Do you want to log in? (Y/N) >>>").strip()
        if islogin.upper() == 'N':
            exit(0)
        else:
            login_name = input("Please enter login username >>>")
            login_pwd = getpass.getpass(prompt="Please enter the password >>>")
            login_value = login(login_name, login_pwd)

        if login_value:
            user_action(login_name)
            exit(0)

# 写和很好