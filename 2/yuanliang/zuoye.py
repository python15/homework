
"""在用户管理功能中添加密码信息:
增、 改强制验证用户密码，验证通过后，提示进行的操作信息，比如：修改xxx的密码为xxxx
当使用list 和 find操作的时候，为了保护用户隐私，将用户密码替换显示成为N(密码长度)个*
使用list时，提示用户可以对列表显示的信息进行排序，排序的字段（name, age, tel）,
根据用户输入字段进行排序（升序），默认为name排序. """

message={"Jack":"25,18297042587,312512412","Tomy":"34,9673342371,31242144",
         "Lucy":"19,13678923450,3124244","Mage":"37,18958773625,4214124"}
def User_mangement():
    while True:
        key_words = input("Enter your keywords>>>").strip()
        if not key_words.isspace():
            #delete user
            if key_words == "delete":
                user_name = input("Enter username>>>")
                if user_name not in message:
                    print("User does not exist")
                else:
                    del message[user_name]
                    print("successfully deleted {}".format(user_name))

            #update and add user
            elif key_words == "update":
                information=input("Enter user_name:age:tel:password.separated by colon>>>").strip().split(":")
                user_name = information[0]
                new_value = information[1]+","+information[2]+','+information[3]
                if user_name in message:  #update
                    ps_word=input("Enter user's password>>>")
                    old_value=message[user_name].split(",")
                    if ps_word == old_value[2]:
                        message[user_name]= new_value
                        print("successfully update {}'s password is {}".format(user_name,information[3]))
                    else:
                        print("Wrong password")
                else:
                    anwser=input("User does not exist,you want add? (y/n)")
                    if anwser == "y":   #add user
                        message.update({user_name:new_value})
                        print("Add user success")
                    else:
                        pass

            #find user
            elif key_words == "find":
                user_name = input("Enter user_name>>>")
                if user_name in message:
                    value=message[user_name].split(",")
                    print("username: {}\nage: {}\ntel: {}\npassword: {} ".format(user_name,value[0],value[1],len(value[2])*'*'))
                else:
                    print("User does not exist")

            #list all user
            elif key_words == "list":
                sort_word=input("Do you want sort the information?you can enter name or age or tel")
                k_list=["user_name","age","telphone","pasword"]
                old_klist=message.keys()
                new_lst=[]

                for k in old_klist:
                    v_list = message[k].split(",")
                    d="{} {} {} {}".format(k, v_list[0], v_list[1], len(v_list[2]) * "*").split(" ")
                    new_dict=dict(zip(k_list,d))
                    new_lst.append(new_dict)

                if sort_word == "age":
                    sort_after=sorted(new_lst,key=lambda new_lst : new_lst['age'])
                elif sort_word == "tel":
                    sort_after = sorted(new_lst,key=lambda new_lst : new_lst['telphone'])
                else:
                    sort_after = sorted(new_lst, key=lambda new_lst: new_lst['user_name'])
                print("{}\t{} \t{}      \t{}".format("user_name", "age", "telphone" ,"pasword")) #print key
                for m in sort_after:   #print value
                    print("{}    \t{}    \t{}  \t{}".format(m["user_name"],m["age"], m["telphone"],len(m["pasword"]) * "*"))

            elif key_words == "exit":
                print("break")
                break
            else:
                print("Please enter correct keywords")
User_mangement()