"""
1012 数字分类 (20)（20 分）

给定一系列正整数，请按要求对数字进行分类，并输出以下5个数字：

A1 = 能被5整除的数字中所有偶数的和；

A2 = 将被5除后余1的数字按给出顺序进行交错求和，即计算n1-n2+n3-n4...；

A3 = 被5除后余2的数字的个数；

A4 = 被5除后余3的数字的平均数，精确到小数点后1位；

A5 = 被5除后余4的数字中最大数字。

输入格式：

每个输入包含1个测试用例。每个测试用例先给出一个不超过1000的正整数N，随后给出N个不超过1000的待分类的正整数。数字间以空格分隔。

输出格式：

对给定的N个正整数，按题目要求计算A1~A5并在一行中顺序输出。数字间以空格分隔，但行末不得有多余空格。

若其中某一类数字不存在，则在相应位置输出“N”。

输入样例1：

13 1 2 3 4 5 6 7 8 9 10 20 16 18

输出样例1：

30 11 2 9.7 9

输入样例2：

8 1 2 4 5 6 7 9 16

输出样例2：

N 11 2 N 9

"""

def getNumberList():
    input_string = input().split(" ")
    n = int(input_string[0])
    number_list = input_string[1:]
    number_list = [int(x) for x in number_list]
    return number_list

# print(getNumberList())
# print(len(getNumberList()))

def case1(lst):
    """能被5整除的数字中所有偶数的和"""
    legal_numbers = []
    result = ""

    for i in lst:
        if(i % 5 == 0):
            if(i % 2 == 0):
                legal_numbers.append(i)
    if(legal_numbers):
        result = str(sum(legal_numbers))
    else:
        result = "N"
    
    return result

def case2(lst):
    """将被5除后余1的数字按给出顺序进行交错求和:计算n1-n2+n3-n4..."""
    legal_numbers = []
    sum = 0
    result = ""

    for i in lst:
        if(i % 5 == 1):
            legal_numbers.append(i)

    if(legal_numbers):
        for i in range(0, len(legal_numbers)):
            if(i % 2 == 0):
                sum += legal_numbers[i]
            else:
                sum += -legal_numbers[i]
        result = str(sum)
    else:
        result = "N"
    
    return result

def case3(lst):
    """被5除后余2的数字的个数"""
    legal_numbers = []
    result = ""

    for i in lst:
        if(i % 5 == 2):
            legal_numbers.append(i)

    if(legal_numbers):
        result = str(len(legal_numbers))
    else:
        result = "N"
    
    return result

def case4(lst):
    """被5除后余3的数字的平均数，精确到小数点后1位"""
    legal_numbers = []
    result = ""

    for i in lst:
        if(i % 5 == 3):
            legal_numbers.append(i)

    if(legal_numbers):
        # result = str(len(legal_numbers))
        average = sum(legal_numbers) / len(legal_numbers)
        result = str(round(average, 1))
    else:
        result = "N"
    
    return result

def case5(lst):
    """ 被5除后余4的数字中最大数字"""
    legal_numbers = []
    result = ""

    for i in lst:
        if(i % 5 == 4):
            legal_numbers.append(i)
    if(legal_numbers):
        result = str(max(legal_numbers))
    else:
        result = "N"
    
    return result

def main():
    lst = getNumberList()
    result = "%s %s %s %s %s"%(case1(lst), case2(lst), case3(lst), 
            case4(lst), case5(lst))
    print(result)

main()