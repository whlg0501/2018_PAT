"""
1058 选择题（20 分）

批改多选题是比较麻烦的事情，本题就请你写个程序帮助老师批改多选题，并且指出哪道题错的人最多。
输入格式：

输入在第一行给出两个正整数 N（≤ 1000）和 M（≤ 100），分
别是学生人数和多选题的个数。随后 M 行，每行顺次给出一道题的
满分值（不超过 5 的正整数）、选项个数（不少于 2 且不超过 5 的
正整数）、正确选项个数（不超过选项个数的正整数）、所有正确
选项。注意每题的选项从小写英文字母 a 开始顺次排列。各项间以
1 个空格分隔。最后 N 行，每行给出一个学生的答题情况，其每题
答案格式为 (选中的选项个数 选项1 ……)，按题目顺序给出。注意：
题目保证学生的答题情况是合法的，即不存在选中的选项数超过
实际选项数的情况。
输出格式：

按照输入的顺序给出每个学生的得分，每个分数占一行。
注意判题时只有选择全部正确才能得到该题的分数。
最后一行输出错得最多的题目的错误次数和编号（题目按照输入的顺序从 1 开始编号）。
如果有并列，则按编号递增顺序输出。数字间用空格分隔，行首尾不得有多余空格。
如果所有题目都没有人错，则在最后一行输出 Too simple。
输入样例：

3 4 
3 4 2 a c
2 5 1 b
5 3 2 b c
1 5 4 a b d e
(2 a c) (2 b d) (2 a c) (3 a b e)
(2 a c) (1 b) (2 a b) (4 a b d e)
(2 b d) (1 e) (2 b c) (4 a b c d)

输出样例：

3
6
5
2 2 3 4
"""

# 非常实用的套路
def getStringInBrackets(s):
    """读取括号中的字符串"""

    strat_flag = "("
    end_flag = ")"
    temp = ''
    result = []
    i = 0
    read = False
    while(i < len(s)):
        if(s[i] == strat_flag):
            read = True
        elif(s[i] == end_flag):
            read = False
            result.append(temp)
            temp = ''
        else:
            if(read):
                temp += s[i]
        i += 1
    
    return result
    
# print(getstringInBrackets("(a + b = c)    (ccc + kkk = ddd)"))

def getProblem(problem_number):
    """题目列表"""
    problems_list = []
    """读取题目信息"""
    for i in range(0, problem_number):
        """题目字典的初始化"""
        problem_dict = {"value":0, "selection":0, "correct":0, 
                "answer":[], "wrong":0}

        problem = input().split(" ")
        problem_dict["value"] = int(problem[0])
        problem_dict["selection"] = int(problem[1])
        problem_dict["correct"] = int(problem[2])
        problem_dict["answer"] = problem[3:]
        problems_list.append(problem_dict)
    return problems_list

# print(getProblem(4))

def getStudentsAnswers(student_number):
    """学生答案列表"""
    students_answers = []

    """读取学生信息"""
    for i in range(0, student_number):
        """单个学生答案列表"""
        student_answers = []
        temp = []
        answer = input()
        answer = getStringInBrackets(answer)
        answer = [s.split(" ") for s in answer]

        for j in answer:
            """学生字典的初始化"""
            student_dict = {"selection":0, "answer":[]}

            student_dict["selection"] = int(j[0])
            student_dict["answer"] = j[1:]
            student_answers.append(student_dict)
        students_answers.append(student_answers)
    return students_answers

# print(getStudentsAnswer(3))


def getStudentPoints(students_answers, problems_list):
    for student in students_answers:
        points = 0
        for i in range(0, len(student)):
            d_student = student[i]
            d_problems = problems_list[i]

            if(d_student["selection"] == d_problems["correct"]):
                if(d_student["answer"] == d_problems["answer"]):
                    points += d_problems["value"]
                else:
                    d_problems["wrong"] += 1
            else: 
                d_problems["wrong"] += 1
        print(points)
    return problems_list

def findMaxWrong(problems_list):
    wrong_max = problems_list[0]["wrong"]
    for i in range(1, len(problems_list)):
        d = problems_list[i]
        if(d["wrong"] > wrong_max):
            wrong_max = d["wrong"]
    
    if(wrong_max == 0):
        result = "Too simple"
    else:
        result = str(wrong_max)
        for i in range(0, len(problems_list)):
            d = problems_list[i]
            if(d["wrong"] == wrong_max):
                result += ' ' + str(i + 1)
    print(result)

def main():
    student_problem = input().split(" ")
    student_number = int(student_problem[0])
    problem_number = int(student_problem[1])

    """获取标准答案和试卷"""
    problems_list = getProblem(problem_number)
    students_answers = getStudentsAnswers(student_number)

    """给学生判分 同时修改problem_list中的wrong值"""
    problems_list = getStudentPoints(students_answers, problems_list)
    
    """统计错题"""
    findMaxWrong(problems_list)

main()