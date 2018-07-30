"""
1051 复数乘法 (15)（15 分）

复数可以写成(A + Bi)的常规形式，其中A是实部，B是虚部，i是虚数单位，满足i^2^ = -1；
也可以写成极坐标下的指数形式(R*e^(Pi)^)，其中R是复数模，P是辐角，i是虚数单位，
其等价于三角形式 R(cos(P) + isin(P))。

现给定两个复数的R和P，要求输出两数乘积的常规形式。

输入格式：

输入在一行中依次给出两个复数的R1, P1, R2, P2，数字间以空格分隔。

输出格式：

在一行中按照“A+Bi”的格式输出两数乘积的常规形式，实部和虚部均保留2位小数。
注意：如果B是负数，则应该写成“A-|B|i”的形式。

输入样例：

2.3 3.5 5.2 0.4

输出样例：

-8.68-8.23i

"""
# 设z1=a+bi，z2=c+di(a、b、c、d∈R)是任意两个复数，
# 那么它们的积(a+bi)(c+di)=(ac-bd)+(bc+ad)i.

#将极坐标形式转化为常规形式
"""
分析：当A或者B小于0但是大于-0.005(比如-0.00001)时候，如果按照A>=0的判断，会输出“-0.00”这样的结果,
事实上应该输出“0.00”【B同理，应该输出“+0.00i”】
"""
import math

def converToComplex(l):
    r, p = [float(x) for x in l]
    a = r * math.cos(p)
    b = r * math.sin(p)
    return complex(a, b)

def main():
    input_line = input().split(" ")
    c1 = [input_line[0], input_line[1]]
    c2 = [input_line[2], input_line[3]]

    c1 = converToComplex(c1)
    c2 = converToComplex(c2)
    product = c1 * c2

    real = product.real
    imag = product.imag

    if(real + 0.005 >= 0 and real < 0):
        real_part = "0.00"
    else:
        real_part = "{:.2f}".format(real)
    
    if(imag >= 0):
        imag_part = "+{:.2f}i".format(imag)
    elif(imag + 0.005 >= 0 and imag < 0):
        imag_part = "+0.00i"
    else:
        imag_part = "{:.2f}i".format(imag)

    result = real_part + imag_part

    print(result)

main()

# if (A + 0.005 >= 0 && A < 0)
#     printf("0.00");
# else
#     printf("%.2f", A);
# if(B >= 0)
#     printf("+%.2fi", B);
# else if (B + 0.005 >= 0 && B < 0)
#     printf("+0.00i");
# else
#     printf("%.2fi", B);
# return 0;
