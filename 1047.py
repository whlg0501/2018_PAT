"""
1047 编程团体赛(20)（20 分）提问

编程团体赛的规则为：每个参赛队由若干队员组成；所有队员独立比赛；参赛队的成绩为所有队员的成绩和；成绩最高的队获胜。

现给定所有队员的比赛成绩，请你编写程序找出冠军队。

输入格式：

输入第一行给出一个正整数N（<=10000），即所有参赛队员总数。随后N行，每行给出一位队员的成绩，
格式为：“队伍编号-队员编号 成绩”，其中“队伍编号”为1到1000的正整数，
“队员编号”为1到10的正整数，“成绩”为0到100的整数。

输出格式：

在一行中输出冠军队的编号和总成绩，其间以一个空格分隔。注意：题目保证冠军队是唯一的。

输入样例：

6
3-10 99
11-5 87
102-1 0
102-3 100
11-9 89
3-2 61

输出样例：

11 176

"""

# 无视队员编号，用队伍编号生成字典
def generateDict():
    n = int(input())
    count = 0
    d = {}

    while(count < n):
        input_line = input().split(" ")
        points = int(input_line[1])
        team = input_line[0].split("-")[0]

        if(d.get(team) == None):
            d[team] = points
        else:
            d[team] += points

        count += 1
    return d

# print(generateDict())

# 找出字典中的最大值以及对应的键
# def findMax(d):
#     max_total = 0
#     for key in d:
#         if(d[key] > max_total):
#             max_total = d[key]
    
#     for key in d:
#         if(d[key] == max_total):
#             print("{} {}".format(key, d[key]))

"""
为什么可以这么写：
1.max可以作用一个可迭代对象
2.d.items()将字典转化成一个以列表形式返回可遍历的(键, 值) 元组数组
举例：
d = {'3': 160, '11': 176, '102': 100}
d.items()
>>>dict_items([('3', 160), ('11', 176), ('102', 100)])
3.lambda x : x[1] -> 每一个迭代对象用元组的第二个值作比较
4.返回值最大的键值对元祖
"""

def findMax(d):
    k, v = max(d.items(), key = lambda x : x[1])
    print("{} {}".format(k, v))

def main():
    d = generateDict()
    findMax(d)

main()
