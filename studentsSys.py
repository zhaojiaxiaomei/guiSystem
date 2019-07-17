import sys


def addStu(stuList):
    stu={}
    id = input('请输入学号：')
    name = input('请输入姓名：')
    mobile = input('请输入电话：')
    if len(stuList)==0:
        stu['id'] = id
    else:
        for stu in stuList:
            if stu['id']==id:
                print('系统中已经存在改学生')
            else:
                stu['id']=id
    stu['name']=name
    stu['mobile'] = mobile
    stuList.append(stu)
    print('添加成功！')
    return stuList


def selectStu(stuList,xh):
    if xh=='1':
        flage=0
        s = input('请输入要查询的学号：')
        for stu in stuList:
            if stu['id']==s:
                flage=1
                print(stu)
        if flage==0:
            print('找不到该学号学生')
    elif xh=='2':
        flage = 0
        s = input('请输入要查询学生的姓名：')
        for stu in stuList:
            if stu['name'] == s:
                flage = 1
                print(stu)
        if flage == 0:
            print('找不到该姓名学生')
    else:
        flage = 0
        s = input('请输入要查询学生的电话：')
        for stu in stuList:
            if stu['mobile'] == s:
                flage = 1
                print(stu)
        if flage == 0:
            print('找不到该电话学生')
    return stuList


def deleteStu(stuList):
    flage = 0
    s = input('请输入要删除的学生的姓名：')
    for stu in stuList:
        if stu['name'] == s:
            flage = 1
            stuList.remove(stu)
            print('删除成功')
    if flage == 0:
        print('找不到该姓名学生')
    return stuList


def updateStu(stuList):
    flage = 0
    id=input('请输入要修改学生的学号：')
    for stu in stuList:
        if stu['id'] == id:
            flage = 1
            mobile=input('请输入修改后的手机号：')
            stu['mobile']=mobile
    if flage == 0:
        print('找不到该姓名学生')
    return stuList


if __name__ == '__main__':
    stuList=[]
    flage='y'
    while flage=='y':
        if len(stuList)==0:
            print('当前还没有学生，请添加学生')
            stuList=addStu(stuList)
        else:
            s=input('请选择你操作1.添加 2.删除 3.查找 4.修改 5打印全部学生 输入其他字符退出程序')
            if s=='1':
                stuList=addStu(stuList)
                flage=input("是否还要继续，是请输入'y':")
            elif s=='2':
                stuList=deleteStu(stuList)
                flage = input("是否还要继续，是请输入'y':")
            elif s=='3':
                xh=input('通过什么方式查找1.学号 2.姓名 3.电话 输入其他字符退出程序')
                stuList=selectStu(stuList,xh)
                flage = input("是否还要继续，是请输入'y':")
            elif s=='4':
                print('注请输入学号并并修改手机号！')
                stuList=updateStu(stuList)
                flage = input("是否还要继续，是请输入'y':")
            elif s=='5':
                print(stuList)
            else:
                sys.exit()