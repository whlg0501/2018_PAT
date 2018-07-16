"""
1081 检查密码（15 分）

本题要求你帮助某网站的用户注册模块写一个密码合法性检查的小功能。
该网站要求用户设置的密码必须由不少于6个字符组成，并且只能有英文字母、数字和小数点 .，
还必须既有字母也有数字。
输入格式：

输入第一行给出一个正整数 N（≤ 100），随后 N 行，每行给出一个用户设置的密码，
为不超过 80 个字符的非空字符串，以回车结束。
输出格式：

对每个用户的密码，在一行中输出系统反馈信息，分以下5种：

    如果密码合法，输出Your password is wan mei.；
    如果密码太短，不论合法与否，都输出Your password is tai duan le.；
    如果密码长度合法，但存在不合法字符，则输出Your password is tai luan le.；
    如果密码长度合法，但只有字母没有数字，则输出Your password needs shu zi.；
    如果密码长度合法，但只有数字没有字母，则输出Your password needs zi mu.。

输入样例：

5
123s
zheshi.wodepw
1234.5678
WanMei23333
pass*word.6

输出样例：

Your password is tai duan le.
Your password needs shu zi.
Your password needs zi mu.
Your password is wan mei.
Your password is tai luan le.
"""

def getPasswords():
    num = int(input())
    result = []
    for i in range(0, num):
        password = input()
        result.append(password)
    return result
# print(getPasswords())

def hasillegal(s):
    legal_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.0123456789"
    result = False
    for i in s:
        if(i in legal_list):
            continue
        else:
            result = True
            break
    return result

def nodigit(s):
    letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz."
    result = True
    for i in s:
        if(i in letter):
            continue
        else:
            result = False
            break
    return result

def noletter(s):
    digit = "0123456789."
    result = True
    for i in s:
        if(i in digit):
            continue
        else:
            result = False
            break
    return result

def main():
    passwords = getPasswords()
    for password in passwords:
        if(len(password) < 6):
            print("Your password is tai duan le.")
        elif(len(password) >= 6):
            if(hasillegal(password)):
                print("Your password is tai luan le.")
            elif(nodigit(password)):
                print("Your password needs shu zi.")
            elif(noletter(password)):
                print("Your password needs zi mu.")
            else:
                print("Your password is wan mei.")

main()
