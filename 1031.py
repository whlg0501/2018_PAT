"""
1031 查验身份证(15)（15 分）

一个合法的身份证号码由17位地区、日期编号和顺序编号加1位校验码组成。校验码的计算规则如下：

首先对前17位数字加权求和，权重分配为：{7，9，10，5，8，4，2，1，6，3，7，9，10，5，8，4，2}；然后将计算的和对11取模得到值Z；最后按照以下关系对应Z值与校验码M的值：

Z：0 1 2 3 4 5 6 7 8 9 10\ M：1 0 X 9 8 7 6 5 4 3 2

现在给定一些身份证号码，请你验证校验码的有效性，并输出有问题的号码。

输入格式：

输入第一行给出正整数N（<= 100）是输入的身份证号码的个数。随后N行，每行给出1个18位身份证号码。

输出格式：

按照输入的顺序每行输出1个有问题的身份证号码。这里并不检验前17位是否合理，只检查前17位是否全为数字且最后1位校验码计算准确。如果所有号码都正常，则输出“All passed”。

输入样例1：

4
320124198808240056
12010X198901011234
110108196711301866
37070419881216001X

输出样例1：

12010X198901011234
110108196711301866
37070419881216001X

输入样例2：

2
320124198808240056
110108196711301862

输出样例2：

All passed
"""

def getInput():
    """输入函数"""
    #输入次数
    number = int(input())
    #返回结果在一个列表中
    input_lst = []
    #控制输入次数 储存全部结果
    count = number
    while(count > 0):
        input_str = input()
        input_lst.append(input_str)
        count -= 1
    return input_lst

# print(getInput())

def isdigit(n):
    return (ord(n) >= 48 and ord(n) <= 57)

# print(isdigit('1'))
# print(isdigit('a'))

def checked(s):
    index = 0
    result = 0
    seventeen = s[:-1]
    z_lst = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    # print(len(z_lst))
    weight_lst = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    # print(len(weight_lst))
    for i in seventeen:
        if(isdigit(i) == False):
            result = False
            break
    else:
        for i in range(0, len(seventeen)):
            index += int(seventeen[i]) * weight_lst[i]
        index = index % 11
        result = (z_lst[index] == s[-1])
    return result

# print(checked('320124198808240056'))
# print(checked('12010X198901011234'))
# print(checked('110108196711301866'))
# print(checked('37070419881216001X'))
# print(checked('320124198808240056'))
# print(checked('110108196711301862'))    

def unpassed():
    result = []
    input_lst = getInput()
    for i in input_lst:
        if(checked(i) == False):
            result.append(i)
    return result

def getOutput():
    result = unpassed()
    if(result):
        for i in result:
            print(i)
    else:
        print("All passed")

getOutput()