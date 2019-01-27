#third homework:���밢��������
num=(input("give me a four-number please:"))
data={"0":"��","1":"Ҽ","2":"��","3":"��","4":"��","5":"��","6":"½","7":"��","8":"��","9":"��"}
lstt=[]#���ж�����
lst=[]#������ʵ����
#�����ֳ��ַ�д���б�
for i in str(num):
    lstt.append(i)

#������Ϊ0�����
while lstt[0]=="0":
    lenth=len(lstt)
    if lenth>1:
        lstt.pop(0)
    else:
        break
    


#���������б��γɣ���ʼ���� 

lst=lstt
lenth=len(lst)

#��λ
if lenth<2:
    print(data[lst[0]]+" "+"Ԫ")

#��λ��
elif lenth<3:
    if lst[1]=="0":
        print(data[lst[0]]+"ʮ"+" "+"Ԫ")
    else:
        print(data[lst[0]]+"ʮ"+data[lst[1]]+" "+"Ԫ")

#��λ��
elif lenth<4:
    if lst[1]=="0":
        if lst[2]=="0":
            print(data[lst[0]]+"��"+" "+"Ԫ")
        else:
            print(data[lst[0]]+"����"+data[lst[2]]+" "+"Ԫ")
    elif lst[2]=="0":
        print(data[lst[0]]+"��"+data[lst[1]]+"ʮ"+" "+"Ԫ")
    else:
        print(data[lst[0]]+"��"+data[lst[1]]+"ʮ"+data[lst[2]]+" "+"Ԫ")
#��λ��
else:
    if lst[1]=="0":
        if lst[2]=="0":
            if lst[3]=="0":
                print(data[lst[0]]+"Ǫ"+" "+"Ԫ")
            else:
                print(data[lst[0]]+"Ǫ��"+data[lst[3]]+" "+"Ԫ")
        elif lst[3]=="0":
            print(data[lst[0]]+"Ǫ��"+data[lst[2]]+"ʮ"+" "+"Ԫ")
        else:
            print(data[lst[0]]+"Ǫ��"+data[lst[2]]+"ʮ"+data[lst[3]]+" "+"Ԫ")
    elif lst[2]=="0":
        if lst[3]=="0":
            print(data[lst[0]]+"Ǫ"+data[lst[1]]+"��"+" "+"Ԫ")
        else:
            print(data[lst[0]]+"Ǫ"+data[lst[1]]+"����"+data[lst[3]]+" "+"Ԫ")
    else:
        if lst[3]=="0":
            print(data[lst[0]]+"Ǫ"+data[lst[1]]+"��"+data[lst[2]]+"ʮ"+" "+"Ԫ")
        else:
            print(data[lst[0]]+"Ǫ"+data[lst[1]]+"��"+data[lst[2]]+"ʮ"+data[lst[3]]+" "+"Ԫ")


# 我这边看到的是乱码，可以的话 私聊我下