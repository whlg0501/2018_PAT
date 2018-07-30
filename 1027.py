"""
1027 打印沙漏(20)（20 分）提问

本题要求你写个程序把给定的符号打印成沙漏的形状。例如给定17个“*”，要求按下列格式打印

*****
 ***
  *
 ***
*****

所谓“沙漏形状”，是指每行输出奇数个符号；各行符号中心对齐；相邻两行符号数差2；符号数先从大到小顺序递减到1，再从小到大顺序递增；首尾符号数相等。

给定任意N个符号，不一定能正好组成一个沙漏。要求打印出的沙漏能用掉尽可能多的符号。

输入格式：

输入在一行给出1个正整数N（<=1000）和一个符号，中间以空格分隔。

输出格式：

首先打印出由给定符号组成的最大的沙漏形状，最后在一行中输出剩下没用掉的符号数。

输入样例：

19 *

输出样例：

*****
 ***
  *
 ***
*****
2

"""


def getArray():
    lst = [1]
    for i in range(3, 100, 2):
        lst.append(i)
    return lst

# print(getArray())

def spacefill(s, length):
    # 每一行只有左边有空格
    step = (length - len(s)) // 2
    result = (' ' * step) + s
    return result

# print(spacefill("*******", 7))
# print(spacefill("*****", 7))
# print(spacefill("***", 7))
# print(spacefill("*", 7))

def generateList(num):
    result = [1]
    lst = getArray()
    index = 1

    while(sum(result) < num):
        result.insert(0, lst[index])
        result.append(lst[index])
        # print("result is {}, sum is {}".format(result, sum(result)))
        index += 1
    
    if(sum(result) - num > 0):
        result = result[1:-1]
    
    return result

# print(generateList(22))
# print(generateList(17))

def main():
    input_line = input().split(" ")
    num = int(input_line[0])
    symbol = input_line[1]

    lst = generateList(num)
    length = lst[0]
    for i in lst:
        s = symbol * i
        print(spacefill(s, length))

    remains = num - sum(lst)
    print(remains)

main()