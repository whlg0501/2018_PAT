"""
1015 德才论 (25)（25 分）

宋代史学家司马光在《资治通鉴》中有一段著名的“德才论”：“是故才德全尽谓之圣人，才德兼亡谓之愚人，德胜才谓之君子，才胜德谓之小人。凡取人之术，苟不得圣人，君子而与之，与其得小人，不若得愚人。”

现给出一批考生的德才分数，请根据司马光的理论给出录取排名。

输入格式：

输入第1行给出3个正整数，分别为：N（<=10^5^），即考生总数；L（>=60），为录取最低分数线，即德分和才分均不低于L的考生才有资格被考虑录取；H（<100），为优先录取线——德分和才分均不低于此线的被定义为“才德全尽”，此类考生按德才总分从高到低排序；才分不到但德分到线的一类考生属于“德胜才”，也按总分排序，但排在第一类考生之后；德才分均低于H，但是德分不低于才分的考生属于“才德兼亡”但尚有“德胜才”者，按总分排序，但排在第二类考生之后；其他达到最低线L的考生也按总分排序，但排在第三类考生之后。

随后N行，每行给出一位考生的信息，包括：准考证号、德分、才分，其中准考证号为8位整数，德才分为区间[0, 100]内的整数。数字间以空格分隔。

输出格式：

输出第1行首先给出达到最低分数线的考生人数M，随后M行，每行按照输入格式输出一位考生的信息，考生按输入中说明的规则从高到低排序。当某类考生中有多人总分相同时，按其德分降序排列；若德分也并列，则按准考证号的升序输出。

输入样例：

14 60 80
10000001 64 90
10000002 90 60
10000011 85 80
10000003 85 80
10000004 80 85
10000005 82 77
10000006 83 76
10000007 90 78
10000008 75 79
10000009 59 90
10000010 88 45
10000012 80 100
10000013 90 99
10000014 66 60

输出样例：

12
10000013 90 99
10000012 80 100
10000003 85 80
10000011 85 80
10000004 80 85
10000007 90 78
10000006 83 76
10000005 82 77
10000002 90 60
10000014 66 60
10000008 75 79
10000001 64 90
"""

class student(object):
    def __init__(self, number, de, cai):
        self.number = number
        self.de = de
        self.cai = cai
        self.zong = self.de + self.cai
        self.flag = 0

    def getflag(self, enroll, outstanding):
        if(self.de >= outstanding and self.cai >= outstanding):
            self.flag = 5
        elif(self.de >= outstanding and (self.cai >= enroll and self.de > self.cai)):
            self.flag = 4 
        elif((self.cai < outstanding and self.cai >= enroll) and (self.de < outstanding and self.de >= enroll) and (self.de > self.cai)):
            self.flag = 3
        elif(self.de >= enroll and self.cai >= enroll):
            self.flag = 2
        elif(self.de <= enroll and self.cai <= enroll):
            self.flag = 1
        return self.flag 

# a = student(1001, 90, 80)
# b = student(1002, 90, 80)
# print(a.getflag(60, 80))

def generateStudents(numberOfStudent):
    studentsList = []
    for i in range(0, numberOfStudent):
        studentInfo = input().split(" ")
        item = student(int(studentInfo[0]), int(studentInfo[1]), int(studentInfo[2]))
        studentsList.append(item)
    return studentsList

def main():
    """处理输入"""
    input_string = input().split(" ")
    numberOfStudent = int(input_string[0])
    enroll = int(input_string[1])
    outstanding = int(input_string[2])

    """生成学生对象列表"""
    studentsList = generateStudents(numberOfStudent) 

    """排序(全部按降序 学号按升序 套路：用负数在降序里排升序)"""
    result = sorted(studentsList, key = lambda item: (item.getflag(enroll, outstanding), item.zong, item.de, -item.number), reverse = True)

    """打印及格人数"""
    count = 0
    for student in result:
        if(student.getflag(enroll, outstanding) > 1):
            count += 1
    print(count)

    """打印合格学生信息"""
    for student in result:
        if(student.getflag(enroll, outstanding) > 1):
            print("%d %d %d" %(student.number, student.de, student.cai))

main()

# 成绩：16/25 三个测试点超时
# 解决办法：在处理数据的同时还要排序的话用内置的sorted还是慢，此时要选择合适的数据结构来排序：堆/红黑树





        
