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