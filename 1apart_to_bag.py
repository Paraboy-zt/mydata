#文件摆放。应该是第一步？分成四个包？
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
import pandas as pd
import os
import shutil
###################################################在此处写入路径#################################################
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


for f in ff:
# 读取地址中的文件，以列表形式存储到files_list中
    print(f)
#f=./trytry/1
    files_list = os.listdir(f)

# 遍历列表中的所有文件
    for file in files_list:
        if '_' in file:
            name1 = file.split('_', 4)[2]+'_'+file.split('_', 4)[-1]

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
    for dirpath, dirnames, filenames in os.walk(f):
        file_count = 0
        for file in filenames:
            file_count = file_count + 1
        print(dirpath,file_count)