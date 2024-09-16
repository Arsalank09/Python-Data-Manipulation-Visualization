# #a = 'a'
# #b = 'b'
# #c = 'c'
# #d = 'd'
# #e = 'e'

# #a_list = [a, b, c, d, e]
# #print(a_list[0:10])

# #a_list.reverse()
# #print(a_list)


# list1 = [1, 2, 3]
# list2 = [4, 5, 6]


# list3 = list1 + list2
# print(list3)  

# fruit_list = ['banana', 'apple', 'orange', 'grape']
# fruit_list.sort()

# print(fruit_list)

# number_list = [4, 2, 9, 6, 1]
# number_list.sort(reverse=True)
# print(number_list)

# original_dict = {'a': 1, 'b': 2, 'c': 3}
# copied_dict = original_dict.copy()

# copied_dict['a'] = 10
# copied_dict['d'] = 4

# print(original_dict)  
# print(copied_dict)    

# line= '*'
# max_length= 11

# while len(line) <=max_length:
#     print(line)
#     line += '*'

# while len(line)>0:
#     line = line[:-1]
#     print(line)


def print_diamond(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    for i in range(n-2, -1, -1):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

print_diamond(5)




