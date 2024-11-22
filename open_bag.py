###已经打包好的东西 你发现错了 调整到上一步
import os
import shutil

dir='./dawn_cloudy_normal_light_tunnel100200'
# 原始数据的存储地址
path = r'{}'.format(dir)

dd=[]
ddd=os.listdir(path)
for dddd in ddd:
    dd.append(dddd)
ff=[]

for i in range(len(dd)):
    a=str(dir+'\\'+dd[i])
    ff.append(a)
print(ff)
#ff=['./bag\\bag1', './bag\\bag2']
for f in ff:
    file_list=os.listdir(f)
    fs=[]
    for m in file_list:
        if '_' in m:
            fs.append(str(f)+'\\'+str(m))
    print(fs)
    '''['./bag\\bag1\\1_0', './bag\\bag1\\1_1', './bag\\bag1\\1_2', './bag\\bag1\\2_0',
    './bag\\bag1\\2_1', './bag\\bag1\\2_2', './bag\\bag1\\3_0', './bag\\bag1\\3_1', './bag\\bag1\\3_2']'''
    for ffs in fs :
        s = os.listdir(ffs)
        #s=['arbe_new_1_0', 'ars548_new_1_0', 'ca_new_1_0', 'rslidar_new_1_0']
        print(s)
        for ss in s:
            shutil.move('{0}/{1}'.format(ffs,ss),'{0}'.format(f))
