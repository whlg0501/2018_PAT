"""
1037 在霍格沃茨找零钱（20）（20 分）提问

如果你是哈利·波特迷，你会知道魔法世界有它自己的货币系统 —— 就如海格告诉哈利的：“十七个银西可(Sickle)兑一个加隆(Galleon)，
二十九个纳特(Knut)兑一个西可，很容易。”
现在，给定哈利应付的价钱P和他实付的钱A，你的任务是写一个程序来计算他应该被找的零钱。

输入格式：

输入在1行中分别给出P和A，格式为“Galleon.Sickle.Knut”，
其间用1个空格分隔。这里Galleon是[0, 10^7^]区间内的整数，Sickle是[0, 17)区间内的整数，Knut是[0, 29)区间内的整数。

输出格式：

在一行中用与输入同样的格式输出哈利应该被找的零钱。如果他没带够钱，那么输出的应该是负数。

输入样例1：

10.16.27 14.1.28

输出样例1：

3.2.1

输入样例2：

14.1.28 10.16.27

输出样例2：

-3.2.1

"""

# 十进制模拟
# 5.21 -> 521
# 6 -> 600
# 79 // 10 = 7
# 79 % 10 = 9
# 0.79

def moneyToInt(s):
    result = 0
    money = s.split(".")
    knut = int(money[2])
    sickle = int(money[1])
    galleon = int(money[0])

    result = galleon * 17 * 29 + sickle * 29 + knut

    return result
# print(moneyToInt("10.16.27"))


def intToMoney(n):
    result = ""
    flag = ""

    if(n < 0):
        n = -n
        flag = "-"
    
    knut = n % 29
    n //= 29
    sickle = n % 17
    n //= 17
    galleon = n

    result = "{}.{}.{}".format(galleon, sickle, knut)
    result = flag + result

    return result

# print(intToMoney(moneyToInt("10.16.27")))
# print(intToMoney(-5421))

def main():
    input_line = input().split(" ")
    p = input_line[0]
    a = input_line[1]

    result = moneyToInt(a) - moneyToInt(p)
    print(intToMoney(result))

main()