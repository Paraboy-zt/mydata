#--file
#--------1
#------------night_..._1001(already devide in to 4 files)  这1001里面已经有4个分好的包了
#--------2
#------------night_..._1002(already devide in to 4 files)
#--------apart_ca
#
#camrea分成了按照规则分成了100多个包，那三个还没分😀
#
#将ca按照20s(203帧)来拆分
import os
import shutil
import pandas as pd
import openpyxl 
#   每一帧数据   ca_front_left_image_raw_1665057720.800077677.png  ###


### CF这个方法可以返回 时间戳 1665057720  ###
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
# 这里 返回的是 ca_front_left_image_raw_1665057720.800077677.png 等一系列的东西 ，score是时间戳 c.score返回的是1665057200800077677
# ca的内容按照时间戳排序
def sort_file(files):
    return sorted(files, key=lambda file: file.score)
#生成若干个文档(筛选)
def apart(ca_time):
    #此处设置相机多少秒 开始条秒
    delta = 700000000
    #ca_time 是一个文件名排序好了的列表 .score可以导出来时间戳 还可以.file_name dir+file_name=fullname
    #列表套列表？
    res = []
    for i in range(len(ca_time)-1):
        if int(ca_time[i+1].score)-int(ca_time[i].score) > delta :
            ###此处是因为相机  间隔多长时间 会有一个大跳 （不连续）
            res.append(i+1)
            #res.append(i-1)
            #res.append(i+1)
    return res #[102, 305, 508, 711, 914, 1117] 返回这个东西
#res分割的时间点 看分出来的不对就用 i-1 或者 i+1


def work(dd):
    ca = read_directory(dd)
    ca_time = sort_file(ca)
    # for c in ca_time:
    #     print(c.file_name)
    #     print(c.score)
    #     print(c.full_path)
    #  print(*ca_time[:20])
    #  ca_front_left_image_raw_1665057587.000048876.png 输出格式（列表取其一）
    #  1665057587000048876  输出格式（列表取其一）
    #  ./ 1\night_sunny_normal_light_urban100601 / ca\ca_front_left_image_raw_1665057587.000048876.png 输出格式（列表取其一）
    #  ca_time 是一个以文件名排序好了的列表
    #  此处返回的是第项目开始切   eg：[102, 305, 508, 711, 914, 1117]
    apart_files_num = apart(ca_time)
    # n=len(apart_files_num)
    # n+=1
    #在列表0处插入
    apart_files_num.insert(0, 0)
    #在列表末尾插入
    #晚些时候用新的测试一下这个
    # 插入0和一共有多少元素的末尾项
    apart_files_num.append(int(len(ca)))
    # 输出结果为 [0, 102, 305, 508, 711, 914, 1117, 1300]
    #apart_files_num.insert(-1, int(len(ca)))
    #输出结果为[0, 102, 305, 508, 711, 914, 1300, 1117]
    #在实验代码例


    #m 123 循环  被整除 以ca为依据先分成三个包   取余3为012 分到不同的 三个包
    for m in range(3):
        for i in range (len(apart_files_num)-1) :
            if not os.path.exists('{0}/ca_new_{1}_{2}'.format(fff[j],i,m)):#如果路径不存在
        # fff = ['./1\\night_sunny_normal_light_urban100601', './1\\night_sunny_normal_light_urban100602']
                os.makedirs('{0}/ca_new_{1}_{2}'.format(fff[j],i,m), exist_ok=True)

            for file in ca_time[apart_files_num[i]:apart_files_num[i+1]]:
                ###切片后小区间的index### 假如说102切片 那102对应的编号就是0
                if ca_time[apart_files_num[i]:apart_files_num[i+1]].index(file) % 3 == m :
                    shutil.move('{}'.format(file.full_path), '{0}/ca_new_{1}_{2}'.format(fff[j],i,m))
                    ### file 给一个方法
                    ### 我之前的代码咋写的这么厉害呢？
            #shutil.move('{}'.format(file.full_path), '{0}/ca_new_{1}'.format(fff[j],i))

            print("==================")
    #  print(apart_files_num)
        print('===')

    #  实现len(insert之前的apart_files_num)个的文件夹，将每组分派到各个文件夹里


if __name__ == '__main__':
    ################################在此处写入路径#################################################
    dirr = './TEST'

    # 原始数据的存储地址
    path = r'{}'.format(dirr)
    dd = []
    ddd = os.listdir(path)
    for dddd in ddd:
        # dd:[nighe_...01,NIGHT_...02]
        dd.append(dddd)
    # p,_,_=os.walk(path)
    # print(p)
    fff = []
    for i in range(len(dd)):
        a = str(dirr + '\\' + dd[i])
        ##fff =['./1\\night_sunny_normal_light_urban100601', './1\\night_sunny_normal_light_urban100602']
        fff.append(a)
    print(fff)
    for j in range(len(fff)):
        work('{}/ca'.format(fff[j]))