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
