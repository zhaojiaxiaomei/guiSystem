'''
2元1瓶饮料
2个空瓶可以换一瓶饮料
4个瓶盖可以换一瓶饮料
问带X（x>2）元可以喝几瓶
n       # 记录饮料数
button  # 记录瓶盖
bottle  # 记录空瓶
money   # 记录多少元钱
'''
n = 0
def drink(money, button=0, bottle=0):
    global n
    if button >= 4:
        button -= 3
        bottle += 1
        n += 1
        drink(money,button,bottle)
    elif bottle >= 2:
        button += 1
        bottle -= 1
        n += 1
        drink(money,button,bottle)
    else:
        if money>1:
            money -= 2
            button += 1
            bottle += 1
            n += 1
            drink(money,button,bottle)
        else:
            #当钱money不足2元，但瓶盖剩余3个，可以先和老板借一个瓶盖，喝了这瓶饮料将瓶盖还给老板，即botton=0，但空瓶多了一个
            if button == 3:
                button = 0
                bottle += 1
                n += 1
                drink(money,button,bottle)
            # 当钱money不足2元，但空瓶剩余1个，可以先和老板借一个空瓶，喝了这瓶饮料将空瓶还给老板，所以空瓶都不可能有剩余
            elif bottle == 1:
                bottle = 0
                button += 1
                n += 1
                drink(money,button,bottle)
            else:
                print('总共喝了%d瓶' % n)
                print('剩余%d个瓶盖' % button)
                print('剩余%d个瓶子' % bottle)
                print('剩余%d元钱' % money)
if __name__ == '__main__':
    s=input('请输入你的钱')
