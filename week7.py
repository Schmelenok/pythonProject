# numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]
# def average(i):
#     return sum(i) / len(i)
# print(min(numbers, key=average))
# print(max(numbers, key=average))

# points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
# def distance(i):
#     return (i[0] ** 2 + i[1] ** 2) ** 0.5
# print(sorted(points, key=distance))

# numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
# def sum(i):
#     return min(i)+max(i)
# print(sorted(numbers, key=sum))

# athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
# def name(i):                        # return x[i-1]
#     return i[0]
#
# def age(i):
#     return i[1]
#
# def height(i):
#     return i[2]
#
# def weight(i):
#     return i[3]
#
#
# diff = {1:name, 2:age, 3:height, 4:weight}
# text_input = diff[int(input())]
# athletes.sort(key=text_input)
# for i in athletes:                  # [print(*i) for i in sorted(athletes, key=typ)]
#     print(*i)

# from math import *
#
# def two(i):
#     return i ** 2
#
# def cub(i):
#     return i ** 3
#
# def f_sqrt(i):
#     return sqrt(i)
#
# def f_abs(i):
#     return abs(i)
#
# def f_sin(i):
#     return sin(radians(i))
#
# input_num = int(input())
# input_txt = str(input())
# commands = {'квадрат':two, 'куб':cub, 'корень':f_sqrt, 'модуль':f_abs, 'синус':f_sin }
# print(commands[input_txt](input_num))
# 12 14 79 7 4 123 45 90 111
# numbers_list = sorted(input().split(), key=int)    # [int(i) for i in input().split()]
# def difsum(i):
#     s = 0
#     for x in range(len(i)):
#         num = int(i[x])
#         s += num
#     return s                       # return sum([int(i) for i in str(n)]
# print(*sorted(numbers_list, key=difsum))

# def map(function, items, x):
#     result = []
#     for item in items:
#         result.append(function(item, x))
#     return result
# numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]
# numbers = map(round, numbers, 2)
# print(*numbers, sep='\n')

# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
# def divide5(i):
#     if 99 < i < 1000 and i % 5 == 2:
#         return i
# def cube(i):
#     return i ** 3
# numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]
# filtered_numbers = filter(divide5, numbers)
# map_numbers = map(cube,filtered_numbers)
# print(*map_numbers, sep='\n')

# def kvadrat(i,j):
#     return i + j ** 2
# def reduce(operation, items, initial_value):
#     acc = initial_value
#     for item in items:
#         acc = operation(acc, item)
#     return acc
# numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35, 11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36, 72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35, 7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]
# print(reduce(kvadrat, numbers, 0))

# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
# numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35, 11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36, 72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35, 7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]
# def kvadrat(i):
#     return i ** 2
# print(sum(map(kvadrat,numbers)))

# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
# def divide7(i):
#     if 10 < abs(i) < 99 and i % 7 == 0:
#         return i
# def twice(i):
#     return i ** 2
# numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202, 58, 99, 270, 219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208, 231, 178, 201, 260, -35, 152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128, 143, 43, 297, 229, 60, 254, -9, 5, 187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65, 135, 29, 148, 242, 33, 35, 211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274, 73, 197, 272, 54, 278, 26, 280, 13, 171, 2, 79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63, 263, 219, 57, 18, 236, 291, 234, 10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]
# filtered_numbers = filter(divide7, numbers)
# map_numbers = map(twice,filtered_numbers)
# print(sum(map_numbers))

# from functools import reduce
# floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
# words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
# numbers = [4, 6, 9, 23, 5]
# # Исправьте этот код
# map_result = list(map(lambda num: round(num**2,1), floats))
# filter_result = list(filter(lambda name: name[:] == name[::-1] and len(name) > 4, words))
# reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)
# print(map_result)
# print(filter_result)
# print(reduce_result)

# from functools import reduce
#
# data = [['Tokyo', 35676000, 'primary'],
#         ['New York', 19354922, 'nan'],
#         ['Mexico City', 19028000, 'primary'],
#         ['Mumbai', 18978000, 'admin'],
#         ['Sao Paulo', 18845000, 'admin'],
#         ['Delhi', 15926000, 'admin'],
#         ['Shanghai', 14987000, 'admin'],
#         ['Kolkata', 14787000, 'admin'],
#         ['Los Angeles', 12815475, 'nan'],
#         ['Dhaka', 12797394, 'primary'],
#         ['Buenos Aires', 12795000, 'primary'],
#         ['Karachi', 12130000, 'admin'],
#         ['Cairo', 11893000, 'primary'],
#         ['Rio de Janeiro', 11748000, 'admin'],
#         ['Osaka', 11294000, 'admin'],
#         ['Beijing', 11106000, 'primary'],
#         ['Manila', 11100000, 'primary'],
#         ['Moscow', 10452000, 'primary'],
#         ['Istanbul', 10061000, 'admin'],
#         ['Paris', 9904000, 'primary']]
# data_filtered = filter(lambda x: x[1] > 10000000 and x[2] == 'primary', data)
# data_fil_sort = sorted(data_filtered)
# data_fil_sort_map = map(lambda x: x[0], data_fil_sort)
# txt = reduce(lambda x,y: x + y + ', ', data_fil_sort_map, 'Cities: ')[0:-2]
# print(txt)

# func = lambda x: True if x.startswith('a') and x.endswith('a') else False
# print(func('abcd'))
# print(func('bcda'))
# print(func('abcda'))
# print(func('Abcd'))
# print(func('bcdA'))
# print(func('abcdA'))
# def func(string):
#     counter = 0
#     for i in string:
#         if i not in ('.0123456789'):
#             return False
#         if i == '.':
#             counter += 1
#     if float(i) >= 0 and counter < 2:
#         return True
#     else:
#         return False
#
# is_non_negative_num = lambda x: True if func(x) else False          # is_non_negative_num = lambda q: q.replace('.', '', 1).isdigit()
# print(is_non_negative_num('10.34ab'))
# print(is_non_negative_num('10.45'))
# print(is_non_negative_num('-18'))
# print(is_non_negative_num('-34.67'))
# print(is_non_negative_num('987'))
# print(is_non_negative_num('abcd'))
# print(is_non_negative_num('123.122.12'))
# print(is_non_negative_num('123.122'))

# is_num = lambda x: x.replace('.', '', 1).replace('-', '', 1).isdigit()      # is_num = lambda x: x.lstrip('-').replace('.','',1).isdigit()
# print(is_num('10.34ab'))
# print(is_num('10.45'))
# print(is_num('-18'))
# print(is_num('-34.67'))
# print(is_num('987'))
# print(is_num('abcd'))
# print(is_num('123.122.12'))
# print(is_num('-123.122'))
# print(is_num('--13.2'))

# words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse', 'bid', 'wednesday', 'able', 'betray', 'accident', 'abduct', 'bigot', 'bet', 'abandon', 'besides', 'access', 'friday', 'bestow', 'abound', 'absent', 'beware', 'abundant', 'abnormal', 'aboard', 'about', 'accelerate', 'abort', 'thursday', 'tuesday', 'sunday', 'berth', 'beyond', 'benevolent', 'abate', 'abide', 'bicycle', 'beside', 'accept', 'berry', 'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']
# print(*sorted(filter(lambda x: len(x) == 6, words)), sep=' ')

# numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80, 93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94, 37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]
# numbers_filter = filter(lambda x: x % 2 != 0 and x < 47 or x % 2 == 0, numbers)
# numbers_map = map(lambda x: x // 2 if x % 2 == 0 else x, numbers_filter)
# print(*numbers_map, sep=' ')

# data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'), (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'), (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'), (7029917, 'Massachusetts'), (6910840, 'Tennessee')]
# data_sorted = sorted(data, key=lambda x: x[1][-1])
# print(*[f'{i[1]}: {i[0]}' for i in reversed(data_sorted)], sep='\n')

# data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид', 'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']
# data_sorted = sorted(sorted(data), key=lambda x: len(x))
# print(*data_sorted, sep=' ')

# mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory', 'absorb', 1384878, 'sunday', 'about', 454805, 'saturday', 'abort', 2121919, 2552839, 977970, 1772933, 1564063, 'abduct', 901271, 2680434, 'bicycle', 'accelerate', 1109147, 942908, 'berry', 433507, 'bias', 'bestow', 1875665, 'besides', 'bewilder', 1586517, 375290, 1503450, 2713047, 'abnormal', 2286106, 242192, 701049, 2866491, 'benevolent', 'bigot', 'abuse', 'abrupt', 343772, 'able', 2135748, 690280, 686008, 'beyond', 2415643, 'aboard', 'bet', 859105, 'accident', 2223166, 894187, 146564, 1251748, 2851543, 1619426, 2263113, 1618068, 'berth', 'abolish', 'beware', 2618492, 1555062, 'access', 'absent', 'abundant', 2950603, 'betray', 'beverage', 'abide', 'abandon', 2284251, 'wednesday', 2709698, 'thursday', 810387, 'friday', 2576799, 2213552, 1599022, 'accept', 'abuse', 'abound', 1352953, 'bid', 1805326, 1499197, 2241159, 605320, 2347441]
# print(max(mixed_list, key=lambda x: x if type(x) != str else False))

# mixed_list = ['beside', 1, 'accelerate', 0, 'beware', 'absorb', 'besides', 'berry', 15, 65, 'abate', 'thursday', 76, 70, 94, 35, 36, 'berth', 41, 'abnormal', 'bicycle', 'bid', 'sunday', 'saturday', 87, 'bigot', 41, 'abort', 13, 60, 'friday', 26, 13, 'accident', 'access', 40, 26, 20, 75, 13, 40, 67, 12, 'abuse', 78, 10, 80, 'accessory', 20, 'bewilder', 'benevolent', 'bet', 64, 38, 65, 51, 95, 'abduct', 37, 98, 99, 14, 'abandon', 'accept', 46, 'abide', 'beyond', 19, 'about', 76, 26, 'abound', 12, 95, 'wednesday', 'abundant', 'abrupt', 'aboard', 50, 89, 'tuesday', 66, 'bestow', 'absent', 76, 46, 'betray', 47, 'able', 11]
# print(*sorted(mixed_list, key= lambda x: str(x)), sep=' ')

# print(*map(lambda x: abs(int(x)-255), input().split()))

# colors = ['red', 'green', 'blue']
# for index, item in enumerate(colors):
#     print(index, item)
# print(*enumerate(colors))

# def ignore_command(command):
#     ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
#     # for i in ignore:
#     #     if i in command:
#     #         return True
#     # return False
#     return any([i in command for i in ignore])
# print(ignore_command('delete all'))

# countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
# capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
# population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]
# for capital, country, popul in zip(capitals, countries, population):
#     print(f'{capital} is the capital of {country}, population equal {popul} people.')

# abscissas = [float(i) for i in input().split()]
# ordinates = [float(i) for i in input().split()]
# applicates = [float(i) for i in input().split()]
# print(all([x ** 2 + y ** 2 + z ** 2 <= 4 for x,y,z in zip(abscissas, ordinates, applicates)]))

# ip_list = [int(i) for i in input().split('.') if i.isdigit()]
# if len(ip_list) != 4:
#     print(False)
# else:
#     print(all([ 0 <= x <= 255 for x in ip_list]))               # print(all([i.isdigit() and 0 <= int(i) <= 255 for i in input().split('.')]))

# ab_list = [str(i) for i in range(int(input()), int(input())+1)]
# print(*filter(lambda x: x if all(int(x) % int(i) == 0 for i in x if '0' not in i) and '0' not in x else False, ab_list))
# print(*[i for i in range(int(input()), int(input()) + 1) if '0' not in str(i) and all([i % int(j) == 0 for j in str(i)])])

# print(*filter(lambda n: all(int(i) and not n % int(i) for i in str(n)), range(int(input()), int(input()) + 1)))

# txt = str(input())
# print(('NO','YES')[all([any([i.isdigit() for i in txt]), any([i.islower() for i in txt]), any([i.isupper() for i in txt]), len(txt) >= 7])])

# l = list()
# for i in range(int(input())):
#     for j in range(int(input())):
#         l.append(input()[-1])
# print()

# n = int(input())
# print(('NO', 'YES')[all([any(['5' in str(input()) for i in range(int(input()))]) for j in range(n)])])

# file_name = str(input())
# file_link = open(file_name, 'r')
# content = file_link.read()
# print(content)
# file_link.close()

# from random import *
# file_link = open('lines.txt', 'r', encoding='UTF-8')
# content = file_link.readlines()
# print(choice(content))
# file_link.close()


# file_link = open('nums.txt', 'r', encoding='UTF-8')
# content = list(filter(None, [i.strip() for i in file_link.readlines()]))
# print(sum([int(i) for i in content]))
# file_link.close()

# file = open('nums.txt')
# a = file.read()
# print(a)
# b = file.read().split()
#
# s = sum(map(int, file.read().split()))
# file.close()

# txt = """
#
#
#
#
#   453459384
#
#
#            32242"""
# a = txt.split()
# print(a)
# print(sum([int(i) for i in a]))

# file = open('prices.txt', encoding='UTF-8')
# file_content = [i.strip().split('\t') for i in file.readlines()]
# file_sum = sum(map(lambda x: int(x[1])*int(x[2]), file_content))
# print(file_sum)
# print(*[i.strip() for i in file.readlines()[::-1]], sep='\n')

# with open('lines.txt', 'r') as file:
#     # print(max([i.strip() for i in file], key=len))
#     l = list([i.strip() for i in file.readlines()])
#     print(*filter(lambda x: x if len(x) == max(len(i) for i in l) else False, l), sep='\n')

# with open('numbers.txt', 'r') as file:
#     [print(sum(int(i) for i in line.split())) for line in file]

# with open('nums.txt') as file:
#     element = [i.strip() for i in file.readlines()]
#     l = list()
#     for i in element:
#         for j in i:
#             if j not in '0123456789':
#                 i = i.replace(j, ' ')
#         i = i.strip().split()
#         l.extend(i)
#     print(sum(map(int, l)))

# with open('nums.txt', encoding='utf-8') as file:
#     print(sum([int(num) for num in ''.join(list(map(lambda sym: sym if sym.isdigit() else ' ' , file.read()))).split()]))

# with open('nums.txt', encoding='utf-8') as file:
#     # print(list(map(lambda x: x if x.isdigit() else ' ', file.read().split())))
#     print(sum([int(i) for i in ''.join(list(map(lambda x: x if x.isdigit() else ' ', file.read()))).split()]))

# with open('file.txt', encoding='utf-8') as file:
#     text = file.read()
#     lines = text.count('\n') + 1
#     words = text.count(' ') + lines
#     chars = 0
#     for i in text.strip('\n '):
#         if i.isalpha():
#             chars += 1
#     print(f"""Input file contains:
# {chars} letters
# {words} words
# {lines} lines
# """)

# from random import *
# with open('first_names.txt', encoding='utf-8') as f_names, open('last_names.txt', encoding='utf-8') as f_surnames:
#     names = f_names.readlines()
#     surnames = f_surnames.readlines()
#     [print(f'{choice(names).strip()} {choice(surnames).strip()}') for i in range(3)]

# with open('population.txt', encoding='utf-8') as file:
#     cities = [i.strip().split('\t') for i in file.readlines()]
#     [print(i[0]) for i in cities if i[0].startswith('G') and int(i[1]) > 5*10**5]

# def read_csv():
#     with open('data.csv', encoding='utf-8') as file:
#         k = file.readline().strip().split(',')
#         v = [i.strip().split(',') for i in file.readlines()]
#     l = list()
#     for i in v:
#         l.append(dict(zip(k,i)))
#     # print(*l, sep='\n')
#     return l
# read_csv()

# from random import *
# with open('random.txt', 'w', encoding='utf-8') as file_out:
#     file_out.writelines([str(i)+'\n' for i in sample(range(111, 777), 25)])

# with open('output.txt', 'w', encoding='utf-8') as file_out, open('input.txt', encoding='utf-8') as file_in:
#     text = [i.strip() for i in file_in.readlines()]
#     file_out.writelines([f'{str(i[0])}) {i[1]}\n' for i in enumerate(text, 1)])

# with open('new_scores.txt', 'w', encoding='utf-8') as file_out, open('class_scores.txt', encoding='utf-8') as file_in:
#     text = [i.strip().split() for i in file_in.readlines()]
#     names = map(lambda x: x[0], text)
#     marks = map(lambda x: str(int(x[1]) + 5) if int(x[1]) + 5 <= 100 else str(int(x[1]) + (100 - int(x[1]))), text)
#     new_scores = [i for i in zip(names, marks)]
#     file_out.writelines([f'{i[0]} {i[1]}\n' for i in new_scores])

# with open('class_scores.txt') as inp, open('new_scores.txt','w') as out:
#     for line in inp:
#         name, score = line.split()
#         score = int(score) + 5 if int(score) + 5 <= 100 else int(score) + (100 - int(score))
#         out.write(f'{name} {score}\n')

# objects = [1, 2, 1, 2, 3]
# s = set()
# for i in objects:
#     s.add(id(i))
# print(len(s))

# x = print(4)
# print(type(x))

# def closest_mod_5(x):
#     if x % 5 == 0:
#         return x
#     else:
#         return x - x % 5 + 5
#
# x = int(input())
# y = closest_mod_5(x)
# print(y)

# DATABASE = {
#     'Серёга': 'Омск',
#     'Соня': 'Москва',
#     'Миша': 'Москва',
#     'Дима': 'Челябинск',
#     'Алина': 'Красноярск',
#     'Егор': 'Пермь',
#     'Коля': 'Красноярск'
# }

# def process_anfisa(query):
#     if query == 'Сколько у меня друзей?':
#         count = len(DATABASE)
#         return 'У тебя ' + str(count) + ' друзей.'
#     # Здесь проверьте, что переменная query равна строке 'Кто все мои друзья?'
#     elif query == 'Кто все мои друзья?':
#         friends_string = ''
#         # Чтобы получить перечень друзей -
#         # переберите словарь DATABASE в цикле
#         for i in DATABASE:
#              friends_string += ' ' + i     # Добавляйте к переменной friends_string имя друга и пробел
#         # Верните строку, составленную из 'Твои друзья: ' и friends_string
#         return 'Твои друзья:' + friends_string
#     elif query == 'Где все мои друзья?':
#         cities = set(DATABASE.values())
#         friends_string = ''
#         for i in cities:
#             friends_string += ' ' + i
#         return 'Твои друзья в городах:' + friends_string
#     else:
#         return '<неизвестный запрос>'
#
# # Не изменяйте следующий код
# print('Привет, я Анфиса!')
# print(process_anfisa('Сколько у меня друзей?'))
# print(process_anfisa('Кто все мои друзья?'))
# print(process_anfisa('Где все мои друзья?'))

# def calc_stat(listened):  # От англ. calculate statistics, посчитать статистику
#     # Напишите код функции calc_stat()
#     count = 0
#     for i in listened:
#         count += i
#     return len(listened), count
#
# print(f'Вы прослушали {calc_stat([189, 148, 210, 144, 174, 158, 163, 189, 227, 198])[0]} песен общей продолжительностью {calc_stat([189, 148, 210, 144, 174, 158, 163, 189, 227, 198])[1]} минут.')
