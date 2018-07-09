"""
1014 福尔摩斯的约会 (20)（20 分）

大侦探福尔摩斯接到一张奇怪的字条：“我们约会吧！ 3485djDkxh4hhGE 2984akDfkkkkggEdsb s&hgsfdk d&Hyscvnm”。
大侦探很快就明白了，字条上奇怪的乱码实际上就是约会的时间“星期四 14:04”
，因为前面两字符串中第1对相同的大写英文字母（大小写有区分）是第4个字母'D'
，代表星期四；
第2对相同的字符是'E'，那是第5个英文字母，代表一天里的第14个钟头（于是一天的0点到23点由数字0到9、以及大写字母A到N表示）；
后面两字符串第1对相同的英文字母's'出现在第4个位置（从0开始计数）上，代表第4分钟。
现给定两对字符串，请帮助福尔摩斯解码得到约会的时间。

输入格式：

输入在4行中分别给出4个非空、不包含空格、且长度不超过60的字符串。

输出格式：

在一行中输出约会的时间，格式为“DAY HH:MM”，其中“DAY”是某星期的3字符缩写，即MON表示星期一，TUE表示星期二，WED表示星期三，THU表示星期四，FRI表示星期五，SAT表示星期六，SUN表示星期日。题目输入保证每个测试存在唯一解。

输入样例：

3485djDkxh4hhGE 
2984akDfkkkkggEdsb 
s&hgsfdk 
d&Hyscvnm

输出样例：

THU 14:04

"""

# equal_1
# equal_2
# 函数需要考虑严格限定 A~G 0~N
# 否则字符匹配相等时会得到错误的索引

def zfill(s):
    result = s
    if(len(s) == 1):
        result = '0' + s
    return result

def findDay(s, day_lst):
    index = ord(s) - ord('A')
    return day_lst[index]
# print(findDay('D', day_lst))

def findHour(s, hour_lst):
    for i in range(0, len(hour_lst)):
        if(hour_lst[i] == s):
            return zfill(str(i))
# print(findHour('E', hour_lst))

def equal_1(i, j):
    c1 = (i == j)
    c2 = ((ord(i) >= 65) and (ord(i) <= 71))
    return c1 and c2

def equal_2(i, j):
    c1 = (i == j)
    c2 = ((ord(i) >= 65) and (ord(i) <= 78))
    c3 = ((ord(i) >= 48) and (ord(i) <= 57))
    return c1 and (c2 or c3)

def getDayAndHour(s1, s2, day_lst, hour_lst):
    day = ''
    hour = ''
    count = 0
    for i in range(0, len(s1)):
        if(equal_1(s1[i], s2[i]) and count == 0):
            day = findDay(s1[i], day_lst)
            count += 1
            continue
        if(equal_2(s1[i], s2[i]) and count == 1):
            hour = findHour(s1[i], hour_lst)
            break
    return day + ' ' + hour

# print(getDayAndHour(s1, s2, day_lst, hour_lst))

def isAlphabeta(s):
    c1 = ((ord(s) >= 65) and (ord(s) <= 90))
    c2 = ((ord(s) >= 97) and (ord(s) <= 122))
    return c1 or c2



def getMinute(s3, s4):
    for i in range(0, len(s3)):
        if(s3[i] == s4[i] and isAlphabeta(s3[i])):
            return zfill(str(i))


def main():
# s1 = '3485djDkxh4hhGE'
# s2 = '2984akDfkkkkggEdsb'
# s3 = 's&hgsfdk'
# s4 = 'd&Hyscvnm'

    day_lst = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    hour_lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
    # print(len(day_lst))
    # print(len(hour_lst))

    input_lst = []
    count = 4
    while(count > 0):
        input_str = input()
        input_lst.append(input_str)
        count -= 1
    
    s1 = input_lst[0]
    s2 = input_lst[1]
    s3 = input_lst[2]
    s4 = input_lst[3]

    result = getDayAndHour(s1, s2, day_lst, hour_lst) + ':' + getMinute(s3, s4)
    print(result)

main()