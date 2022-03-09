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