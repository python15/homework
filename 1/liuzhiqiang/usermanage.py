usersData = {
    'tester01': [27, 15200000001],
    'tester02': [28, 15200000002],
    'tester03': [29, 15200000003]
}
usersform = usersData.keys()

SYSTEM_DESC = """
===UserManage===================================================

Action Comd:

add,    to add a user;
delete, to delete the specified user;
update, to update specified user information;
find,   to find the specified user;
list,   to display all users information;
exit,   to exit system
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""


def add_user(username, age, contact):
    """add function, to add a userinfo"""

    if username not in usersform:
        usersData[username]  = [age, contact]
        print("username '{}' add successed,username info:\n{:<15}{:<15}{:<15}".format(\
         username, username, usersData[username][0], usersData[username][1]))
    else:
        print("username '{}' already exists!\n{:<15}{:<15}{:<15}".format(username,\
         username, usersData[username][0], usersData[username][1]))

def delete_user(username):
    """delete function, to delete the specified userinfo"""

    if username in usersform:
        _ = usersData.pop(userinfo)
        print("user named '{}' had deleted!".format(username))
    else:
        print("Sorry, username '{}' does not exist!".format(username))

def update_user(username):
    """update function, to update specified userinfo"""

    if username in usersform:
        infos = input("Please enter age:contact, and separated by ':'>>>")
        if infos.count(':') == 1:
            userInfos = infos.split(':')
            usersData[username][0] = int(userInfos[0])
            usersData[username][1] = int(userInfos[1])
            print("Success! Update result：\n{:<15}{:<15}{:<15}".format(username, usersData[username][0], usersData[username][1]))
        else:
            print("Input format is incorrect, please re-enter!")
    else:
        print("Sorry, username '{}' dose not exist!".format(username))

def find_user(username):
    """find function, to find the specified userinfo"""

    if username in usersform:
        print("{:<15}{:<15}{:<15}".format(username, usersData[username][0], usersData[username][1]))
    else:
        print("Sorry, username '{}' dose not exist!".format(username))

def display():
    """list function, to display all usersinfo"""

    print("{:<15}{:<15}{:<15}".format('Username', 'Age', 'Contact'))
    print("-"*50)
    for i in usersform:
        print("{:<15}{:<15}{:<15}".format(i, usersData[i][0], usersData[i][1]))


flag = True
while flag:
    print(SYSTEM_DESC)
    keyword  = input("Please enter the Command：")

    if keyword == 'add':
        userInfo = input("Please enter username:age:contact, and separated by ':'>>>").strip().split(":")
        add_user(userInfo[0], userInfo[1], userInfo[2])
    elif keyword == 'delete':
        userinfo = input("Please enter the username which delete: ")
        delete_user(userinfo)
    elif keyword == 'update':
        userInfo = input("Please enter the username which update: ")
        update_user(userInfo)
    elif keyword == 'find':
        userInfo = input("Please enter the username which find: ")
        find_user(userInfo)
    elif keyword == 'list':
        display()
    elif keyword == 'exit':
        flag = False
        print("UserManage System exit!")
    else:
        print("Incorrect input, please re-enter!")
