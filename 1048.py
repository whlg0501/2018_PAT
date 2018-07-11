"""
1048 数字加密(20)（20 分）

本题要求实现一种数字加密方法。首先固定一个加密用正整数A，对任一正整数B，将其每1位数字与A的对应位置上的数字进行以下运算：对奇数位，对应位的数字相加后对13取余——这里用J代表10、Q代表11、K代表12；对偶数位，用B的数字减去A的数字，若结果为负数，则再加10。这里令个位为第1位。

输入格式：

输入在一行中依次给出A和B，均为不超过100位的正整数，其间以空格分隔。

输出格式：

在一行中输出加密后的结果。

输入样例：

1234567 368782971

输出样例：

3695Q8118

"""
# 注意点：位数不一样的时候需要在字符串左侧补0，直到两字符串长度相等

def getInput():
    return input().split(" ")

def zfill(s, n):
    while(len(s) < n):
        s = '0' + s
    return s
# print(zfill('abc', 6))

def fixStrings(input_lst):
    s1 = input_lst[0]
    s2 = input_lst[1]
    if(len(s1) > len(s2)):
        input_lst[1] = zfill(s2, len(s1))
    elif(len(s1) < len(s2)):
        input_lst[0] = zfill(s1, len(s2))
    return input_lst
# print(fixStrings(['abc', 'aaaa']))
# print(fixStrings(['abc', 'aa']))

def getResult(s1, s2):
    odd_lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']
    result = ""
    for i in range(-1, -len(s2)-1, -1):
        if(i % 2 == 0):
            item = int(s2[i]) - int(s1[i])
            if(item < 0):
                item += 10
            item = str(item)
        else:
            item = odd_lst[(int(s2[i]) + int(s1[i])) % 13]
        result = item + result
    return result

# print(getResult("1234567", "8782971"))

def main():
    input_lst = getInput()
    s1 = fixStrings(input_lst)[0]
    s2 = fixStrings(input_lst)[1]
    print(getResult(s1, s2))
    
main()