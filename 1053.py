"""
1053 住房空置率 (20)（20 分）

在不打扰居民的前提下，统计住房空置率的一种方法是根据每户用电量的连续变化规律进行判断。
判断方法如下：

    在观察期内，若存在超过一半的日子用电量低于某给定的阈值e，则该住房为“可能空置”；
    若观察期超过某给定阈值D天，且满足上一个条件，则该住房为“空置”。

现给定某居民区的住户用电量数据，请你统计“可能空置”的比率和“空置”比率，即以上两种状态的住房占居民区住房总套数的百分比。

输入格式：

输入第一行给出正整数N（<=1000），为居民区住房总套数；
正实数e，即低电量阈值；
正整数D，即观察期阈值。
随后N行，每行按以下格式给出一套住房的用电量数据：

K E~1~ E~2~ ... E~K~

其中K为观察的天数，E~i~为第i天的用电量。

输出格式：

在一行中输出“可能空置”的比率和“空置”比率的百分比值，其间以一个空格分隔，保留小数点后1位。

输入样例：

5 0.5 10
6 0.3 0.4 0.5 0.2 0.8 0.6
10 0.0 0.1 0.2 0.3 0.0 0.8 0.6 0.7 0.0 0.5
5 0.4 0.3 0.5 0.1 0.7
11 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1
11 2 2 2 1 1 0.1 1 0.1 0.1 0.1 0.1

输出样例：

40.0% 20.0%

（样例解释：第2、3户为“可能空置”，第4户为“空置”，其他户不是空置。）

"""

# 超过一半的日子->地板除

class CountPower(object):

    def __init__(self, days, power):
        self.days = days
        self.power = power

    def isVacant(self, days_threshold, power_threshold):
        count = 0
        for p in self.power:
            if(p < power_threshold):
                count += 1
        is_vacant = (count > (self.days // 2)) and (self.days > days_threshold)
        maybe_vacant = count > (self.days // 2)
        if(is_vacant):
            state = "Vacant"
        elif(maybe_vacant):        
            state = "Maybe vacant"
        else:
            state = "No vacant"
        return state


def main():
    input_line = input().split(" ")
    num = int(input_line[0])
    power_threshold = float(input_line[1])
    days_threshold = int(input_line[2])

    lst = []
    count = 0 
    while(count < num):
        input_line = input().split(" ")
        days = int(input_line[0])
        power = [float(x) for x in input_line[1:]]
        lst.append(CountPower(days, power))
        count += 1
    
    maybe_vacant = 0
    vacant = 0
    for s in lst:
        if(s.isVacant(days_threshold, power_threshold) == "Maybe vacant"):
            maybe_vacant += 1
        elif(s.isVacant(days_threshold, power_threshold) == "Vacant"):
            vacant += 1
    maybe_vacant /= len(lst)
    vacant /= len(lst)

    print("{:.1f}% {:.1f}%".format(maybe_vacant * 100, vacant * 100))

main()