"""
1044 火星数字(20)（20 分）提问

火星人是以13进制计数的：

    地球人的0被火星人称为tret。
    地球人数字1到12的火星文分别为：jan, feb, mar, apr, may, jun, jly, aug, sep, oct, nov, dec。
    火星人将进位以后的12个高位数字分别称为：tam, hel, maa, huh, tou, kes, hei, elo, syy, lok, mer, jou。

例如地球人的数字“29”翻译成火星文就是“hel mar”；而火星文“elo nov”对应地球数字“115”。
为了方便交流，请你编写程序实现地球和火星数字之间的互译。

输入格式：

输入第一行给出一个正整数N（<100），随后N行，每行给出一个[0, 169)区间内的数字 —— 或者是地球文，或者是火星文。

输出格式：

对应输入的每一行，在一行中输出翻译后的另一种语言的数字。

输入样例：

4
29
5
elo nov
tam

输出样例：

hel mar
may
115
13

"""

def earthToMars(s):
    low = ["tret", "jan", "feb", "mar", "apr", "may", "jun", "jly", "aug", "sep", "oct", "nov", "dec"]
    high = ["", "tam", "hel", "maa", "huh", "tou", "kes", "hei", "elo", "syy", "lok", "mer", "jou"]
    
    n = int(s)
    single = n % 13
    tens = n // 13
    if(n == 0):
        result = low[n]
    elif(tens == 0):
        result = "{}".format(low[single])
    elif(single == 0):
        result = "{}".format(high[tens])
    else:
        result = "{} {}".format(high[tens], low[single])

    print(result)

# print(earthToMars("29"))
# print(earthToMars("0"))
# print(earthToMars("5"))
# print(earthToMars("115"))
# print(earthToMars("13"))

def MarsToEarth(s):
    low = ["tret", "jan", "feb", "mar", "apr", "may", "jun", "jly", "aug", "sep", "oct", "nov", "dec"]
    high = ["", "tam", "hel", "maa", "huh", "tou", "kes", "hei", "elo", "syy", "lok", "mer", "jou"]

    s_list = s.split(" ")

    result = 0

    if(len(s_list) == 2):
        tens = s_list[0]
        single = s_list[1]
        
        for i in range(0, len(low)):
            if(low[i] == single):
                result += i
        
        for j in range(1, len(high)):
            if(high[j] == tens):
                result += j * 13
    else:
        if(s in low): 
            for i in range(0, len(low)):
                if(low[i] == s):
                    result += i
        else:
            for j in range(1, len(high)):
                if(high[j] == s):
                    result += j * 13
    print(result)

# MarsToEarth("elo nov")
# MarsToEarth("tam")
# MarsToEarth("hel mar")
# MarsToEarth("may")
# MarsToEarth("tret")


def main():
    num = int(input())
    count = 0
    l = []
    while(count < num):
        s = input()
        l.append(s)
        count += 1
    for s in l:
        if(s.isdigit()):
            earthToMars(s)
        else:
            MarsToEarth(s)

main()