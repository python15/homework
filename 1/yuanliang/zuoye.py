message={"Jack":"25,18297042587","Tom":"34,96732371","Lucy":"19,13678923450","Mage":"37,18958773625"}


def delete():
    user_name = input("Enter username>>>")
    if user_name not in message:
        print("User does not exist")
    else:
        del message[user_name]
        print("successfully deleted {}".format(user_name))

def update():
    information = input("Enter user_name:age:tel.separated by colon>>>").strip().split(":")
    user_name = information[0]
    if user_name in message:
        message[user_name] = information[1] + "," + information[2]
        print("successfully update {}".format(user_name))
    else:
        print("User does not exist")

def list():
    print("{} {} {}".format("user_name", "age", "telphone"))
    for k, v in message.items():
        print(k, v)

def find():
    user_name = input("Enter user_name>>>")
    if user_name in message:
        print("username: {}\nage & tel：{}".format(user_name, message[user_name]))
    else:
        print("User does not exist")

def User_mangement():
    while True:
        key_words = input("Enter your keywords>>>").strip()
        if not key_words.isspace():
            if key_words == "delete":
                delete()
            elif key_words == "update":
                update()
            elif key_words == "find":
                find()
            elif key_words == "list":
                list()
            elif key_words == "exit":
                print("break")
                break
            else:
                print("Please enter true keywords")
User_mangement()

# 抽成独立的函数，会不会好点？
