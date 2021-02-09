# mylist = [1, 2, 3]
#
# listlen = len(mylist)
#
# if listlen % 2 == 0:
#     print('ruleaza #1')
# else:
#     print('ruleaza #2')
#
# print(type(mylist))
# print(id(mylist))
#
# my_list1 = [1, 2, 3, 4, 5, 6, 7, 12, 1, 56]
# list_len = len(my_list1)
#
# index = 0
#
# while index < list_len:
#     list_element = my_list1[index]
#     print('list_element', list_element)
#
#     if list_element % 2 == 0:
#         print(f'{list_element} is even number')
#     else:
#         print(f'{list_element} is od number')
#     index += 1
#
# print('index', index)

# my_list = [2, 34, 56, 88, 0, 2, 33]
#
# for element in my_list:
#     if element % 2 == 0:
#         print('do something')
#     else:
#         print('wrong')
#
# if True:
#     pass
# else:
#     print('else branch')

#
# my_list =[2, 4, 5, 7, 1, 13 ]
#
# list_len = len(my_list)
# index = 0
#
# while index < list_len:
#     list_element = my_list[index]
#
#     if list_element  % 2 == 0:
#         print(f'element {index + 1} with value {list_element} is even')
#
#
#     else:
#         print(f'element {index + 1} with value {list_element} is odd')
#
#     index += 1
# print ('index', index)


def sum_numb(a, b):
    return a + b

def compare(a, b):
    return a < b

nr1 = 5
nr2 = 7

my_sum = sum_numb(nr1, nr2)
print('my_sum', my_sum)

compare1 = compare(nr1, nr2)
print('compare', compare1)