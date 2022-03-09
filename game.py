# import random
#
#
# def hello():
#     category_list = ['Домашние животные - 1', 'Дни недели - 2', 'Месяцы года - 3', 'Планеты солнечной системы - 4', 'ВСЕ ТЕМЫ - 9','Хочу выйти из игры - 0']
#     word_list_animals = ['СОБАКА', 'КОШКА', 'ХОМЯК', 'КРОЛИК', 'КРЫСА', 'ЧЕРЕПАХА', 'ЗМЕЯ', 'ПОПУГАЙ']
#     word_list_days = ['ПОНЕДЕЛЬНИК', 'ВТОРНИК', 'СРЕДА', 'ЧЕТВЕРГ', 'ПЯТНИЦА', 'СУББОТА', 'ВОСКРЕСЕНЬЕ', ]
#     word_list_months = ['ЯНВАРЬ', 'ФЕВРАЛЬ', 'МАРТ', 'АПРЕЛЬ', 'МАЙ', 'ИЮНЬ', 'ИЮЛЬ', 'АВГУСТ', 'СЕНТЯБРЬ', 'ОКТЯБРЬ', 'НОЯБРЬ', 'ДЕКАБРЬ']
#     word_list_planets = ['МЕРКУРИЙ', 'ВЕНЕРА', 'ЗЕМЛЯ', 'МАРС', 'ЮПИТЕР', 'САТУРН', 'УРАН', 'НЕПТУН']
#     all_lists = word_list_planets + word_list_months + word_list_days + word_list_animals
#     print(f'Доступные темы для игры: {category_list}')
#     category_number = int(input('Выбери тему для игры: \n'))
#     if category_number == 1:
#         return random.choice(word_list_animals).upper(), 'Домашние животные'
#     elif category_number == 2:
#         return random.choice(word_list_days).upper(), 'Дни недели'
#     elif category_number == 3:
#         return random.choice(word_list_months).upper(), 'Месяцы года'
#     elif category_number == 4:
#         return random.choice(word_list_planets).upper(), 'Планеты солнечной системы'
#     elif category_number == 0:
#         return exit, exit
#     elif category_number == 9:
#         return random.choice(all_lists).upper(), 'Компьютер сам не знает тему загадок...'
#     all_lists.clear()
#
#
# def continue_game(num):
#     if num == 0:
#         return exit
#     else:
#         return 1
#
#
# def display_hangman(tries):
#     stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
#         '''
#            --------
#            |      |
#            |      O
#            |     \\|/
#            |      |
#            |     / \\
#         -------
#         ''',
#         # голова, торс, обе руки, одна нога
#         '''
#            --------
#            |      |
#            |      O
#            |     \\|/
#            |      |
#            |     /
#         -------
#         ''',
#         # голова, торс, обе руки
#         '''
#            --------
#            |      |
#            |      O
#            |     \\|/
#            |      |
#            |
#         -------
#         ''',
#         # голова, торс и одна рука
#         '''
#            --------
#            |      |
#            |      O
#            |     \\|
#            |      |
#            |
#         -------
#         ''',
#         # голова и торс
#         '''
#            --------
#            |      |
#            |      O
#            |      |
#            |      |
#            |
#         -------
#         ''',
#         # голова
#         '''
#            --------
#            |      |
#            |      O
#            |
#            |
#            |
#         -------
#         ''',
#         # начальное состояние
#         '''
#            --------
#            |      |
#            |
#            |
#            |
#            |
#         -------
#         '''
#     ]
#     return stages[tries]
#
#
# def guess_check(text, word, tries, guessed_words, guessed_letters):
#     if len(text) > len(word):
#         return guess_check(input('Ваше слово длиннее, чем загаданное. Попробуйте еще раз. \n'), word, tries, guessed_words, guessed_letters)
#     elif len(text) == 1:
#         if text.lower() not in 'йцукеёнгшщзхъфывапролджэячсмитьбю':
#             return guess_check(input('Пишите буквами русского алфавита! \n'), word, tries, guessed_words, guessed_letters)
#         if text in guessed_letters:
#             return guess_check(input('Это вы уже пробовали и не угадали. Попробуйте что-то другое. \n '), word, tries, guessed_words, guessed_letters)
#         else:
#             guessed_letters.append(text)
#             tries -= 1
#             return text, tries, guessed_words, guessed_letters
#     elif len(text) == len(word):
#         for i in text:
#             if i not in 'йцукеёнгшщзхъфывапролджэячсмитьбю':
#                 return guess_check(input('Пишите буквами русского алфавита! \n'), word, tries, guessed_words, guessed_letters)
#         if text in guessed_words:
#             return guess_check(input('Это вы уже пробовали и не угадали. Попробуйте что-то другое. \n'), word, tries, guessed_words, guessed_letters)
#         else:
#             guessed_words.append(text)
#             tries -= 1
#             return text, tries, guessed_words, guessed_letters
#
#
# def play(word, theme):
#     guessed_letters = []
#     guessed_words = []
#     word_completion = '_' * len(word)
#     tries = 6
#     word_out = ''
#     while word_completion != word and tries >= 0:
#         print(f'У вас {tries} попыток(и). Тема загадки - {theme}', display_hangman(tries), word_completion, sep='\n')
#         letter_word, tries, guessed_words, guessed_letters = guess_check(input('Введите букву или слово целиком: \n'), word, tries, guessed_words, guessed_letters)
#         if letter_word.upper() == word:
#             print('Ура! Поздравляем! Вы угадали слово! \n')
#             return continue_game(int(input('Хочешь продолжить - 1 или выйти из игры - 0 \n')))
#         else:
#             for i in range(len(word)):
#                 if word[i] == letter_word.upper():
#                     word_out += letter_word.upper()
#                 elif word[i] == word_completion[i]:
#                     word_out += word_completion[i]
#                 else:
#                     word_out += '_'
#         word_completion = word_out
#         word_out = ''
#     print(f'Вы не угадали. А слово это было - {word}.')
#     return continue_game(int(input('Хочешь продолжить - 1 или выйти из игры - 0 ? \n')))
#
#
# print('Добро пожаловать в игру "Угадай слово".')
# print('Жми цифру для выбора и "ENTER".')
# print('Для написания слов и букв используй русский алфавит.')
# print()
# word, theme = 1, 1
# while theme != exit:
#     word, theme = hello()
#     if theme != exit:
#         print(f'Играем по теме "{theme}".')
#     else:
#         break
#     theme = play(word, theme)
# print('До скорой встречи!')