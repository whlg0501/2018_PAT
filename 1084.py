"""
1084 外观数列（20 分）

外观数列是指具有以下特点的整数序列：

d, d1, d111, d113, d11231, d112213111, ...

它从不等于 1 的数字 d 开始，序列的第 n+1 项是对第 n 项的描述。比如第 2 项表示第 1 项有 1 个 d，所以就是 d1；第 2 项是 1 个 d（对应 d1）和 1 个 1（对应 11），所以第 3 项就是 d111。又比如第 4 项是 d113，其描述就是 1 个 d，2 个 1，1 个 3，所以下一项就是 d11231。当然这个定义对 d = 1 也成立。本题要求你推算任意给定数字 d 的外观数列的第 N 项。
输入格式：

输入第一行给出 [0,9] 范围内的一个整数 d、以及一个正整数 N（≤ 40），用空格分隔。
输出格式：

在一行中给出数字 d 的外观数列的第 N 项。
输入样例：

1 8

输出样例：

1123123111


"""
def countDigit(s):
    result = ""
    if(len(s) == 1):
        result = s + "1"
    else:
        count = 1
        flag = s[0]
        i = 1
        while(True):
            if(s[i] == flag):
                count += 1
            else:
                # print("%s%s" %(flag, count))
                result += "%s%s" %(flag, count)
                flag = s[i]
                count = 1
            i += 1
            if(i == len(s)):
                # print("%s%s" %(flag, count))
                result += "%s%s" %(flag, count)                
                break        
    return result 

# print(countDigit("1"))
# print(countDigit("11"))
# print(countDigit("12"))
# print(countDigit("1121"))
# print(countDigit("122111"))

def main():
    input_string = input().split(" ")
    num = input_string[0]
    n = int(input_string[1])

    if(n == 1):
        print(num)
    else:
        count = 1
        arrayItem = countDigit(num) 
        while(count < n - 1):
            arrayItem = countDigit(arrayItem)
            count += 1
        print(arrayItem)

main()