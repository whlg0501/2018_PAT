my_sentence = input()

print(len(my_sentence))
my_lst = my_sentence.split(" ")
result = my_lst[len(my_lst) - 1]
for i in range(len(my_lst) - 2, -1, -1):
    result += ' ' + my_lst[i]

print(len(result))
print(result)
