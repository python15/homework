
# coding: utf-8

# In[3]:


#User information management program
#用户管理
#如果输入 delete， 则让用户输入” 用户名” 格式字符串， 根据用户名查找 dict 中数据， 若
#存在数据则将该数据移除， 若用户数据不存在， 则提示不存在;
#如果输入 update， 则让用户输入” 用户名:年龄:联系方式” 格式字符串， 并使用:分隔用户
#数据， 根据用户名查找 dict 中数据， 若存在数据则将改数据更新数据， 若用户数据不存在，
#则提示不存在;
#如果用户输入 find， 则让用户输入” 用户名” 格式字符串， 根据用户名查找 dict 中数据包
#含输入字符串的用户信息， 并打印;
#如果用户输入 list， 则打印所有用户信息;
#打印用户第一个行数据为用户信息描述， 从第二行开始为用户数据;
#如果用户输入 exit， 则打印退出程序， 并退出 ;   


# In[29]:


print('User Information Management Program Instructions')
print('Please use the following commands to manipulate the program')
print('find: Enter a Name to look up information')
print('update: Add a new User to the program ')
print('delete: Remove a User in the program which has already existed')
print('list: Present all the User information')
print('exit: Exit the program')


# In[30]:


#Default dictionary
Dic_0={'Name':[],'Age':[],'Contact':[]}


# In[5]:


#function1 Update user infomation


# In[9]:


def Upd(Dic):
    print('Please enter User Information in the following order:')
    print('Name:Age:Contact')
    User_info=input()
    InfoList=User_info.split(':')
    Dic['Name'].append(InfoList[0])
    Dic['Age'].append(InfoList[1])
    Dic['Contact'].append(InfoList[2])
    print('Done!')
    #print(Dic_0) funtion test


# In[ ]:


#function2 find info


# In[13]:


def find(Dic):
    print('Please enter a Name:')
    UserName=input()
    if UserName in Dic_0['Name']:
        Pn=Dic['Name'].index(UserName)
        print('Name:',Dic['Name'][Pn])
        print('Age:',Dic['Age'][Pn])
        print('Contact:',Dic['Contact'][Pn])
    else:
        print(UserName,"is not found!")


# In[17]:


#function3 Delete info


# In[18]:


def Dele(Dic):
    print('Please enter a Name:')
    UserName=input()
    if UserName in Dic_0['Name']:
        Pn=Dic_0['Name'].index(UserName)
        del Dic_0['Name'][Pn]
        del Dic_0['Age'][Pn]
        del Dic_0['Contact'][Pn]
    else:
        print(UserName,"is not found!")


# In[19]:


#function4 List all the info


# In[20]:


def List(Dic):
    print('----------------------------') #我是分隔符
    for index in range(len(Dic['Name'])):
        print('Name:',Dic['Name'][index])
        print('Age:',Dic['Age'][index])
        print('Contact:',Dic['Contact'][index])
        print('----------------------------') #我是分隔符


# In[26]:


#function5 User's command lines


# In[28]:


print('Please enter your command')
loop =1 # loop index
while loop == 1: #loop before Exit
    cmd=input()
    if cmd == 'list':
        List(Dic_0)
    elif cmd =='update':
        Upd(Dic_0)
    elif cmd == 'find':
        find(Dic_0)
    elif cmd == 'delete':
        Dele(Dic_0)
    elif cmd == 'exit':
        print('Exit Program!')
        break

