#分别匹配生成txt文件 整段匹配
#文件格式
# ---D:\
# -------BAG
# -------------bag1
# -------------bag2
# -------.py

import os
import shutil
import math
#新生成的文件夹子的名字（怕占内存的话可能就不生成了）

class CFile(object):
    dir = ""
    file_name = ""
    full_path = ""
    score = 0

    def __init__(self, file_name, d):
        self.dir = d
        self.full_path = os.path.join(d, file_name)
        self.file_name = file_name
        if file_name.find("_")!=-1:
            self.score = int(self.get_score(file_name))
    def __str__(self):
        return self.file_name
    def get_score(self, file_name):
        # 符合要求的文件才被解析
        fs = file_name.split(".")
        ffs = fs[0].split("_")
        return ffs[-1]+fs[1]
#此处输出的是166xxxxx（没有小数点）

# 读取文件夹里的内容，文件夹里没有其它的文件，文件名要符合规范
def read_directory(d):
    files = []
    file_name_list = os.listdir(d)
    for f in file_name_list:
        c=CFile(f, d)
        if c.score:
            files.append(c)
    return files
# 对文件夹里的内容进行排序，按照时间的顺序，即文件的后缀部分

# 按照score即时间戳排序
def sort_file(files):
    return sorted(files, key=lambda file: file.score)

#少------多
# 匹配548和cam文件夹，依据548的内容来匹配cam
def match(f548, fcam):
    #d=850000000     #ars548
    #d=50000000       #arbe
    d=0
    
    res=[]
    # 548目录中的内容匹配cam中的内容，先找到全部相同的
    f548_map={}
    fcam_map={}
    #f这里便利的是ca 548是其他那些
    for f in f548:
        for ff in fcam:
            # 标记已经用过
            #f.score是cam_new_n的 ff.score是你要找的 这几个上下加减
            if f.score == ff.score-d :
                f548_map[f.file_name] = ff.file_name
                fcam_map[ff.file_name] = f.file_name
                # res.append(f) 这里只要cam文件夹的内容
                res.append(ff)
                print(f.file_name)
    # 没有精准匹配的再拿出来做匹配，双循环 在字典里面的是匹配过的
    for f in f548:
        if f.file_name in f548_map.keys():
            continue
        # 找到时间戳差值小的
        delta = 100000000000000
        cur = ''
        for ff in fcam:
            if ff.file_name not in fcam_map.keys():
                # f.score是cam_new_n的 ff.score是你要找的 这几个上下加减
                t = math.fabs((ff.score-d) - f.score)#绝对值
#           差多少时间的时候报错
#                if t>40000000:
#                    print('wrong')
                if t < delta:
                    delta = t
                    cur = ff
        print(cur.file_name)
        f548_map[f.file_name] = cur.file_name
        fcam_map[cur.file_name] = f.file_name
        # res.append(f) 这里只要cam文件夹的内容
        res.append(cur)
    return res

# 移动复制文件到新目录中去
def move_files(files, dir):
    if not os.path.exists(dir):
        os.mkdir(dir)

    if not os.path.isdir(dir):
        return

    for f in files:
        if os.path.isfile(f.full_path):
            #shutil.move(f.full_path, dir)
            shutil.copy(f.full_path, dir)
    return
#少---多(别管名字了)
def work(d548, dcam):
    filenames_548 = read_directory(d548)
    filenames_dcam = read_directory(dcam)

    #for c in filenames_548:
        #print(c.file_name)
        #print(c.score)
        #print(c.full_path)

        # ca_front_left_image_raw_1665057587.000048876.png
        # 1665057587000048876
        # ./ 1\night_sunny_normal_light_urban100601 / ca\ca_front_left_image_raw_1665057587.000048876.png



    f548 = sort_file(filenames_548)
    fcam = sort_file(filenames_dcam)
    print(type(f548))

#列表
    match_files = match(f548, fcam)
    print("total_length ", len(match_files))

# 这里修改输出的目录名字(直接输出文件夹看这里)  def move_files(files, dir)
    move_files(match_files, "{}".format(newfile))

#txt生成(生成文件夹)
    # less = d548.split('/', 6)[-1]
    # more = dcam.split('/', 6)[-1]
    #
    # file = open('select {0} for {1} in {2}.txt'.format(more,less,day),'w',encoding='utf-8')
    # for i in range(len(match_files)):
    #     file.write(str(match_files[i])+'\n')
    #
    # file.close()


#txt文件生成(不避免生成文件夹)
'''    file_path = "{}".format(new_file)
    path_list = os.listdir(file_path)

    path_name = []

    for i in path_list:
        path_name.append(i)
    path_name.sort()
    for file_name in path_name:
        with open("./txt.txt", "a") as file:
            file.write(file_name + "\n")
            print(file_name)
        file.close()
'''

#print("work over")

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    #Sensor_name=['rslidar']
    #Sensor_name=['ars548']
    Sensor_name=['arbe']
# 这里是两个目录，前一个目录作为比较的基础(少 -- 多)  ##此处需要输入
#############################################在此处写入路径#############################################################
    dirr='./TEST'
# 原始数据的存储地址
    path = r'{}'.format(dirr)
    dd=[]
    ddd=os.listdir(path)
    for dddd in ddd:
    #dd:[nighe_...01,NIGHT_...02]
        dd.append(dddd)
#p,_,_=os.walk(path)
#print(p)
    fff=[]
    for i in range(len(dd)):
        a=str(dirr+'\\'+dd[i])
        fff.append(a)
    #print(fff)
    ##['./1\\night_sunny_normal_light_urban100601', './1\\night_sunny_normal_light_urban100602']
    for i in range(len(fff)):
        #少----多(多的里面找东西和少匹)
        num=os.listdir(fff[i])      #一天的相机分完且其他打包好的返回成一个文件
        #print(num)
        for nn in num :
            if '_' in nn:
                p=nn.split('_')[2]
                q=nn.split('_')[-1]
                for s in Sensor_name:
                    newfile='{0}/{1}_new_{2}_{3}'.format(fff[i],s,p,q)
                    work('{0}/ca_new_{2}_{3}'.format(fff[i],s,p,q), "{0}/{1}".format(fff[i],s))


        # a=0
        # for nn in num:
        #     if '_' in nn:
        #         a+=1
        # print(a)
        
        # for times in range(a):
        #     for s in Sensor_name:
        #         newfile='{0}/{1}_new_{2}'.format(fff[i],s,times)
        # # 少----多(多的里面找东西和少匹)
        #         work("{0}/ca_new_{1}".format(fff[i],times), "{0}/{1}".format(fff[i],s))

