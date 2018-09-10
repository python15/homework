#!/usr/bin/env python
#-*- coding:utf-8 -*-
#global att
import hashlib
import types
user_info_box=[]
find_index={}
#menu
def show_menu(menu_action):
    if menu_action==1:
        print("="*50)
        print("this is a user managerment program.version 1.0")
        print("\t1.if you want to delete a user,please input 'delete'")
        print("\t2.if you want to update a user,please input 'update'")
        print("\t3.if you want to find a user,please input 'find'")
        print("\t3.show all,please input 'list'")
        print("\t4.add user,please input 'add'")
        print("\t5.exit,please input 'exit'")
        print("="*50)
    else:
        print("this is a user managerment program.version 1.0")
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
        if user_delete_option=="Y" or user_delete_option=="y":
            print(find_index)
            user_info_box.remove(find_index)
    else:
        print("the user doesn't exist")
#user update
def user_update():
    user_info={}
    user=[]
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
        if user_len<=3:
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
        passwd=input("please input your password:")
        passwd_lens=len(passwd)
        if 8<passwd_lens<16:
            user.append(passwd)
            passwd_control=True
        elif passwd_lens<8:
            print("passwd too short")
        elif passwd_lens>16:
            print("passwd too long")
    except:    
        print("error")
    if user_len_control and passwd_control:
        user_name=user[0]
        user_age=user[1]
        user_tel=user[2]
        user_passwd=user[3]
        if user_find(user[0]):
            user_update_option=input("the user was in system,is it update?Y/N:")
            if user_update_option=="Y" or user_update_option=="y":
                user_info_box.remove(find_index)
                user_info["name"]=user_name
                user_info["age"]=user_age
                user_info["tel"]=user_tel
                user_info["pw"]=user_passwd
                user_info_box.append(user_info)
                print("the data has been updated")
                #print("name={}age={}tel={}".format(find_index["name"],find_index["age"],find_index["tel"]))
        else:
            user_info["name"]=user_name
            user_info["age"]=user_age
            user_info["tel"]=user_tel
            user_info["pw"]=user_passwd
            user_info_box.append(user_info)
            print("user has been added")
    else:
        print("please input correct information!")
#user_find , 
def user_find(user_name):
    global find_index
    find_flag=False
    if user_name=="":
        user_name=input("input your name:")
        for user in user_info_box:
            if user_name==user["name"]:
                if find_flag:
                    print("name\tage\ttel\tpw")
                print("{}\t{}\t{}\t{}".format(user["name"],user["age"],user["tel"],md5(user["pw"])))
                find_flag=True
        else:
            if find_flag!=True:
                print(find_flag)
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
    print("name\tage\ttel\tpw")
    for user in user_info_box:
        print("{}\t{}\t{}\t{}".format(user["name"],user["age"],user["tel"],md5(user["pw"])))
def user_add():
    user_update()
def md5(pw_str):
    pw=len(pw_str)*"*"
    return pw
#main function
def user_manager():
    show_menu(1)
    while True:
        menu_input=input("option:")
        if menu_input=="delete":
            user_delete()
        elif menu_input=="update":
            user_update()
        elif menu_input=="find":
            user_find("")
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

