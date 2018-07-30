"""
1032 挖掘机技术哪家强(20)（20 分）提问

为了用事实说明挖掘机技术到底哪家强，PAT组织了一场挖掘机技能大赛。现请你根据比赛结果统计出技术最强的那个学校。

输入格式：

输入在第1行给出不超过10^5^的正整数N，即参赛人数。随后N行，每行给出一位参赛者的信息和成绩，包括其所代表的学校的编号（从1开始连续编号）、及其比赛成绩（百分制），中间以空格分隔。

输出格式：

在一行中给出总得分最高的学校的编号、及其总分，中间以空格分隔。题目保证答案唯一，没有并列。

输入样例：

6
3 65
2 80
1 100
2 70
3 40
3 0

输出样例：

2 150

"""
# 卡常数导致超时
# 得分 17/20

def generateList(num):
    result = []
    for i in range(0, num + 1):
        result.append(0)
    return result

# print(generateList(5))


def addPoints(num):
    result = generateList(num)
    count = 0
    while(count < num):
        input_line = input().split(" ")
        index = int(input_line[0])
        value = int(input_line[1])
        result[index] += value
        count += 1
    return result

# print(addPoints(6))

def main():
    num = int(input())
    lst = addPoints(num)
    value = max(lst)

    index  = 0
    for i in range(1, len(lst)):
        if(lst[i] == value):
            index = i
            break
    
    print("{} {}".format(index, value))

main()
            


