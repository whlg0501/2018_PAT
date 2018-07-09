# number = int(input())

# 一定要理解题意找出隐藏条件
# 2 -> 2
# 10 -> S
# 100 -> B
# 101 -> B1

def main(number):
    temp = number

    gewei = number % 10
    number //= 10
    shiwei = number % 10
    number //= 10
    baiwei = number % 10

    def s_gewei(gewei):
        result = ''
        if (gewei == 0):
            result = ''
        else:
            for i in range(1, gewei + 1):
                result += str(i)
        return result

    def s_shiwei(shiwei):
        result = ''
        if(shiwei == 0):
            result = ''
        else:
            for i in range(0, shiwei):
                result += 'S'
        return result

    def s_baiwei(baiwei):
        result = ''
        for i in range(0, baiwei):
            result += 'B'
        return result

    if (temp < 10):
        result = s_gewei(gewei)
    else:
        result  = s_baiwei(baiwei) + s_shiwei(shiwei) + s_gewei(gewei)

    print(result)

# main(number)

def Unit_test():
    for i in range(0, 1000):
        main(i)

Unit_test()