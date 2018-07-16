"""
1042 字符统计(20)（20 分）

请编写程序，找出一段给定文字中出现最频繁的那个英文字母。

输入格式：

输入在一行中给出一个长度不超过1000的字符串。字符串由ASCII码表中任意可见字符及空格组成，至少包含1个英文字母，以回车结束（回车不算在内）。

输出格式：

在一行中输出出现频率最高的那个英文字母及其出现次数，其间以空格分隔。如果有并列，则输出按字母序最小的那个字母。统计时不区分大小写，输出小写字母。

输入样例：

This is a simple TEST.  There ARE numbers and other symbols 1&2&3...........

输出样例：

e 7
"""
def getInput():
    return input()


def createArray():
    array = []
    for i in range(0, 26):
        array.append(0)
    return array

# print(len(createArray()))

def upperToLower(i):
    result = None
    if(ord(i) >= 65 and ord(i) <= 90):
        result = chr(ord(i) + 32)
    elif(ord(i) >= 97 and ord(i) <= 122):
        result = i
    return result

# print(upperToLower('A'))
# print(upperToLower('a'))
# print(upperToLower('z'))
# print(upperToLower('0'))

def letterRecode(array, s):
    for i in s:
        letter = upperToLower(i)
        if(letter != None):
            index = ord(letter) - ord('a')
            array[index] += 1
    return array

# print(letterRecode())

def findMax(array):
    max = array[0]
    for i in array:
        if(i > max):
            max = i
    return max

# print(findMax([5, 4, 3, 2, 9, 1, 0]))

def findLetter(array):
    max = findMax(array)
    for i in range(0, len(array)):
        if(max == array[i]):
            letter = chr(i + ord('a'))
            print(letter + ' ' + str(max))
            break

# findLetter([5, 4, 3, 2, 9, 1, 0])

def main():
    s = getInput()
    array = createArray()
    recoded_array = letterRecode(array, s)
    findLetter(recoded_array)

main()


