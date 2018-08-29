#!/usr/bin/env python
#-*- coding:utf-8 -*-
#´Ë´Î×÷ÒµËùÓĞÑ§Ô±ĞèÒªĞ´×Ô¼ºµÄÑ§Ï°¼Æ»®£¬ºÍ×Ü½á´Ë²¿·Ö¿ÉÒÔµ¥¶ÀÒÔWordµÄĞÎÊ½·¢¸øÎÒ
#ÓÃ»§¹ÜÀí

user_info_box=[]
find_index={}
def show_menu(menu_action):
    if menu_action==1:
        print("="*50)
        print("this is a user managerment program.version 1.0")
        print("\t1.if you want to delete a user,please input 'delete'")
        print("\t2.if you want to update a user,please input 'update'")
        print("\t3.if you want to find a user,please input 'find'")
        print("\t3.show all,please input 'list'")
        print("\t4.exit,please input 'exit'")
        print("="*50)
    else:
        print("this is a user managerment program.version 1.0")
        print("\t1.if you want to delete a user,please input 'delete'")
        print("\t2.if you want to update a user,please input 'update'")
        print("\t3.if you want to find a user,please input 'find'")
        print("\t3.show all,please input 'list'")
        print("\t4.exit,please input 'exit'")
#Èç¹ûÊäÈë delete£¬ ÔòÈÃÓÃ»§ÊäÈë¡± ÓÃ»§Ãû¡± ¸ñÊ½×Ö·û´®£¬ ¸ù¾İÓÃ»§Ãû²éÕÒ dict ÖĞÊı¾İ£¬ Èô
#´æÔÚÊı¾İÔò½«¸ÃÊı¾İÒÆ³ı£¬ ÈôÓÃ»§Êı¾İ²»´æÔÚ£¬ ÔòÌáÊ¾²»´æÔÚ;
def user_delete():
    user=input("please input your want to delete user:")
    if user_find(user[0])>0:
        user_delete_option=input("are you sure that you want to delete?Y/N:")
        if user_delete_option=="Y":
            print(find_index)
            user_info_box.remove(find_index)
    else:
        print("the user doesn't exist")
#Èç¹ûÊäÈë update£¬ ÔòÈÃÓÃ»§ÊäÈë¡± ÓÃ»§Ãû:ÄêÁä:ÁªÏµ·½Ê½¡± ¸ñÊ½×Ö·û´®£¬ ²¢Ê¹ÓÃ:·Ö¸ôÓÃ»§
#Êı¾İ£¬ ¸ù¾İÓÃ»§Ãû²éÕÒ dcit ÖĞÊı¾İ£¬ Èô´æÔÚÊı¾İÔò½«¸ÄÊı¾İ¸üĞÂÊı¾İ£¬ ÈôÓÃ»§Êı¾İ²»´æÔÚ£¬
#ÔòÌáÊ¾²»´æÔÚ;
def user_update():
    user_info={}
    user=[]
    try:
        user=input("please input user_info format(user:age:tel):").split(":")
        user_len=len(user)
        if user_len==1:
            user.append("")
            user.append("")
        elif user_len==2:
            user.append("")
        elif user_len==3:
            pass
        else:
            user=[]
    except:    
        print("error")
    if len(user)>=1:
        if user_find(user[0])>0:
            user_update_option=input("the user was in system,is it update?Y/N:")
            if user_update_option=="Y":
                print(find_index)
                user_info_box.remove(find_index)
                user_info["name"]=user[0]
                user_info["age"]=user[1]
                user_info["tel"]=user[2]
                user_info_box.append(user_info)
        else:
            user_info["name"]=user[0]
            user_info["age"]=user[1]
            user_info["tel"]=user[2]
            user_info_box.append(user_info)
    else:
        print("please input correct information!")
#Èç¹ûÓÃ»§ÊäÈë find£¬ ÔòÈÃÓÃ»§ÊäÈë¡± ÓÃ»§Ãû¡± ¸ñÊ½×Ö·û´®£¬ ¸ù¾İÓÃ»§Ãû²éÕÒ dict ÖĞÊı¾İ°
#º¬ÊäÈë×Ö·û´®µÄÓÃ»§ĞÅÏ¢£¬ ²¢´òÓ¡;
def user_find(user_name):
    global find_index
    find_flag=0
    if user_name=="":
        user_name=input("input your name:")
        for user in user_info_box:
            if user_name==user["name"]:
                if find_flag==0:
                    print("name\tage\ttel")
                print("{}\t{}\t{}".format(user["name"],user["age"],user["tel"]))
                find_flag=1
        else:
            if find_flag==0:
                print("the user doesn't exist")
    else:
        for user in user_info_box:
            if user_name==user["name"]:
                find_index=user
                #if find_flag==0:
                #    print("name\tage\ttel")
                #print("{}\t{}\t{}".format(user["name"],user["age"],user["tel"]))
                find_flag=1
    return find_flag
#Èç¹ûÓÃ»§ÊäÈë list£¬ Ôò´òÓ¡ËùÓĞÓÃ»§ĞÅÏ¢;
#´òÓ¡ÓÃ»§µÚÒ»¸öĞĞÊı¾İÎªÓÃ»§ĞÅÏ¢ÃèÊö£¬ ´ÓµÚ¶şĞĞ¿ªÊ¼ÎªÓÃ»§Êı¾İ;
def user_list():
    print("name\tage\ttel")
    for user in user_info_box:
        print("{}\t{}\t{}".format(user["name"],user["age"],user["tel"]))
#Èç¹ûÓÃ»§ÊäÈë exit£¬ Ôò´òÓ¡ÍË³ö³ÌĞò£¬ ²¢ÍË³ö ;          
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
        elif menu_input=="exit":
            break
        else:
            print("haven't this option.")
            show_menu(2)
        print("="*50)
user_manager()
