"""
1018 锤子剪刀布 (20)（20 分）

大家应该都会玩“锤子剪刀布”的游戏：两人同时给出手势，胜负规则如图所示：

现给出两人的交锋记录，请统计双方的胜、平、负次数，并且给出双方分别出什么手势的胜算最大。

输入格式：

输入第1行给出正整数N（<=10^5^），即双方交锋的次数。随后N行，每行给出一次交锋的信息，即甲、乙双方同时给出的的手势。C代表“锤子”、J代表“剪刀”、B代表“布”，第1个字母代表甲方，第2个代表乙方，中间有1个空格。

输出格式：

输出第1、2行分别给出甲、乙的胜、平、负次数，数字间以1个空格分隔。第3行给出两个字母，分别代表甲、乙获胜次数最多的手势，中间有1个空格。如果解不唯一，则输出按字母序最小的解。

输入样例：

10
C J
J B
C B
B B
B C
C C
C B
J B
B C
J J

输出样例：

5 3 2
2 3 5
B B

"""

# 超时2分
def getMostWin(win_lst):
    BCJ = ["B", "C", "J"]
    result = [0, 0, 0]
    for i in win_lst:
        if(i == "B"):
            result[0] += 1
        elif(i == "C"):
            result[1] += 1
        elif(i == "J"):
            result[2] += 1

    my_max = max(result)
    for i in range(0, len(result)):
        if(result[i] == my_max):
            return BCJ[i]

# print(getMostWin(["B", "B", "B", "B", "J", "J", "J", "J", "C"]))

def getList():
    result = []
    num = int(input())
    count = 0
    while(count < num):
        item = input()
        result.append(item)
        count += 1
    return result

def win(lst):
    win = 0
    tie = 0
    lost = 0
    my_winList = []
    my_lostList = []
    win_lst = ["B C", "C J", "J B"]
    tie_lst = ["B B", "C C", "J J"]
    lost_lst = ["B J", "C B", "J C"]
    for i in lst:
        if(i in win_lst):
            win += 1
            my_winList.append(i[0])
        elif(i in tie_lst):
            tie += 1
        elif(i in lost_lst):
            lost += 1
            my_lostList.append(i[2])
    print("%d %d %d" %(win, tie, lost))
    print("%d %d %d" %(lost, tie, win))
    return [my_winList, my_lostList]

k = win(getList())
print("%s %s" %(getMostWin(k[0]), getMostWin(k[1])))