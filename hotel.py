import sys


def addPass(Passengers,num):
    name=input('请输入旅客姓名：')
    data=input('请输入入住时间：')
    Id=input('请输入旅客身份证：')
    for i in range(len(num)):
        if num[i][1]==0:
            num[i][1]=1
            room=num[i][0]
            break
    passer={'name':name,'data':data,'Id':Id,'room':room}
    Passengers.append(passer)
    print(name+'成功入住本旅店'+room)
    return Passengers,num


def deletePass(Passengers,sNum,dNum):
    xm = input('请输入退房人的姓名：')
    n = 0
    for i in Passengers:
        if i['name'] == xm:
            n = 1
            if '单' in i['room']:
                for j in range(len(dNum)):
                    if dNum[j][0] == i['room']:
                        dNum[j][1] = 0
                        break
            else:
                for j in range(len(sNum)):
                    if sNum[j][0] == i['room']:
                        sNum[j][1] = 0
                        break
            Passengers.remove(i)
            print(i['name'] + '退房成功')
    if n == 0:
        print('没有此姓名的用户入住本酒店')
    return Passengers,dNum,sNum


def outfiles(Passengers):
    outfile = open('hotel.txt', 'W')
    for i in Passengers:
        outfile.write('身份证号：' + i['Id'] + '                姓名：' + i['name'] + '                旅客入住：' + i[
            'room'] + '             入住时间：' + i['data'] + '\n')
    outfile.close()
    print('成功保存到hotel.txt')
    return Passengers


def printAll(Passengers):
    for i in Passengers:
        print('身份证号：' + i['Id'] + '     姓名：' + i['name'] + '     旅客入住：' + i['room'] + '    入住时间：' + i['data'])
    print('目前有%d个旅客入住本旅店'%(len(Passengers)))
    return Passengers


def cf(num):
    f=False
    for i in num:
        if i[1]==0:
            f=True
            break
    return f


def selectPass(Passengers):
    xm=input('请输入您要修改的用户姓名：')
    flage=False
    passer={}
    for i in Passengers:
        if i['name']==xm:
            room=i['room']
            Passengers.remove(i)
            flage=True
            passer=i
            break
    return flage,passer


def updataPass(Passengers):
    s=selectPass(Passengers)
    if s[0]:
        s[1]['name']=input('请输入修改后用户姓名：')
        s[1]['data'] = input('请输入修改入住时间：')
        s[1]['Id']=input('请输入修改后的旅客身份证：')
        Passengers.append(s[1])
    return Passengers


def run():
    Passengers = []
    dNum = [['单人间1', 0], ['单人间2', 0], ['单人间3', 0], ['单人间4', 0], ['单人间3', 0], ['单人间4', 0]]
    sNum = [['双人间1', 0], ['双人间2', 0], ['双人间3', 0], ['双人间4', 0]]
    print('欢迎来到本旅店！')
    print('------------------------------------------')
    flage = 'y'
    while flage == 'y':
        if len(Passengers) == 0:
            print('当前还没有旅客入住，请入住旅客')
            fj = input('请输入选择1.单人间 2.双人间')
            if fj == '1':
                qk = addPass(Passengers, dNum)
                Passengers = qk[0]
                dNum = qk[1]
            elif fj == '2':
                qk = addPass(Passengers, sNum)
                Passengers = qk[0]
                dNum = qk[1]
            else:
                pass
        else:
            cz = input('请输入你要进行的操作1.旅客住店登记旅客住店登记 2.退房 3.查询 4.入住信息保存到文本 5修改 6退出：')
            if cz == '1':
                fj = input('请输入选择1.单人间 2.双人间:')
                if fj == '1':
                    if cf(dNum):
                        qk = addPass(Passengers, dNum)
                        Passengers = qk[0]
                        dNum = qk[1]
                    else:
                        print('抱歉，现在没有单人间可以安排')

                elif fj == '2':
                    if cf(sNum):
                        qk = addPass(Passengers, sNum)
                        Passengers = qk[0]
                        sNum = qk[1]
                    else:
                        print('抱歉，现在没有单人间可以安排')
                flage = input("是否还要继续，是请输入'y':")
            elif cz == '2':
                fj=deletePass(Passengers,sNum,dNum)
                Passengers=fj[0]
                dNum=fj[1]
                sNum=fj[2]
                flage = input("是否还要继续，是请输入'y':")
            elif cz == '3':
                Passengers = printAll(Passengers)
                flage = input("是否还要继续，是请输入'y':")
            elif cz == '4':
                Passengers = outfiles(Passengers)
                flage = input("是否还要继续，是请输入'y':")
            elif cz=='5':
                Passengers = updataPass(Passengers)
                flage = input("是否还要继续，是请输入'y':")
            else:
                sys.exit()


if __name__ == '__main__':
    run()

