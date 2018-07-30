"""
1038 统计同成绩学生(20)（20 分）提问

本题要求读入N名学生的成绩，将获得某一给定分数的学生人数输出。

输入格式：

输入在第1行给出不超过10^5^的正整数N，即学生总人数。随后1行给出N名学生的百分制整数成绩，中间以空格分隔。最后1行给出要查询的分数个数K（不超过N的正整数），随后是K个分数，中间以空格分隔。

输出格式：

在一行中按查询顺序给出得分等于指定分数的学生人数，中间以空格分隔，但行末不得有多余空格。

输入样例：

10
60 75 90 55 75 99 82 90 75 50
3 75 90 88

输出样例：

3 2 0

"""

def generateDict(lst):
    result = {}

    for i in lst:
        if(result.get(i) == None):
            result[i] = 1
        else:
            result[i] += 1

    return result

# print(generateDict([60,75,90,55,75,99,82,90,75,50]))

# result = {60: 1, 75: 3, 90: 2, 55: 1, 99: 1, 82: 1, 50: 1}

def findResult(result, lst):
    result_list = []
    for i in lst:
        if(result.get(i) == None):
            result_list.append(0)
        else:
            result_list.append(result[i])
    
    result = str(result_list[0])
    for j in range(1, len(result_list)):
        result += " " + str(result_list[j])
    return result

# print(findResult(result, [75, 90, 88]))

def main():
    n = input()
    lst = input().split(" ")
    find_lst = input().split(" ")[1:]

    d = generateDict(lst)
    result = findResult(d, find_lst)
    print(result)

main()