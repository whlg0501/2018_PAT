"""
1016 部分A+B (15)（15 分）

正整数A的“D~A~（为1位整数）部分”定义为由A中所有D~A~组成的新整数P~A~。例如：给定A = 3862767，D~A~ = 6，则A的“6部分”P~A~是66，因为A中有2个6。

现给定A、D~A~、B、D~B~，请编写程序计算P~A~ + P~B~。

输入格式：

输入在一行中依次给出A、D~A~、B、D~B~，中间以空格分隔，其中0 < A, B < 10^10^。

输出格式：

在一行中输出P~A~ + P~B~的值。

输入样例1：

3862767 6 13530293 3

输出样例1：

399

输入样例2：

3862767 1 13530293 8

输出样例2：

0

"""

def generateNumber(seed, n):
    count = 0
    result = 0
    seed = int(seed)

    while(count < n):
        result += seed
        seed *= 10
        count += 1

    return result

# print(generateNumber(6, 3))

def getTimes(s, seed):
    n = 0
    for i in s:
        if(i == seed):
            n += 1
    return n

def main():
    """处理输入"""
    input_string = input().split(" ")

    number_a = input_string[0]
    seed_a = input_string[1]

    number_b = input_string[2]
    seed_b = input_string[3]

    """获取P~A和P~B"""
    n_a = getTimes(number_a, seed_a)
    p_a = generateNumber(seed_a, n_a)

    n_b = getTimes(number_b, seed_b)
    p_b = generateNumber(seed_b, n_b)

    print("%d" %(p_a + p_b))

main()
