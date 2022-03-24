# text = '''Пример текста,
# состоящего из нескольких строк.
# Здесь не нужно экранировать одинарные кавычки ' и двойные "
# '''
# print(text)

# king = 'King Balon the 6th'
# rooms_per_casle = 17
# casels = 6
# # BEGIN (write your solution here)
# total_rooms = rooms_per_casle * casels
# # END
# print(f"{king} has {total_rooms} rooms.")

# magic = '\nyou'
# print(magic)
# print(magic[1])

# one = 'Naharis'
# two = 'Mormont'
# three = 'Sand'
# text = one[2] + two[1] + three[3] + two[4] + two[2]
# # BEGIN (write your solution here)
# print(text)
# # END

# from random import random
# # BEGIN (write your solution here)
# print(int(random() * 9) + 1)
# # END

# print(print())

# from datetime import date
# # BEGIN (write your solution here)
# def get_current_year():
#     current_year = int(str(date.today())[0:4])
#     return current_year
# # END
# print(get_current_year())

# def get_hidden_card(number, repeat=4):
#     return '*' * repeat + number[-4:]
# print(get_hidden_card('2034399002121100'))

# def has_upper_case(string):
#     return string[0] != string.lower()[0]
# print(has_upper_case("hexlet"))
# def ddd(temperature):
#     if temperature > 10:
#         return temperature
#     else:
#         return 0
# print(ddd(10))

# def normalize_url(text):
#     prefix = text[:7]
#     end = text[7:]
#     if prefix == 'https:/':
#         return text
#     elif prefix == 'http://':
#         return f'https://{end}'
#     else:
#         return f'https://{text}'
#
# print(normalize_url('АДРЕС'))

# def join_numbers_from_range(start, finish):
#     i = start
#     string = ''
#     while i <= finish:
#         string += str(i)
#         i += 1
#     return string
#
# print(join_numbers_from_range(5,10))

# def encrypt(text):
#     i = 0
#     encrypted_text = ''
#     if len(text) % 2 != 0:
#         end = text[-1]
#         text = text[:(len(text)-1)]
#     else:                                                       # nextChar = "" if (i + 1 >= len(text)) else text[i + 1]
#                                                                     # result = result + nextChar + text[i]
#         end = ''
#     while i < len(text):
#         encrypted_text += text[i+1] + text[i]
#         i += 2
#     return encrypted_text + end
#
# print(encrypt("move"))

# def filter_string(text, char):
#     new_text = ''
#     for i in text:
#         if i.lower() == char.lower():
#             i = ''
#         new_text += i
#     return new_text
#
# print(filter_string('I look back if you are lost', 'o'))

# def is_palindrome(text):
#     new_text = ''
#     for i in text:
#         new_text = i + new_text
#     return text == new_text
#
# print(is_palindrome('radar'))
# print(is_palindrome('abs'))

# from symbols import is_vowel
# def count_vowels(string):
#     counter = 0
#     for i in string:
#         if i.is_vowel():
#             counter += 1
#     return counter

# BEGIN (write your solution here)
# def sort_pair(numbers):
#     num1, num2 = (numbers)
#     return (num1, num2) if num2 >= num1 else (num2, num1)
# # END
# print(sort_pair((5, 1)))
# print(sort_pair((7, 8)))

# class MoneyBox:
#     def __init__(self, capacity, val=0):
#         self.capacity = capacity
#         self.val = val
#     def can_add(self, v):
#         return self.val + v <= self.capacity
#     def add(self, v):
#         self.val += v

# class Buffer:
#     def __init__(self):
#         # конструктор без аргументов
#         self.l = list()
#
#     def add(self, *a):
#         # добавить следующую часть последовательности
#
#         for i in a:
#             l.append()
#
#     def get_current_part(self):
#         # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены
#         return self.l[:4]
#
# buf = Buffer()
# buf.add(1, 2, 3)
# buf.get_current_part() # вернуть [1, 2, 3]
# buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
# buf.get_current_part() # вернуть [6]
# buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
# buf.get_current_part() # вернуть []
# buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
# buf.get_current_part() # вернуть [1]


# def counter_add(num):
#     def add():
#         return num + 5
#     return add
# k = int(input())
# cnt = counter_add(k)
# print(cnt())

# def counter_add(n):
#     def add(k):
#         k += n
#         return k
#     return add
# k = int(input())
# cnt = counter_add(2)
# print(cnt(k))
# print(cnt(k))
# print(cnt(k))

# def tag_func(text):
#     def make_tag():
#         return f'<h1>{text}</h1>'
#     return make_tag
# s = str(input())
# tag = tag_func(s)
# print(tag())

# def tag_func(t):
#     def make_tag(text):
#         return f'<{t}>{text}</{t}>'
#     return make_tag
# tag = str(input())
# string = str(input())
# tag_string = tag_func(tag)
# print(tag_string(string))

# def type_func(tp):
#     def make(text):
#         string_list = [int(i) for i in text.strip().split()]
#         return string_list if tp == 'list' else tuple(string_list)
#     return make
# tp = str(input())
# string = str(input())
# list_or_tuple = type_func(tp)
# print(list_or_tuple(string))

# def foo():
#     return 2 / 0
# try:
#     foo()
# except (ArithmeticError, AssertionError) as error:
#     print(type(error).__name__)

class Buffer:
    def __init__(self):
        # конструктор без аргументов
        self.lst = list()


    def add(self, *a):
        # добавить следующую часть последовательности
        [self.lst.append(i) for i in a]
        while len(self.lst) >= 5:
            print(sum(self.lst[0:5]))
            self.lst = self.lst[5:]


    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены
        print(self.lst)
        return self.lst

buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]