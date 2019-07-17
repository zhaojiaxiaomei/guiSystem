import sys
import operator
workers=[]


# 1.程序运行需要先读取txt文件
def read_txt():
    global workers
    file = open('workers.txt', 'r',encoding='utf-8')
    text_lines = file.readlines()
    text_lines=[i for i in text_lines if i!='\n']
    if len(text_lines)!=0:
        for line in text_lines:
            worker={}
            line=line.split(':')
            worker['name']=line[1].replace('  性别','')
            worker['sex']=line[2].replace('  出生年月','')
            worker['brithday']=line[3].replace('  工作年月','')
            worker['workday']=line[4].replace('  学历','')
            worker['xl']=line[5].replace('  职位','')
            worker['zw']=line[6].replace('  住址','')
            worker['addr']=line[7].replace('  电话','')
            worker['tel']=line[8].replace('\n','')
            workers.append(worker)
    file.close()


def text_save():
    file = open('workers.txt','w',encoding='utf-8')
    for i in workers:
        file.write('姓名:'+i['name']+'  性别:'+i['sex']+'  出生年月:'+i['brithday']+
                   '  工作年月:'+i['workday']+'  学历:'+i['xl']+'  职位:'+i['zw']+
                   '  住址:'+i['addr']+'  电话:'+i['tel']+'\n')
    file.close()


# 2.增加员工
def addworker():
    global workers
    name=input('请输入姓名：')
    sex=input('请输入性别：')
    birthday=input('请输入出生年月：')
    workday=input('请输入工作年月：')
    xl=input('输入学历：')
    zw=input('输入职位：')
    addr=input('输入住址：')
    tel=input('输入电话：')
    worker={'name':name,'sex':sex,'brithday':birthday,
            'workday':workday,'xl':xl,'zw':zw,
            'addr':addr,'tel':tel}
    workers.append(worker)
    sortWorker()
    text_save()
    print('添加成功')


# 3.删除员工
def delworker():
    global workers
    name=input('请输入要删除的员工的姓名:')
    if selectworker(name)[0]:
        workers.remove(selectworker(name)[1])
        text_save()
        print('删除成功')
    else:
        print('没有此员工')


# 3.修改员工信息
def updataworker():
    global workers
    name=input('请输入要修改的员工的姓名:')
    if selectworker(name)[0]:
        worker=selectworker(name)[1]
        workers.remove(worker)
        worker['sex'] = input('请输入性别：')
        worker['birthday'] = input('请输入出生年月：')
        worker['workday'] = input('请输入工作年月：')
        worker['xl'] = input('输入学历：')
        worker['zw'] = input('输入职位：')
        worker['addr'] = input('输入住址：')
        worker['tel'] = input('输入电话：')
        workers.append(worker)
        text_save()
        print('修改成功')
    else:
        print('没有此员工')


# 4.查询员工信息
def selectworker(name):
    flage=False
    n=0
    for worker in workers:
        if worker['name']==name:
            flage=True
            n=worker
            break
    return flage,n


# 5.排序员工信息
def sortWorker():
    global workers
    workers = sorted(workers, key=operator.itemgetter('name'))
    text_save()


if __name__ == '__main__':
    read_txt()
    flage = 'y'
    while flage == 'y':
        if len(workers)==0:
            print('现在还没有员工，请先添加员工')
            addworker()
        else:
            cz=input('请输入您要进行的操作（1.新增 2.删除 3.查询 4.修改 5.排序 6.退出）：')
            if cz=='1':
                addworker()
                flage = input("是否还要继续，是请输入'y':")
            elif cz=='2':
                delworker()
                flage = input("是否还要继续，是请输入'y':")
            elif cz=='3':
                name=input('要查询的员工姓名：')
                if selectworker(name)[0]:
                    i=selectworker(name)[1]
                    print('姓名:'+i['name']+'  性别:'+i['sex']+'  出生年月:'+i['brithday']+
                   '  工作年月:'+i['workday']+'  学历:'+i['xl']+'  职位:'+i['zw']+
                   '  住址:'+i['addr']+'  电话:'+i['tel'])
                else:
                    print('没有此员工')
                flage = input("是否还要继续，是请输入'y':")
            elif cz=='4':
                updataworker()
                flage = input("是否还要继续，是请输入'y':")
            elif cz=='5':
                sortWorker()
                for i in workers:
                    print('姓名:' + i['name'] + '  性别:' + i['sex'] + '  出生年月:' + i['brithday'] +
                          '  工作年月:' + i['workday'] + '  学历:' + i['xl'] + '  职位:' + i['zw'] +
                          '  住址:' + i['addr'] + '  电话:' + i['tel'])
                print('成功排序')
                flage = input("是否还要继续，是请输入'y':")
            else:
                sys.exit()