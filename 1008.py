# lst = [1, 2, 3, 4, 5, 6]
# lst2 = ['a', 'b', 'c', 'd', 'e', 'f']




# def moveLeft(lst, position):
#     if (position % len(lst) == 0):
#         start = 0
#     else:
#         position = position % len(lst)
#         start = len(lst) - position

#     end = start + len(lst)
#     # print(start)
#     result = str(lst2[start])


#     for i in range(start + 1, end):
#         if (i > len(lst) - 1):
#             i -= len(lst)
#         # print(i)
#         result += ' ' + str(lst[i])
    
#     print(result)


# for i in range(0, 100):
#     moveLeft(lst2, i)


def moveLeft(lst, position):
    if (position % len(lst) == 0):
        start = 0
    else:
        position = position % len(lst)
        start = len(lst) - position

    end = start + len(lst)
    # print(start)
    result = str(lst[start])


    for i in range(start + 1, end):
        if (i > len(lst) - 1):
            i -= len(lst)
        # print(i)
        result += ' ' + str(lst[i])
    
    print(result)

position = int(input().split(' ')[1])
input_str = input().split(' ')
lst = []
for i in input_str:
    lst.append(int(i))

moveLeft(lst, position)