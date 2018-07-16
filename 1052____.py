"""
1052 卖个萌 (20)（20 分）

萌萌哒表情符号通常由“手”、“眼”、“口”三个主要部分组成。简单起见，我们假设一个表情符号是按下列格式输出的：

[左手]([左眼][口][右眼])[右手]

现给出可选用的符号集合，请你按用户的要求输出表情。

输入格式：

输入首先在前三行顺序对应给出手、眼、口的可选符号集。每个符号括在一对方括号[]内。题目保证每个集合都至少有一个符号，并不超过10个符号；每个符号包含1到4个非空字符。

之后一行给出一个正整数K，为用户请求的个数。随后K行，每行给出一个用户的符号选择，顺序为左手、左眼、口、右眼、右手——这里只给出符号在相应集合中的序号（从1开始），数字间以空格分隔。

输出格式：

对每个用户请求，在一行中输出生成的表情。若用户选择的序号不存在，则输出“Are you kidding me? @\/@”。

输入样例：

[╮][╭][o][~\][/~]  [<][>]
 [╯][╰][^][-][=][>][<][@][⊙]
[Д][▽][_][ε][^]  ...
4
1 1 2 2 2
6 8 1 5 5
3 3 4 3 3
2 10 3 9 3

输出样例：

╮(╯▽╰)╭
<(@Д=)/~
o(^ε^)o
Are you kidding me? @\/@

"""

def saveTextFace(s):
    textface_list = []
    i = 0
    while(i < len(s)):
        item = ''
        while(s[i] != ']' and s[i] != ' '):            
            item += s[i]
            i += 1
        if(item != ''):
            textface_list.append(item[1:])
        i += 1
    return textface_list




def getTextFace():
    result = []
    i = 0
    while(i < 3):
        item = input()
        result.append(saveTextFace(item))
        i += 1
    return result

# print(getTextFace())

def getUserData():
    num = int(input())
    count = 0
    userdata_list = []
    while(count < num):
        item = input().split(" ")
        item = [(int(i) - 1) for i in item]
        userdata_list.append(item)
        count += 1
    return userdata_list

# print(getUserData())

def handsLegal(hands, data):
    length = len(hands)
    left_hand = data[0]
    right_hand = data[4]
    return (left_hand >= 0 and left_hand < length) and (right_hand >= 0 and right_hand < length)

def eyesLegal(eyes, data):
    length = len(eyes)
    left_eyes = data[1]
    right_eyes = data[3]
    return (left_eyes >= 0 and left_eyes < length) and (right_eyes >= 0 and right_eyes < length)

def mouthLegal(mouth, data):
    length = len(mouth)
    mouth = data[2]
    return (mouth >= 0 and mouth < length)


def showTextFace(textface, data):
    result = "Are you kidding me? @\\/@"

    hands = textface[0]
    eyes = textface[1]
    mouth = textface[2]

    if(handsLegal(hands, data) and mouthLegal(mouth, data) and eyesLegal(eyes, data)):
        result = "%s(%s%s%s)%s"%(hands[data[0]], eyes[data[1]], mouth[data[2]], eyes[data[3]], hands[data[4]])
    print(result)


def main():
    textface = getTextFace()
    userdata = getUserData()
    for data in userdata:
        showTextFace(textface, data)

main()