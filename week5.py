# s, c = input()+'0', 1
# for i in range(len(s)-1):
#     if s[i] == s[i+1]:
#         c += 1
#     if s[i] != s[i+1]:
#         print(s[i], c, sep='', end='')
#         c = 1

# numbers, numbers_out = input().split(), list()
# for i in numbers:
#     if i not in numbers_out and numbers.count(i) > 1:
#         numbers_out.append(i)
# print(*numbers_out)
#
# b = [int(n) for n in input().split()]
# for n in range(len(b)-1):
#     if b[n] in b[n+1:] and b[n] not in b[:n]:
#         print(b[n], end=' ')

# sum2, sum = 0, 0
# while True:
#     num = int(input())
#     sum += num
#     sum2 += num ** 2
#     if sum == 0:
#         break
# print(sum2)

# n, l = int(input()), list()
# for i in range(1, n+1):
#     for j in range(i):
#         if len(l) == n:
#             break
#         l.append(i)
# print(*l)

# n, counter = int(input()), 0
# for i in range(1, n+1):
#     for j in range(i):
#         if counter < n:
#             print(i, end=' ')
#             counter += 1

# l, x = input().split(), input()
# if x not in l:
#     print('Отсутствует')
# else:
#     for i in range(len(l)):
#         if l[i] in x:
#             print(i, end=' ')

# s = list()
# while True:
#     num = input()
#     if num == 'end':
#         break
#     else:
#         l = [int(i) for i in num.split()]
#         s.append(l)
# for i in range(len(s)):
#     for j in range(len(s[i])):
#         sum = (s[i][(j+1)%len(s[i])]) + (s[i][(j-1)%len(s[i])]) + (s[(i-1)%len(s)][j]) + (s[(i+1)%len(s)][j])
#         print(sum, end=' ')
#     print()

# def fx(x):
#     if x <= -2:
#         return 1 - ((x + 2) ** 2)
#     elif 2 < x:
#         return (x - 2) ** 2 + 1
#     else:
#         return (-(x / 2))
# x = float(input())
# print(fx(x))

# def modify_list(l):
#     for i in range(len(l) - 1, -1, -1):
#         if i <= len(l):
#             if l[i] % 2 != 0:
#                 del l[i]
#             else:
#                 l[i] = l[i] // 2
#         else:
#             break
#     return l
# # lst = [1, 3, 2, 5, 7, 8, 2, 3, 4, 5, 6, 10, 5, 8, 3]
# lst = [1,1,1,1,3,3,5]
# print(modify_list(lst))

#Выведите таблицу размером n×n, заполненную числами от 1 до n**2 по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5)
# Sample Input:
# 5
# Sample Output:
# 1 2 3 4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9

# import sys
# l = sys.argv
# print(*l[1:])

# import requests
#
# with open(f'dataset_3378_2.txt') as file:
#     url = file.readline().strip()
# new_file = requests.get(url).text.splitlines()
# c = 0
# for line in new_file:
#     c += 1
# print(c)

# import requests
#
# with open(f'dataset_3378_3.txt') as file:
#     url = file.readline().strip()
#     new_file_link_sample = url.split('/')
#     del new_file_link_sample[-1]
#     new_file_link_sample = '/'.join(new_file_link_sample)
# while True:
#     file_name = requests.get(url).text
#     if 'We' in file_name:
#         print(file_name)
#         break
#     url = (new_file_link_sample + '/' + file_name)

# from math import *
# r = float(input())
# print(pi * 2 * r)