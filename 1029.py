"""
1029 旧键盘(20)（20 分）提问

旧键盘上坏了几个键，于是在敲一段文字的时候，对应的字符就不会出现。现在给出应该输入的一段文字、以及实际被输入的文字，请你列出肯定坏掉的那些键。

输入格式：

输入在2行中分别给出应该输入的文字、以及实际被输入的文字。每段文字是不超过80个字符的串，由字母A-Z（包括大、小写）、数字0-9、以及下划线“_”（代表空格）组成。题目保证2个字符串均非空。

输出格式：

按照发现顺序，在一行中输出坏掉的键。其中英文字母只输出大写，每个坏键只输出一次。题目保证至少有1个坏键。

输入样例：

7_This_is_a_test
_hs_s_a_es

输出样例：

7TI

"""

# 列表去重
# list2 = []
# list1 = [1,2,3,2,2,2,4,6,5]
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# list2
# [1, 2, 3, 4, 6, 5]

# 思路：
# 全部转化成大写
def upperString(s):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for i in s:
        if(i in lower):
            for j in range(0, len(lower)):
                if(lower[j] == i):
                    result += upper[j]
        else:
            result += i
    return result

# print(upperString("kfjghdkfjhg"))
# print(upperString("7_This_is_a_test"))

# 找出在输入2中没有的存在lst中
def generateList(s1, s2):
    s1 = upperString(s1)
    s2 = upperString(s2)
    result = []
    for i in s1:
        if(i in s2):
            continue
        else:
            result.append(i)
    return result
# print(generateList("7_This_is_a_test", "_hs_s_a_es"))

# 对lst去重
def duplicateRemove(lst):
    result = ""
    for i in lst:
        if(i in result):
            continue
        else:
            result += i
    return result
# print(duplicateRemove(['7', 'T', 'I', 'I', 'T', 'T']))

def main():
    s1 = input()
    s2 = input()

    badkeys = generateList(s1, s2)
    print(duplicateRemove(badkeys))

main()