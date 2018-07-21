"""
1004 成绩排名 (20)（20 分）

读入n名学生的姓名、学号、成绩，分别输出成绩最高和成绩最低学生的姓名和学号。

输入格式：每个测试输入包含1个测试用例，格式为

  第1行：正整数n
  第2行：第1个学生的姓名 学号 成绩
  第3行：第2个学生的姓名 学号 成绩
  第n+1行：第n个学生的姓名 学号 成绩

其中姓名和学号均为不超过10个字符的字符串，成绩为0到100之间的一个整数，这里保证在一组测试用例中没有两个学生的成绩是相同的。

输出格式：对每个测试用例输出2行，第1行是成绩最高学生的姓名和学号，第2行是成绩最低学生的姓名和学号，字符串间有1空格。

输入样例：

3
Joe Math990112 89
Mike CS991301 100
Mary EE990830 95

输出样例：

Mike CS991301
Joe Math990112

"""

class student(object):
    def __init__(self, name, id, points):
        self.name = name
        self.id = id
        self.points = points
    
def main():
    studentsList = []
    n = int(input())
    count = 0
    while(count < n):
        input_string = input().split(" ")
        studentsList.append(student(input_string[0], input_string[1], int(input_string[2])))
        count += 1
    
    max = studentsList[0]
    min = studentsList[0]
    for i in range(0, len(studentsList)):
        if(studentsList[i].points > max.points):
            max = studentsList[i]
        if(studentsList[i].points < min.points):
            min = studentsList[i]

    print("{} {}".format(max.name, max.id))
    print("{} {}".format(min.name, min.id))

main()

# 注意format比%要好用的多