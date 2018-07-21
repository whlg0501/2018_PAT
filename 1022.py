"""
1022 D进制的A+B (20)（20 分）

输入两个非负10进制整数A和B(<=2^30^-1)，输出A+B的D (1 < D <= 10)进制数。

输入格式：

输入在一行中依次给出3个整数A、B和D。

输出格式：

输出A+B的D进制数。

输入样例：

123 456 8

输出样例：

1103

"""
def numberBaseConversion(n, base = 10):
    result = ""
    if(n == 0):
        result = "0"
    else:
        if(base == 10):
            result = str(n)
        else:
            while(n > 0):
                temp = n % base
                result = str(temp) + result 
                n //= base
    return result        

# print(numberBaseConversion(579))
# print(numberBaseConversion(579, 8))


def main():
    input_string = input().split(" ")
    n = int(input_string[0]) + int(input_string[1])
    base = int(input_string[2])
    print(numberBaseConversion(n, base))

main()