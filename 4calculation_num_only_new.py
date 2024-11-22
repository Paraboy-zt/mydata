#文件摆放
'''
try（D.\......）
---trytry
------1
-----------data
-------2
-----------data
------.py(文件分类+统计个数)
'''
#分成四个文件夹
import os
import shutil
import pandas as pd
import openpyxl
###################################################在此处写入路径########################################
dir='./TEST'
# 原始数据的存储地址
path = r'{}'.format(dir)

dd=[]
ddd=os.listdir(path)
for dddd in ddd:
    #dd:[1,2,3,4]
    dd.append(dddd)
#p,_,_=os.walk(path)
#print(p)

ff=[]
for i in range(len(dd)):
    a=str(dir+'\\'+dd[i])
    ##此处ff是 ./try\\1 ./try\\2
    ff.append(a)

dp=[]
fc=[]
for f in ff:
# 读取地址中的文件，以列表形式存储到files_list中
    print(f)
#f=./trytry/1
    files_list = os.listdir(f)

# 遍历列表中的所有文件
    for file in files_list:

    # 用split函数将文件的名称以‘_’切片4次，取切片后列表的第一个项，即得到了文件名的第一个数字
        name1 = file.split('_', 4)[0]

    # 如果以文件第一个数字命名的文件夹不存在，就创建一个
    # os.path.join()函数用于拼接文件路径
        if not os.path.exists(os.path.join(f, name1)):
            os.makedirs(os.path.join(f, name1))

    # 转移原始文件到新的文件夹中
        shutil.move(os.path.join(f, file), os.path.join(f, name1))
        # for i in range(len(os.path.join(f, name1))):
        #     if i == len(os.path.join(f, name1))-1:
        #         print(name1,end='')
        #         print(len(os.listdir(os.path.join(f, name1))))
#    txt = open('data statistics.txt', 'w', encoding='utf-8')

    for dirpath, dirnames, filenames in os.walk(f):
        file_count = 0
        for file in filenames:
            file_count = file_count + 1
#       txt.write(str(dirpath)+''+str(file_count) + '\n')

        print(dirpath,file_count)
        dp.append(dirpath)
        fc.append(file_count)
print(dp)
print(fc)


df=pd.DataFrame({'个数':fc},index=dp)
df.index.name='数据统计'
df.to_excel('result.xlsx',sheet_name='result')