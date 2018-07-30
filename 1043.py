"""
1043 输出PATest(20)（20 分）提问

给定一个长度不超过10000的、仅由英文字母构成的字符串。请将字符重新调整顺序，按“PATestPATest....”这样的顺序输出，并忽略其它字符。当然，六种字符的个数不一定是一样多的，若某种字符已经输出完，则余下的字符仍按PATest的顺序打印，直到所有字符都被输出。

输入格式：

输入在一行中给出一个长度不超过10000的、仅由英文字母构成的非空字符串。

输出格式：

在一行中按题目要求输出排序后的字符串。题目保证输出非空。

输入样例：

redlesPayBestPATTopTeePHPereatitAPPT

输出样例：

PATestPATestPTetPTePePee

"""

def main():
    char_num = [0, 0, 0, 0, 0, 0]
    char_list = ['P', 'A', 'T', 'e', 's', 't']
    # 生成char_num列表
    s = input()
    for c in s:
        for index in range(0, len(char_list)):
            if(c == char_list[index]):
                char_num[index] += 1
    
    # 用char_num列表打印
    while(sum(char_num) > 0):
        for index in range(0, len(char_num)):
            if(char_num[index] > 0):
                char_num[index] -= 1
                print("{}".format(char_list[index]), end = "")

main()