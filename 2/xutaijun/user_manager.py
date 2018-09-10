#!/usr/bin/env python
#-*- coding:utf-8 -*-
#global att
import hashlib
import types
user_info_box=[{'name':'admin','age':'18','tel':'1818059xxxx','pw':'admin'}]
find_index={}
#menu
def show_menu(menu_action):
    if menu_action==1:
        print("="*50)
        print("this is a user managerment program.version 2.0")
        print("\t1.if you want to delete a user,please input 'delete'")
        print("\t2.if you want to update a user,please input 'update'")
        print("\t3.if you want to find a user,please input 'find'")
        print("\t3.show all,please input 'list'")
        print("\t4.add user,please input 'add'")
        print("\t5.exit,please input 'exit'")
        print("="*50)
    else:
        print("this is a user managerment program.version 2.0")
        print("\t1.if you want to delete a user,please input 'delete'")
        print("\t2.if you want to update a user,please input 'update'")
        print("\t3.if you want to find a user,please input 'find'")
        print("\t3.show all,please input 'list'")
        print("\t4.add user,please input 'add'")
        print("\t5.exit,please input 'exit'")
def user_delete():
    user=input("please input your want to delete user:")
    if user_find(user[0]):
        user_delete_option=input("are you sure that you want to delete?Y/N:")
        user_info_index=user_info_box.index(find_flag)
        if user_delete_option=="Y" or user_delete_option=="y":
            user_passwd=input("please input user password:")
            if user_info_box[user_info_index]['pw']==user_passwd:
                user_info_box.remove(find_index)
                print("has been deleted")
    else:
        print("the user doesn't exist")
#user update
def user_update():
    global user_info_box
    user_info={}#svae key -value user info.
    user_name=""
    user_age=0
    user_tel=0
    user_passwd=""
    user=str(input("please input user name:"))
    if user_find(user):
        user_update_option=input("the user was in system,is it update?Y/N:")
        if user_update_option=="Y" or user_update_option=="y":
            user_passwd=input("please input user passwd:")
            if user_passwd==find_index["pw"]:
                user_info_index=user_info_box.index(find_index)
                update_options=input("please input your option(Info/Passwd)I/P:")
                if update_options=="I" or update_options=="i":
                    user_age=input("please input user age:")
                    user_tel=input("please input user tel:")
                    user_info_box[user_info_index]['age']=user_age
                    user_info_box[user_info_index]['tel']=user_age
                    print("the data has been updated")
                elif update_options=="P" or update_options=="p":
                    user_passwd=input("please input new password:")
                    user_info_box[user_info_index]['pw']=user_passwd
                    print("the data has been updated")
                else:
                    print("not this option")
            else:
                print("password verify error")
        #print("name={}age={}tel={}".format(find_index["name"],find_index["age"],find_index["tel"]))
    else:
        print("user has been exists or your input user is null")
#user_find , 
def user_find(user_name="default"):
    global find_index
    find_flag=False
    if user_name=="default":
        user_name=input("please input your name:")
        for user in user_info_box:
            if user_name==user["name"]:
                if find_flag:
                    print("name\tage\ttel\tpw")
                print("{}\t{}\t{}\t{}".format(user["name"],user["age"],user["tel"],md5(user["pw"])))
                find_flag=True
        else:
            if find_flag!=True:
                print("the user doesn't exist")
    else:
        for user in user_info_box:
            if user_name==user["name"]:
                find_index=user
                #if find_flag==0:
                #    print("name\tage\ttel")
                #print("{}\t{}\t{}".format(user["name"],user["age"],user["tel"]))
                find_flag=True
    return find_flag
#show all
def user_list():
    try:
        sort_input=input("How do you want to display the list(defalut sort by username)N(username)/A(Age)/T(Tel):")
        if sort_input=="N" or sort_input=="n" or sort_input=="":
            user_info_box.sort(key=lambda x:x['name'])
            print("name\tage\ttel\tpw")
            for user in user_info_box:
                print("{}\t{}\t{}\t{}".format(user["name"],user["age"],user["tel"],md5(user["pw"])))
        elif sort_input=="A" or sort_input=="a":
            user_info_box.sort(key=lambda x:x['age'])
            print("name\tage\ttel\tpw")
            for user in user_info_box:
                print("{}\t{}\t{}\t{}".format(user["name"],user["age"],user["tel"],md5(user["pw"])))
        elif sort_input=="T" or sort_input=="t":
            user_info_box.sort(key=lambda x:x['tel'])
            print("name\tage\ttel\tpw")
            for user in user_info_box:
                print("{}\t{}\t{}\t{}".format(user["name"],user["age"],user["tel"],md5(user["pw"])))
        else:
            print("have not this option!")
    except:
        print("++++++++++++++++++++++")
def user_add():
    user_info={}#svae key -value user info.
    user=[]#save user input login info
    user_len_control=True
    user_len=0
    user_name=""
    user_age=0
    user_tel=0
    user_password=""
    passwd_control=False
    '''user information'''
    try:
        '''user control'''
        user=input("please input user_info format(user:age:tel):").split(":")
        user_len=len(user)
        if user_len<=3 and user[0]!="":
            if user_len==1:
               user.append("")
               user.append("")
            elif user_len==2:
                user.append("")
            elif user_len==3:
                user_len_control=True
        else:
            user_len_control=False
        '''password control'''
        if user[0]!="":
            user_find_control=user_find(user[0])
            if not user_find_control and user_len_control:
                passwd=input("please input your password:")
                passwd2=input("please verify your password:")
                if passwd == passwd2:
                    passwd_control=passwd_len_verify(passwd)
                    if passwd_control:
                        user.append(passwd)
                else:
                    print("the password not same")
            else:
                print("user exists")
        else:
            print("user is null")
    except:    
        print(passwd_control,user_find_control,user_len_control)
    if user_len_control and passwd_control and not user_find_control:
        user_name=user[0]
        user_age=user[1]
        user_tel=user[2]
        user_passwd=user[3]
        user_info["name"]=user_name
        user_info["age"]=user_age
        user_info["tel"]=user_tel
        user_info["pw"]=user_passwd
        user_info_box.append(user_info)
        print("user has been added")
    else:
        print("please input correct information!")
def passwd_len_verify(user_passwd):
    passwd_control=False
    passwd_lens=len(user_passwd)
    if 8<=passwd_lens<16:
        passwd_control=True
    elif passwd_lens<8:
        print("passwd too short")
    elif passwd_lens>16:
        print("passwd too long")
    return passwd_control 
def md5(pw_str):
    pw=len(pw_str)*"*"
    return pw
#main function
def user_manager():
    show_menu(1)
    while True:
        menu_input=input("option>>>")
        if menu_input=="delete":
            user_delete()
        elif menu_input=="update":
            user_update()
        elif menu_input=="find":
            user_find("default")
        elif menu_input=="list":
            user_list()
        elif menu_input=="add":
            user_add()
        elif menu_input=="exit":
            break
        else:
            print("haven't this option.")
            show_menu(2)
        print("="*50)
if __name__=="__main__":
    user_manager()

