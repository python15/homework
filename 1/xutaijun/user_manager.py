#!/usr/bin/env python
#-*- coding:utf-8 -*-
#�˴���ҵ����ѧԱ��Ҫд�Լ���ѧϰ�ƻ������ܽ�˲��ֿ��Ե�����Word����ʽ������
#�û�����

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
#������� delete�� �����û����롱 �û����� ��ʽ�ַ����� �����û������� dict �����ݣ� ��
#���������򽫸������Ƴ��� ���û����ݲ����ڣ� ����ʾ������;
def user_delete():
    user=input("please input your want to delete user:")
    if user_find(user[0])>0:
        user_delete_option=input("are you sure that you want to delete?Y/N:")
        if user_delete_option=="Y":
            print(find_index)
            user_info_box.remove(find_index)
    else:
        print("the user doesn't exist")
#������� update�� �����û����롱 �û���:����:��ϵ��ʽ�� ��ʽ�ַ����� ��ʹ��:�ָ��û�
#���ݣ� �����û������� dcit �����ݣ� �����������򽫸����ݸ������ݣ� ���û����ݲ����ڣ�
#����ʾ������;
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
#����û����� find�� �����û����롱 �û����� ��ʽ�ַ����� �����û������� dict �����ݰ
#�������ַ������û���Ϣ�� ����ӡ;
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
#����û����� list�� ���ӡ�����û���Ϣ;
#��ӡ�û���һ��������Ϊ�û���Ϣ������ �ӵڶ��п�ʼΪ�û�����;
def user_list():
    print("name\tage\ttel")
    for user in user_info_box:
        print("{}\t{}\t{}".format(user["name"],user["age"],user["tel"]))
#����û����� exit�� ���ӡ�˳����� ���˳� ;          
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

# 功能都做成独立的模块了，很厉害，再加个add的模块