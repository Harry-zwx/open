import re

def name():
    global name   #定义变量name为全局变量
    while True:
        name = input("请输入你的姓名：")
        for _char in name:   #检验是否全是中文字符
            if not '\u4e00' <= _char <= '\u9fff':  #中文字符的编码范围是：\u4e00 - \u9fff
                print("输入有误，请重新输入：")
                break
        else:
            print("输入成功")
            break
            
def phone():
    global phone
    while True:
        phone = input("请输入手机号码:")
        phone_pat = re.compile('^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$')

        res = re.search(phone_pat,phone)
        if not res:
            print("手机号码异常，请重新输入:")
            continue
        print("手机号码正确")
        break

def idnumber():
    global idnumber
    while True:
        idnumber = input("请输入身份证号码:")
        idnumber_pat = re.compile("^[1-9]\d{5}(18|19|20)\d{2}(0[1-8]|1[0-2])(0[1-9]|[12][0-9]|3[01])\d{3}[0-9xX]$")
        res = re.search(idnumber_pat,idnumber)
        if not res:
            print("身份证号码异常，请重新输入:")
            continue
        print("身份证号码正确")
        break


    def gender(idnumber):  #身份证第17位奇数为男性，偶数为女性
        global gender
        if int(idnumber[16]) % 2 == 0:
            gender = "女"
        else:
            gerder = "男"
    check_gender(idnumber)


    def birth(idnumber): #身份证
        global birthdate
        year = idnumber[6:10]
        mouth = idnumber[10:12]
        day = idnumber[12:14]
        birthdate = f"{year}年{mouth}月{day}日"
    check_birth_date(idnumber)


def display():
    print(
f'------------------------------\n姓名：{name}\n性别：{gender}\n出生年月：{birthdate}\n身份证号：{idnumber}\n电话：{phone}\n-----------------------------')


while True:
    add_name()
    add_phone()                
    add_idnumber()
    display()
