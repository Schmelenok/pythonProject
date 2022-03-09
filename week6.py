# a, b = int(input()), int(input())
# if b != 0:
#     print((a + b), (a - b), (a * b), (a / b), (a // b), (a % b), ((a ** 10 + b ** 10) ** (1 / 2)), sep='\n')
#
# weight, rost = float(input()), float(input())
# imt = (weight / (rost ** 2))
# if imt < 18.5:
#     print('Недостаточная масса')
# elif 18.5 <= imt <= 25:
#     print('Оптимальная масса')
# elif imt > 25:
#     print('Избыточная масса')

# chars, price = len(input()), 60
# print(f'{(chars * price) // 100} р. {(chars * price) % 100} коп.')

# print(len([i for i in input().split()]))

# animals = ['Дракон', 'Змея', 'Лошадь', 'Овца', 'Обезьяна', 'Петух', 'Собака', 'Свинья', 'Крыса', 'Бык', 'Тигр', 'Заяц']
# print(animals[(int(input()) + 4 ) % 12])

# num = input()
# if len(num) == 5:
#     print(int(num[::-1]))
# if len(num) == 6:
#     num = num[0] + num[len(num):0:-1]
#     print(int(num))

# a = '927568'
# print(a[:-5])
# print(a[-5:][::-1]+ a[0][2:3])

# txt = [i for i in input()]
# for i in range(len(txt)-3, 0, -3):
#     txt.insert(i, ',')
# print(*txt, sep='')

# n, k = list(range(1,int(input())+1)), int(input())
# while len(n) != 1:
#     for i in range(k-1):
#         n.append(n.pop(0))
#     del n[0]
# print(*n)

# c1 = c2 = c3 = c4 = 0
# for i in range(int(input())):
#     coord = [int(i) for i in input().split()]
#     if coord[0] > 0 and coord[1] > 0:
#         c1 += 1
#     elif coord[0] < 0 and coord[1] > 0:
#         c2 += 1
#     elif coord[0] < 0 and coord[1] < 0:
#         c3 += 1
#     elif coord[0] > 0 and coord[1] < 0:
#         c4 += 1
# print(f'Первая четверть: {c1}\nВторая четверть: {c2}\nТретья четверть: {c3}\nЧетвертая четверть: {c4}')

# l, c = [int(i) for i in input().split()], 0
# for i in range(1, len(l)):
#     if l[i] > l[i - 1]:
#         c += 1
# print(c)

# l = [int(i) for i in input().split()]
# for i in range(1, len(l), 2):
#     l[i - 1], l[i] = l[i], l[i - 1]
# print(*l)

# l = [int(i) for i in input().split()]
# l.insert(0, l.pop(-1))
# print(*l)

# l, c, s = [int(i) for i in input().split()], 0, 1
# while c != len(l)-1:
#     if l[c] != l[c + 1]:
#         s += 1
#     c += 1
# print(s)

# n, s = int(input()), 0
# for i in range(n):
#     s += int(input())
# print(s)

# n = int(input())
# l, num, flag = [int(input()) for i in range(n)], int(input()), 'НЕТ'
# for i in range(len(l)):
#     for j in range(len(l)):
#         if i != j:
#             if l[i] * l[j] == num:
#                 flag = 'ДА'
#                 break
# print(flag)


# nt, nr = input(), input()
# if nt == nr:
#     print('ничья')
# elif nt == 'камень' and nr == 'ножницы' or nt == 'ножницы' and nr == 'бумага' or nt == 'бумага' and nr == 'камень' or nt == 'Спок' and nr =='камень' or nt == 'ножницы' and nr =='ящерица' or nt == 'ящерица' and nr =='бумага' or nt == 'ящерица' and nr =='Спок' or nt == 'камень'and nr =='ящерица':
#     print('Тимур')
# else:
#     print('Руслан')
#
#     a, b = input()[0], input()[0]
#     print('ничья' if a == b else 'Тимур' if a + b in 'нбкяСнябСкн' else 'Руслан')

# n, c, s= input(), 0, 0
# for i in n:
#     if i == 'Р':
#         c += 1
#         if c >= s:
#             s = c
#     if i == 'О':
#         c = 0
# print(s)

# b = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
# word = input()
# txt = word +' запретил букву'
# for i in range(len(b)):
#     if b[i] in txt:
#         print(txt, b[i])
#         txt = txt.replace(b[i], '').strip()
#         if '  ' in txt:
#             txt = txt.replace('  ', ' ')
#     if len(txt) < 1:
#         break
# s = ['0', '222anton456', 'a1n1t1o1n1', '0000a0000n00t00000o000000n', 'gylfole', 'richard', 'ant0n']
# sample, counter, l = ['a', 'n', 't', 'o', 'n'], 0, list()
# for i in range(0, int(input())):
#     txt = input()
#     counter = 0
#     for j in sample:
#         if j in txt:
#             counter += 1
#             txt = txt[txt.find(j):]
#     if counter == 5:
#         l.append(i)
# print(*l)

# constants = [3.1415, 2.71828, 1.1415, 'Argentina']
# # print(type(constants))
# n = int(input())
# my_list = [[i]*n for i in range(n)]
# print(*my_list, sep='\n')

# n, l = int(input()), []
# for elem in range(n):
#     l.append(list(range(1, n+1)))
# print(*l, sep='\n')

# n = int(input())
# print(*[[i for i in range(1, n+1)] for i in range(1, n+1)], sep = "\n")

# n, l = int(input()), []
# for elem in range(1, n+1):
#     l.append(list(range(1, elem+1)))
# print(*l, sep='\n')

# print('abcdefg'.rjust(10))


# n = 3
# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# for i in range(n):
#     for j in range(n):
#         print(a[n - i - 1][n - j - 1], end=' ')
#     print()

# n = 5
# a = [[19, 21, 33, 78, 99],
#      [41, 53, 66, 98, 76],
#      [79, 80, 90, 60, 20],
#      [33, 11, 45, 67, 90],
#      [45, 67, 12, 98, 23]]
#
# maximum = -1
# minimum = 100
#
# for i in range(n):
#     if a[i][i] > maximum:
#         maximum = a[i][i]
#         print(maximum)
#     if a[i][n - i - 1] < minimum:
#         minimum = a[i][n - i - 1]
#         print(minimum)
# print(minimum + maximum)

# a = [[1, 0],[4, 1]]
# print(a*a)

# Pascal triangle___________________________
# n = int(input())
# l = [[1]]
# for i in range(0,n):
#     for j in range(0, n):
#         l.append(list(range(1, l[i][j-1]+1)))
#     print(l)??????????????

# text = 'hello python'
# str_tuple = list(text)
# print(str_tuple)
# str_tuple[5] = ''
# print(''.join(str_tuple))

# tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
# non_empty_tuples = [i for i in tuples if bool(i)]
# print(non_empty_tuples)
#
# tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
# # new_tuples = []
# # for i in tuples:
# #     i = (list(i[:-1]))
# #     i.append(100)
# #     new_tuples.append(tuple(i))
# # print(new_tuples)
# print([i[:-1]+(100,) for i in tuples])

# poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
# poet_data = poet_data[:2]+('Москва',)
# print(poet_data)

# numbers, l = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10)), []
# for i in numbers:
#     total = 0
#     for j in i:
#         total += j
#
#     l.append(total / len(i))
# print(l)

# def parabola(a,b,c):
#     x = - (b / (2 * a))
#     y = (4 * a * c - b ** 2) / (4 * a)
#     return x, y
# print(parabola(int(input()),int(input()),int(input())))

# marks = [input() for i in range(int(input()))]
# print(*marks, sep='\n')
# print()
# for i in marks:
#     if i[-1] >= str(4):
#         print(i)

# n = int(input())
# f1, f2, f3 = 1, 1, 1
#
# for i in range(n):
#     print(f1, end=' ')
#     f1, f2, f3 = f2, f3, f1+f2+f3

# n,m,k,x,y,z = int(input()), int(input()), int(input()), int(input()),int(input()),int(input())
# total = (n-x)+x+(m-x-y)+y+(k-y)+z
# print(total)

# n, m, k, x, y, z, t, A = int(input()), int(input()), int(input()), int(input()),int(input()),int(input()), int(input()), int(input())
# a = n+m-x-t
# b = n+k-z-t
# c = k+m-y-t
# one_book = n-a-b-t+m-a-c-t+k-b-c-t
# two_books = a+b+c
# no_books = A - one_book-two_books-t
# print(one_book, two_books, no_books, sep='\n')

# my_set = set()
# print(type(my_set))
# my_set = set('')
# print(type(my_set))
# my_set = set([''])
# print(type(my_set))
# my_set = {}
# print(type(my_set))
# my_set = set([])
# print(type(my_set))
# my_set = set(())
# print(type(my_set))

# fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
# sorted_fruits = sorted(fruits, reverse=True)
# print(*sorted_fruits, sep='\n')

# print(len(set(str(input()))))

# txt = input()
# if len(txt) != len(set(txt)):
#     print('NO')
# else:
#     print('YES')

# txt = input()
# print(('n','y')[len(txt) == len(set(txt))])

# string1, string2, total = input(), input(), set('0123456789')
# if set(string1+string2) == total:
#     print('YES')
# else:
#     print('NO')

# string1, string2 = input(), input()
# print('YES' if set(string1) == set(string2) else 'NO')

# string = input().split()
# if set(string[0]) == set(string[1]) == set(string[2]):
#     print('YES')
# else:
#     print('NO')

# l = list()
# strings = [input() for i in range(int(input()))]
# for i in strings:
#     l.append(len(set(i.lower())))
# print(sum(l), sep='\n')

# l = [i.lower().strip('.,;:-?!') for i in input().split()]
# print(len(set(l)))

# numbers, doubles = [int(i) for i in input().split()], set()
# for i in numbers:
#     if i not in set(doubles):
#         print('NO')
#         doubles.add(i)
#     else:
#         print('YES')

# print(len(set(input().split()) & set(input().split())))

# set1 = set([int(i) for i in input().split()])
# set2 = set([int(i) for i in input().split()])
# set3 = set1.intersection(set2)
# set3 = sorted(set3)
# print(*set3)

# print(*sorted(set([int(i) for i in input().split()]) - set([int(i) for i in input().split()])))

# n, myset = int(input()), set(input())
# for i in range(n-1):
#     myset.intersection_update(set(input()))
# print(*sorted(myset))


# print(('YES', 'NO')[set(input()).isdisjoint(set(input()))])

# marks1, marks2, marks3 = set([int(i) for i in input().split()]), set([int(i) for i in input().split()]), set([int(i) for i in input().split()])
# marks1.intersection_update(marks2)
# marks1.difference_update(marks3)
# print(*sorted(marks1, reverse=True))

# set1, set2, set3 = [set(input().split()) for i in range(3)]
# # union_set = marks1.union(marks2)
# # union_set.update(marks3)
# # inter_set = marks1.intersection(marks2)
# # inter_set.intersection_update(marks3)
# # print(*sorted((union_set - inter_set), key=int))
# print(*sorted((set1 | set2 | set3) - (set1 & set2 & set3)))

# set1, set2, set3 = [set(input().split()) for i in range(3)]
# print(*sorted((set3 - set1 - set2), reverse=True, key=int)

# set1, set2, set3 = [set(input().split()) for i in range(3)]
# print(*sorted((set('0123456789') | {'10'}) - (set3 | set1 | set2), key=int))

# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
# print(*sorted({(i.strip('(),.:!?-;')).lower() for i in sentence.split() if len(i.strip('(),.:!?-;')) < 4}))

# files = ['python.png', 'qwerty.py', 'Python.PNg', 'apple.pnG', 'zebra.PNG',  'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git', 'ZeBrA.PnG']
# print(*sorted({i.lower() for i in files if i[-4:].lower() == '.png'}))

# my_dict = {1.12: 'aa', 67.9: 45, 3.11: 'ccc', 7.9: 'dd', 9.2: 'ee', 7.1: 'ff', 0.12: 'qq', 1.91: 'aa', 10.12: [1, 2, 3], 99.0: {9, 0, 1}}
# print(float(min(my_dict))+float(max(my_dict)))

# capitals = {'Россия': 'Москва', 'Англия': 'Лондон', 'Чехия': 'Прага', 'Бразилия':'Бразилиа'}
# for i,j in sorted(capitals.items(), key = lambda x: x[1]):
#     print(j)
# print((capitals.items()))

# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
# l = list()
# for i in users:
#     if i['phone'].endswith('8'):
#         l.append(i['name'])
# print(*sorted(l), end=' ')

# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
#
# l = list()
# for i in users:
#     if 'email' not in i or i['email'] == '':
#         l.append(i['name'])
# print(*sorted(l), end=' ')

# num = 230
# d = {
#     0: "zero",
#     1: "one",
#     2: "two",
#     3: "three",
#     4: "four",
#     5: "five",
#     6: "six",
#     7: "seven",
#     8: "eight",
#     9: "nine"
# }
# # l = list()
# # while num != 0:
# #     l.append(d[num % 10])
# #     num //= 10
# # print(*l[::-1], end=' ')
#
# print(*[d[int(key)] for key in input()])
# txt = input()
# d = {
#     "CS101": "3004, Хайнс, 8:00",
#     "CS102": "4501, Альварадо, 9:00",
#     "CS103": "6755, Рич, 10:00",
#     "NT110": "1244, Берк, 11:00",
#     "CM241": "1411, Ли, 13:00"
# }
# if txt in d:
#     print(f'{txt}:{d[txt]}')

# кнопочный телефон
# txt = 'He said: "I can solve this problem".'
# d = {
#     "1": ".,?!:",
#     "2": "ABC",
#     "3": "DEF",
#     "4": "GHI",
#     "5": "JKL",
#     "6": "MNO",
#     "7": "PQRS",
#     "8": "TUV",
#     "9": "WXYZ",
#     "0": " "
# }
# for i in txt.lower():
#     for k, v in d.items():
#         if i in v.lower():
#             print(k*(v.lower().index(i) + 1), end='')

#Код морзе
# txt = input().upper()
# letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
# morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
# coding = dict(zip(letters, morse))
# decoding = dict(zip(morse, letters))
# for char in txt:
#     if char in letters:
#         print(coding[char], end=' ')

# result = {}
# for i in range(1,16):
#     result[i] = i ** 2
# print(result)
# result = {i: i**2 for i in range(1, 16)}
# print(result)

# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
# result = dict1.copy()
# for i in dict2:
#     result[i] = result.get(i, 0) + dict2[i]
# print(result)

# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
# result = {}
# for i in text:
#     result[i] = result.get(i,0) + 1
# print(result)

# s = ('orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley').split()
# w, l = {}, list()
# for i in s:
#     w[i] = s.count(i)
# for i, j in w.items():
#     if j == max(w.values()):
#         l.append(i)
# print(min(l))
# w = {i : s.count(i) for i in s}
# print(min([i for i,j in w.items() if j == max(w.values())]))

# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]
#
# result = {}
# for i in pets:
#     result[i[1:]] = result.get(i[1:], [])+[i[0]]
# print(result)

# txt = [i.strip('.,!?:;-') for i in input().lower().split()]
# dict1 = {i : txt.count(i) for i in txt}
# print(min([i for i, j in dict1.items() if j == min(dict1.values())]))

# result = {}
# txt = input().split()
# for i in txt:
#     if i in result:
#         print(f'{i}_{result[i]}', end=' ')
#     else:
#         print(i, end=' ')
#     result[i] = result.get(i, 0) + 1
#
# result = {}
# txt = [i for i in input().split()]
# for i in txt:
#     result[i]= result.get(i,-1)+1
#     if result[i] == 0:
#         print(i, end=' ')
#     else:
#         print(f'{i}_{result[i]}', end=' ')
#
# dict1 = {}
# for i in range(int(input())):
#     k,v = input().split(': ')
#     dict1[k.lower()] = v
# list2 = [input() for i in range(int(input()))]
# print([dict1.get(i.lower(), 'Не найдено') for i in list2])
#
# dict_word1 = {'word': sorted([i for i in input()])}
# dict_word2 = {'word': sorted([i for i in input()])}
# print(('NO', 'YES')[dict_word1 == dict_word2])

# def make_dict(word):
#     dict_word = {}
#     for i in word:
#         if i not in '.,!?:;- ':
#             dict_word[i.lower()] = dict_word.get(i, 0) + 1
#     return dict_word
# print(('NO', 'YES')[make_dict(input()) == make_dict(input())])

# dict1 = {}
# for i in range(int(input())):
#     k,v = input().split()
#     dict1[k.capitalize()] = v.capitalize()
# search_txt = input().capitalize()
# for k,v in dict1.items():
#     if search_txt == k:
#         print(v)
#     if search_txt == v:
#         print(k)

# counties_dict = {}
# counties = [input().split() for _ in range(int(input()))]
# for i in counties:
#     counties_dict[i[0]] = i[1:]
# print(counties_dict)
# cities_list = [input() for _ in range(int(input()))]
# print(cities_list)
# for i in cities_list:
#     for k,v in counties_dict.items():
#         if i in v:
#             print(k)

# d = {}
# for _ in range(int(input())):
#     country, *cities = input().split()
#     print(country,cities)
#     d.update(dict.fromkeys(cities, country))
#     print(d)
# for _ in range(int(input())):
#     print(d[input()])
# print(d)

# dict={}
# for _ in range(int(input())):
#     k,v = input().split()
#     dict[v.capitalize()] = dict.get(v,'') +' '+ k
# for _ in range(int(input())):
#     name = input().capitalize()
#     print(dict.get(name, 'абонент не найден'))

# word, word_dict2 = input(), {}
# word_dict = {i:str(word.count(i)) for i in word}
# for _ in range(int(input())):
#     v,k = input().split(': ')
#     word_dict2[k] = v
# for i in word:
#     print(word_dict2[word_dict[i]], end='')

# numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
# result = {i:numbers[i] ** 2 for i in range(len(numbers))}
# favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62, 'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654, 'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271, 'anna': 55, 'madlen': 876}
# result = {k:v for k,v in favorite_numbers.items() if len(str(v)) == 2 }
# import string

# s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
# s, result = s.split(), {}
# for i in s:
#     k,v = i.split(':')
#     result[str(v)] = int(k)
# result = {int(k): v for k, v in [s.split(':') for s in s.split()]}
# numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
# result = {i:[n for n in range(1,i+1) if i % n == 0] for i in numbers}
# words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
# result = {i:[ord(n) for n in i] for i in words}
# letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 26: 'Z'}
# remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
# result = {k:v for k,v in letters.items() if int(k) not in remove_keys}
# students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68), 'Roman': (175, 70), 'Madlen': (160, 50), 'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67), 'Scott': (168, 78), 'John': (186, 79), 'Alex': (195, 120), 'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80), 'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}
# result = {k:v for k,v in students.items() if v[0]>167 and v[1]<75}
# tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24), (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]
# result = {i[0]:tuple(i[1:]) for i in tuples}
# result = {i: (*j,) for i, *j in tuples}
# student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
# student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy']
# student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]
# result=[{a:{b:c}} for a, b, c in zip(student_ids, student_names, student_grades)]
# print(result)

# import random
# n = int(input())
# coin = {0:'Орел', 1:'Решка'}
# print(*[random.choice(coin) for i in range(n)],sep='\n')

# import random
# n = int(input())    # количество попыток
# print(*[random.randint(1,6) for i in range(n)],sep='\n')

# import random
# voc = {'big': [chr(i) for i in range(65,91)], 'small': [chr(i) for i in range(97,123)]}
# password = ''
# n = int(input())
# while len(password) != n:
#     password += random.choice(voc['big']+voc['small'])
# print(password)

# bilet = set()
# while len(bilet) != 7:
#     num = random.choice([i for i in range(1,50)])
#     bilet.add(num)
# print(*sorted(bilet))

# def generate_ip():
#     import random
#     ip_list=random.sample([i for i in range(0,256)],4)
#     return f'{ip_list[0]}.{ip_list[1]}.{ip_list[2]}.{ip_list[3]}'
# print(generate_ip())
# def generate_index():
#     import string, random
#     full_index = list()
#     l = string.ascii_uppercase
#     n = [str(i) for i in range(0,100)]
#     full_index.append(random.choice(l))
#     full_index.append(random.choice(l))
#     full_index.append(random.choice(n))
#     full_index.append('_')
#     full_index.append(random.choice(n))
#     full_index.append(random.choice(l))
#     full_index.append(random.choice(l))
#     return ''.join(full_index)
# print(generate_index())

# import random
# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
# for i in matrix:
#     random.shuffle(i)
# random.shuffle(matrix)
# print(matrix)

# import random, string, time
# from random import randint
# a = time.time()
# # set_1 = set()
# # while len(set_1) != 100:
# #     number = ''.join([random.choice(string.digits) for i in range(7)])
# #     if not number.startswith('0'):
# #         set_1.add(number)
# # print(*set_1, sep='\n')
#
# s=set()
# while len(s)!=100:
#     s.add(randint(1000000,9999999))
# print(*s,sep='\n')
# b = time.time()
# print(b-a)

# import random
# list_txt = [i for i in input()]
# random.shuffle(list_txt)
# print(*list_txt,sep='')

# import random, string
# n, m = int(input()), int(input())
# for i in range(n):
#     pas = list()
#     while len(pas) <= m:
#         pas.append(str(random.choice([x for x in string.digits if x not in '01'])))
#         pas.append(random.choice([x for x in string.ascii_lowercase if x not in 'ol']))
#         pas.append(random.choice([x for x in string.ascii_uppercase if x not in 'OI']))
#     pas = pas[:m]
#     random.shuffle(pas)
#     print(*pas, sep='')


# s = '0.77 4.03 9.06 3.80 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.23 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50'
# s = [Decimal(i) for i in s.split()]
# print(min(s)+max(s))

# s = '9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62 9.85 1.85 1.80 0.83 6.75 9.74 9.11 9.14 5.03 5.03 1.34 3.52 8.09 7.89 8.24 8.23 5.22 0.30 2.59 1.25 6.24 2.14 7.54 5.72 2.75 2.32 2.69 9.32 8.11 4.53 0.80 0.08 9.36 5.22 4.08 3.86 5.56 1.43 8.36 6.29 5.13'
# numbers = [Decimal(i) for i in s.split()]
# print(sum(numbers))
# print(*sorted(numbers, reverse=True)[:5])
# from decimal import *
# num = Decimal('-12.1224') # Decimal(str(input()))
# num_tuple = num.as_tuple().digits
# if abs(num) < 1:
#     mi = 0
# else:
#     mi = min(num_tuple)
# print(max(num_tuple)+mi)
# from decimal import *
# num = Decimal(input())
# print(num.exp() + num.ln() + num.log10() + num.sqrt())

# from fractions import Fraction
# numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67', '0.14', '4.29', '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02', '6.95', '1.62', '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31', '4.63', '7.84', '2.25', '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']
# print(*[f'{i} = {Fraction(i)}' for i in numbers], sep='\n')


# s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'
# numbers = [Fraction(i) for i in s.split()]
# print(min(numbers)+max(numbers))
# m, n = int(input()), int(input())
# print(Fraction(numerator=m, denominator=n))
# num1, num2 = input(), input()
# print(f'{num1} + {num2} = {Fraction(num1)+Fraction(num2)}')
# print(f'{num1} - {num2} = {Fraction(num1)-Fraction(num2)}')
# print(f'{num1} * {num2} = {Fraction(num1)*Fraction(num2)}')
# print(f'{num1} / {num2} = {Fraction(num1)/Fraction(num2)}')
# s = 0
# for i in range(1, int(input()) + 1):
#     s += Fraction(1, (i ** 2))
# print(s)
# from time import time
# a = time()
# from fractions import Fraction
# from math import *
# s, f = 0, 1
# for i in range(1, int(input()) + 1):
#     s += Fraction(1, (factorial(i)))
# # for i in range(1, int(input())+1):
# #     f *= i
# #     s += Fraction(1, f)
# print(s)
# b = time()
# print(b-a)

# def matrix(n=1, m=None, value=0):
#     if m == None:
#         m=n
#     return [[value]*m for _ in range(n)]
# print(matrix(3, 4, 9))
#
# def f(n=3):
#     return n + 7
# print(f(f(f())))

# def count_args(*args):
#     return len(args)
# print(count_args())

# def sq_sum(*args):
#     s = 0
#     for i in args:
#         s += i ** 2
#     return s
# print(sq_sum(1.5, 2.5))

# def mean(*args):
#     s, c = 0, 0
#     for i in args:
#         if type(i) == int or type(i) == float:
#             s += i
#             c += 1
#     if c == 0:
#         return 0.0
#     else:
#         return s / c
#
# print(mean())
# print(mean(7))
# print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
# print(mean(True, ['stepik'], 'beegeek', (1, 2)))
# print(mean(-1, 2, 3, 10, ('5')))
# print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# def greet(name, *args):
#     name_list = (name,) + args
#     return 'Hello ' + ' and '.join(name_list) + '!'
#
# def greet(name, *args):
#     if len(args) > 0:
#         for i in args:
#             name = name + ' and ' + i
#     return f'Hello, {name}!'

# def print_products(*args):
#     c = 0
#     for i in args:
#         if type(i) == str and i != '':
#             c += 1
#             print(f'{c}) {i}')
#     if c == 0:
#         print('Нет продуктов')
# print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
# print()
# print_products([4], {}, 1, 2, {'Beegeek'}, '')

# def info_kwargs(**kwargs):
#     print(*sorted({f'{k}: {v}' for k,v in kwargs.items()}), sep='\n')
# info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')

