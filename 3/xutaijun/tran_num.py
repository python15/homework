nums = ['零','壹','贰','叁','肆','伍','陆','柒','捌','玖']
small_int_label = ['', '拾', '佰', '仟','万']
small_int_part=input("please input your number:")
c=small_int_part[::-1]
a=zip(small_int_label,c)
temp=''.join([(x if y!='0' else '')+nums[int(y)] for x,y in a])[::-1]
tmp=temp.replace('零零零','零').replace('零零','零').rstrip('零').lstrip('零')
res=[]
res.append(tmp)
res.append('圆')
print(''.join(res))
#先提交作业，过后再改为函数的
#作业逻辑 将单位和值打包成元组 ，通过列表解析给值附加单位，为零的不加单位
#替换可能出现三个零或者两个零为一个零，去掉中文左右的零
#最后加上圆，生成新的列表，完成阿拉伯数字转换
