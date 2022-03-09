# # def draw_box():
# #     # size = [int(input()) for i in range(2)]
# #     # print('*' * size[-1])
# #     # for i in range(size[0]-2):
# #     #     print('*'+' ' * (size[-1]-2)+'*', sep='')
# #     # print('*' * size[-1])
# #     for i in range(10):
# #         print('*' * i, sep='')
# # draw_box()
#
# # def draw_box(height, width):
# #     height = 2
# #     width = 10
# #     for i in range(height):
# #         print('*' * width)
# #
# # n = 5
# # m = 7
# # draw_box(2, 4)
# # print(n, m)
#
# # # объявление функции
# # def draw_triangle(fill, base):
# #                                             #for i in range(1, base + 1):      print(fill * min(i, base - i + 1))
# #     for i in range(base//2+1):
# #         for j in range(i+1):
# #             print(fill, end='')
# #         print()
# #     for i in range(base//2,0,-1):
# #         for j in range(i):
# #             print(fill, end='')
# #         print()
# # # считываем данные
# # fill = input()
# # base = int(input())
# # # вызываем функцию
# # draw_triangle(fill, base)
#
# # # объявление функции
# # def print_fio(name, surname, patronymic):
# #     print(*[surname[0].upper(), name[0].upper(), patronymic[0].upper()], sep='')
# # # считываем данные
# # name, surname, patronymic = input(), input(), input()
# # # вызываем функцию
# # print_fio(name, surname, patronymic)
#
# # def print_digit_sum(num):
# #     s = 0
# #     while num != 0:
# #         l = num % 10
# #         s += l
# #         num //= 10
# #     print(s)
#
# # # считываем данные
# # n = int(input())
# #
# # # print_digit_sum(n)
# #
# # def is_prime(num):
# #     c = 0
# #     for i in range(1, num+1):
# #         if num % i == 0:
# #             c += 1
# #     if c == 1 or c > 2:
# #         return False
# #     else:
# #         return True
# # def is_prime(num):
# #     return len([i for i in range(1, num+1) if num % i == 0]) == 2
#
# # def is_prime(num):
# #     if num == 1:
# #         return False
# #     return len([i for i in range(2, int(num ** 0.5) + 1) if num % i == 0]) == 0
#
# # n = int(input())
# # print(is_prime(n))
#
# # def is_prime(num):
# #     c = 0
# #     for i in range(1, num+1):
# #         if num % i == 0:
# #             c += 1
# #     if c == 1 or c > 2:
# #         return True
# #     else:
# #         return False,
# # def get_next_prime(num):
# #     num += 1
# #     while is_prime(num) == True:
# #         num += 1
# #     return num
# # n = int(input())
# # print(get_next_prime(n))
#
#
# # def is_password_good(password):
# #     up = lo = dig = l = 0
# #     if len(password) >= 8:
# #         l += 1
# #     for i in password:
# #         if i.isupper() == True:
# #             up += 1
# #         if i.islower() == True:
# #             lo += 1
# #         if i.isdigit() == True:
# #             dig += 1
# #     if dig*up*lo*l == 0:
# #         return False
# #     return True
# # txt = str(input())
# # print(is_password_good(txt))
#
# # def is_one_away(word1, word2):
# #     if len(word1) != len(word2):
# #         return False
# #     c = 0
# #     for i in range(len(word1)):
# #         if word1[i] != word2[i]:
# #             c += 1
# #     if c == 0 or c > 1:
# #         return False
# #     return True
# # txt1 = input()
# # txt2 = input()
# # print(is_one_away(txt1, txt2))
#
# # def is_palindrome(text):
# #     l, text = list(), text.lower()
# #     for i in text:
# #         if i in 'qwertyuiopasdfghjklzxcvbnm' or i in 'йцукенгшщзхъфывапролджэячсмитьбю':
# #             l.append(i)
# #     return l[:] == l[::-1]
# # txt = input()
# # print(is_palindrome(txt))
#
# # def is_prime(num):
# #     c = 0
# #     for i in range(1, num+1):
# #         if num % i == 0:
# #             c += 1
# #     if c == 1 or c > 2:
# #         return False
# #     else:
# #         return True
# #
# # def is_valid_password(password):
# #     p = psw.split(sep=':')
# #     if len(p) != 3:
# #         return False
# #     if p[0] != p[0][::-1]:
# #         return False
# #     if is_prime(int(p[1])) == False:
# #         return False
# #     return int(p[2]) % 2 == 0
# #
# # def is_valid_password(password):
# #     password = password.split(':')
# #     return (password[0] == password[0][::-1]) and (len([i for i in range(1, int(password[1])+1) if int(password[1]) % i == 0]) == 2) and (int(password[2]) % 2 == 0)
# #
# # psw = input()
# # print(is_valid_password(psw))
#
# # def is_correct_bracket(text):
# #     if len(text) % 2 != 0 or text[0] == ')' or text[-1] == '(':
# #         return False
# #     o = 0
# #     for i in text:
# #         if i == '(':
# #             o += 1
# #         if i == ')':
# #             o -= 1
# #         if o < 0:
# #             return False
# #     return o == 0
# # print(is_correct_bracket(input()))
#
# # def convert_to_python_case(text):
# #     i = 0
# #     while i < len(text) - 1:
# #         i += 1
# #         if text[i].isupper():
# #             text = text[:i] + '_' + text[i:]
# #             i += 1
# #     return text.lower()
# # print(convert_to_python_case(input()))
#
#
# # def get_middle_point(x1, y1, x2, y2):
# #     x = (x1 + x2)/2
# #     y = (y1 + y2)/2
# #     return x, y
# #
# # x_1, y_1 = int(input()), int(input())
# # x_2, y_2 = int(input()), int(input())
# #
# # x, y = get_middle_point(x_1, y_1, x_2, y_2)
# # print(x, y)
# #
#
# # def get_circle(radius):
# #     from math import pi
# #     c = 2 * pi * radius
# #     s = pi * (radius ** 2)
# #     return c, s
# #
# # length, square = get_circle(float(input()))
# # print(length, square)
#
# def solve(a, b, c):
#     d = b ** 2 - 4 * a * c
#     if d > 0:
#         x1 = (-b - d ** 0.5) / (2 * a)
#         x2 = (-b + d ** 0.5) / (2 * a)
#         return min(x1, x2), max(x1, x2)
#     elif d == 0:
#         x = -b / (2 * a)
#         return x, x
#     # elif d == 0:
#     #     x = -b / (2 * a)
#     #     return x
# x1, x2 = solve(int(input()), int(input()), int(input()))
# print(x1, x2)

# from math import log, ceil
#
# s = log(int(input()), 2)
# print(ceil(s))

# n = int(input())
# c = 0
# while n != 1:
#     if n % 2 != 0:
#         n += 1
#     n //= 2
#     c += 1
# print(c)
# # Угадай число
# l, h, c, q, press = int(input()), int(input()), 0, int(input()), -1
# midlle = (l+h) // 2
# while press != 'q':
#     if l <= q < midlle:
#        h = midlle
#     if midlle < q <= h:
#        l = midlle + 1
#     midlle = (l+h) // 2
#     c += 1
#     if midlle == q:
#         break
#     print('Your number is -', midlle)
#     press = input('press "Enter" for next number or "q" to quit''\n')
# print(f'Your number is - {midlle}. Tries - {c}')

# import random             #First game Guess the number
#
# q_num = random.randint(1, 100)
# print('Добро пожаловать в числовую угадайку')
#
# def is_valid(num):
#     if num.isdigit() and 1 <= int(num) <= 100:
#         return int(num)
#     else:
#         return is_valid(input('А может быть все-таки введем целое число от 1 до 100? \n'))
#
#
# def game_compare(num):
#     if num < q_num:
#         return 'Ваше число меньше загаданного, попробуйте еще разок'
#     elif num > q_num:
#         return 'Ваше число больше загаданного, попробуйте еще разок'
#     elif num == q_num:
#         return 'Вы угадали, поздравляем!'
#
#
# def game_continue():
#     asc = input('Хотите продолжить? y(д) or n(н) \n')
#     while True:
#         if asc not in 'ynдн':
#             asc = input('Ответь правильно y(д) or n(н) \n')
#         if asc in 'yд':
#             return True
#         if asc in 'nн':
#             return False
# c = 1
# while True:
#     num = is_valid(input('Введите число от 1 до 100 \n'))
#     print(game_compare(num), f'Попыток угадать - {c}')
#     if game_continue():
#         c += 1
#         continue
#     else:
#         print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
#         break

# import random                   #game magic ball
# answers = ['Бесспорно',	'Мне кажется - да',	'Пока неясно, попробуй снова', 'Даже не думай', 'Предрешено', 'Вероятнее всего', 'Спроси позже', 'Мой ответ - нет', 'Никаких сомнений', 'Хорошие перспективы', 'Лучше не рассказывать', 'По моим данным - нет', 'Определённо да', 'Знаки говорят - да', 'Сейчас нельзя предсказать', 'Перспективы не очень хорошие', 'Можешь быть уверен в этом', 'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно']
#
# def hello():
#     print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
#     user_name = input('Как тебя зовут? \n')
#     print(f'Привет {user_name}')
#
# def question(text):
#     pass
#
# def answer():
#     return random.choice(answers)
#
# def continue_game():
#     asc = input('Хочешь спросить еще что-нибудь? y(д) or n(н) \n')
#     while True:
#         if asc not in 'ynдн':
#             asc = input('Попади по клавишам. y(д) or n(н) \n')
#         if asc in 'yд':
#             return True
#         if asc in 'nн':
#             return False
#
# hello()
# while True:
#     question(input('Напиши свой вопрос, на который можно ответить Да или Нет \n' ))
#     print(f'Мой ответ такой: -{answer()}')
#     if continue_game():
#         continue
#     else:
#         print('Возвращайся, если возникнут вопросы!')
#         break

# password generator
# import random
#
# digits = '0123456789'
# lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
# uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# punctuation = '!#$%&*+-=?@^_'
# rare = 'il1Lo0O'
# chars = ''
# pass_number = int(input('Количество паролей для генерации \n'))
# pass_length = int(input('Длину одного пароля \n'))
# add_num = input('Включать ли цифры 0123456789 \n')
# add_cap = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ \n')
# add_low = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? \n')
# add_spec = input('Включать ли символы !#$%&*+-=?@^_? \n')
# remove_rare = input('Исключать ли неоднозначные символы il1Lo0O? \n')
#
# def generate_pass(text):
#     return random.choice(text)
#
#
# if add_num in 'yд':
#     chars += digits
# if add_cap in 'yд':
#     chars += uppercase_letters
# if add_low in 'yд':
#     chars += lowercase_letters
# if add_spec in 'yд':
#     chars += punctuation
# if remove_rare in 'yд':
#     for i in rare:
#         chars = chars.replace(i, random.choice(digits))
# for i in range(pass_number):
#     l = list()
#     while len(l) != pass_length:
#         l.append(generate_pass(chars))
#     print(*l, sep='')

# шифр цезаря

# def coding(alfabet, step, text):
#     text_out = ''
#     for i in text:
#         if i in alfabet:
#             text_out += alfabet[(alfabet.index(i) + step) % len(alfabet)]
#         elif i.lower() in alfabet:
#             text_out += alfabet[(alfabet.index(i.lower()) + step) % len(alfabet)].upper()
#         else:
#             text_out += i
#     return text_out
#
# def decoding(alfabet, step, text):
#     text_out = ''
#     for i in text:
#         if i in alfabet:
#             text_out += alfabet[(alfabet.index(i) - step) % len(alfabet)]
#         elif i.lower() in alfabet:
#             text_out += alfabet[(alfabet.index(i.lower()) - step) % len(alfabet)].upper()
#         else:
#             text_out += i
#     return text_out
#
# def full_decoding(alfabet, text):
#     l = list()
#     for i in range(0, 26):
#         text_out = (decoding(alfabet, i, text))
#         l.append(text_out)
#     return l
#
# while True:
#     intro = int(input('rabotaem - 1 ili vahodim - 2 \n'))
#     if intro == 1:
#         print('rabotaem')
#         while True:
#             direction = int(input('1 - coding, 2 - decoding, 3 - fulldecoding \n'))
#             alfabet = int(input('1 - for english, 2 - for russian \n'))
#             if alfabet == 1:
#                 alfabet = [chr(i) for i in range(97, 123)]
#             if alfabet == 2:
#                 alfabet = [chr(i) for i in range(1072, 1104)]
#             step = int(input('step for coding/decoding \n'))
#             text = str(input('enter the text \n'))
#             if direction == 1:
#                 print(coding(alfabet, step, text))
#             if direction == 2:
#                 print(decoding(alfabet, step, text))
#             if direction == 3:
#                 print(*full_decoding(alfabet, text), sep='\n')
#             print()
#             break
#         continue
#     if intro == 2:
#         print('Good bye')
#     break

# def coding(step, text):
#     alfabet = [chr(i) for i in range(97, 123)]
#     text_out = ''
#     for i in text:
#         if i in alfabet:
#             text_out += alfabet[(alfabet.index(i) + step) % len(alfabet)]
#         elif i.lower() in alfabet:
#             text_out += alfabet[(alfabet.index(i.lower()) + step) % len(alfabet)].upper()
#         else:
#             text_out += i
#     return text_out
#
# text, coded_text = str(input()).split(), list()
# for i in text:
#     c = 0
#     for j in i:
#         if j.isalpha():
#             c += 1
#     coded_text.append(coding(c, i))
# print(*coded_text)

# num = int(input())
# print(bin(num)[2:], oct(num)[2:], hex(num)[2:].upper(), sep='\n')



