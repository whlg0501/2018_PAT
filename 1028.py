"""
1028 人口普查(20)（20 分）提问

某城镇进行人口普查，得到了全体居民的生日。现请你写个程序，找出镇上最年长和最年轻的人。

这里确保每个输入的日期都是合法的，但不一定是合理的——假设已知镇上没有超过200岁的老人，而今天是2014年9月6日，所以超过200岁的生日和未出生的生日都是不合理的，应该被过滤掉。

输入格式：

输入在第一行给出正整数N，取值在(0, 10^5^]；随后N行，每行给出1个人的姓名（由不超过5个英文字母组成的字符串）、以及按“yyyy/mm/dd”（即年/月/日）格式给出的生日。题目保证最年长和最年轻的人没有并列。

输出格式：

在一行中顺序输出有效生日的个数、最年长人和最年轻人的姓名，其间以空格分隔。

输入样例：

5
John 2001/05/12
Tom 1814/09/06
Ann 2121/01/30
James 1814/09/05
Steve 1967/11/20

输出样例：

3 Tom John

"""

import datetime

# d0 = datetime.datetime(2014, 9, 6)
# lower = datetime.datetime(1814, 9, 6)

class mypeople(object):

    def __init__(self, name, date):
        self.name = name
        self.date = date

    def getdays(self):
        date_lst = self.date.split("/")
        year = int(date_lst[0])
        month = int(date_lst[1])
        day = int(date_lst[2])

        birthday = datetime.datetime(year, month, day)
        d0 = datetime.datetime(2014, 9, 6)
        lower = datetime.datetime(1814, 9, 6)
        oldest = (d0 - lower).days
        days = (d0 - birthday).days

        # if(days <= oldest and days > 0):
        return days


# p1 = people("xlz", "1814/09/06")
# print(p1.getdays())
# p2 = people("wsb", "1814/09/05")
# print(p2.getdays())


def getInput():
    peoples = []
    total = int(input())
    count = 0
    illegal_num = 0
    illegal = None

    while(count < total):
        input_line = input().split(" ")
        name = input_line[0]
        date = input_line[1]
        illegal = mypeople(name, date)
        if(illegal.getdays() < 0 or illegal.getdays() > 73049):
            # 1814年9月6日
            illegal_num += 1
        else:
            peoples.append(illegal)
        count += 1
    if((total - illegal_num) == 0):
        print(0)
    else:
        print(total - illegal_num, end = " ")

    # for item in peoples:
    #     print(item.name)
    return peoples

# def main():
#     peoples = getInput()

#     flag1 = 0
#     for i in peoples:
#         if(i.getdays() > flag1):
#             flag1 = i.getdays()
#             oldest = i
#     print(oldest.name, end = " ")
    
#     # flag2 = peoples[0].getdays() 千万不能用这个写法
#     flag2 = 73050
#     for j in peoples:
#         if(j.getdays() < flag2):
#             flag2 = j.getdays()
#             youngest = j
#     print(youngest.name)




# main()

def main():
    peoples = getInput()
    if(peoples != []):
        oldest = max(peoples, key = lambda x : x.getdays())
        youngest = min(peoples, key = lambda x : x.getdays())
        print(oldest.name, end = " ")
        print(youngest.name)

main()