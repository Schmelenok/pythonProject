# DATABASE = {
#     'Серёга': 'Омск',
#     'Соня': 'Москва',
#     'Миша': 'Москва',
#     'Дима': 'Челябинск',
#     'Алина': 'Красноярск',
#     'Егор': 'Пермь',
#     'Коля': 'Красноярск'
# }
#
#
# def process_query(query):
#     query_list = query.split(', ')
#     name, query = query_list[0], query_list[1]
#     if name == 'Анфиса':
#         return process_anfisa(query)
#     else:
#         return process_friend(name, query)
#
#
# def process_friend(name, query):
#     if name in DATABASE:
#         if query == 'ты где?':
#             return f'{name} в городе {DATABASE[name]}'
#         else:
#             return '<неизвестный запрос>'
#     else:
#         return f'У тебя нет друга по имени {name}'
#
#
# def format_friends_count(friends_count):
#     if friends_count == 1:
#         return '1 друг'
#     elif 2 <= friends_count <= 4:
#         return f'{friends_count} друга'
#     else:
#         return f'{friends_count} друзей'
#
#
# def process_anfisa(query):
#     if query == 'сколько у меня друзей?':
#         count = len(DATABASE)
#         return f'У тебя {format_friends_count(count)}.'
#     elif query == 'кто все мои друзья?':
#         friends_string = ', '.join(DATABASE)
#         return f'Твои друзья: {friends_string}'
#     elif query == 'где все мои друзья?':
#         unique_cities = set(DATABASE.values())
#         cities_string = ', '.join(unique_cities)
#         return f'Твои друзья в городах: {cities_string}'
#     else:
#         return '<неизвестный запрос>'
#
#
# print('Привет, я Анфиса!')
# print(process_query('Анфиса, сколько у меня друзей?'))
# print(process_query('Анфиса, кто все мои друзья?'))
# print(process_query('Анфиса, где все мои друзья?'))
# print(process_query('Анфиса, кто виноват?'))
# print(process_query('Соня, ты где?'))
# print(process_query('Коля, что делать?'))
# print(process_query('Антон, ты где?'))

# import datetime as dt
# start_moment = dt.datetime(2022, 3, 1, 20, 0)  # Напишите код здесь
# current_moment = dt.datetime(2022, 3, 15, 17, 30)  # и здесь
# total_time = current_moment - start_moment  # и здесь
# print(total_time)

# import datetime as dt
# utc_time = dt.datetime.utcnow()
# print(utc_time)
#
# def what_time(city):
#     return dt.datetime.utcnow() + dt.timedelta(hours = UTC_OFFSET[city])

# import datetime as dt
#
#
# DATABASE = {
#     'Серёга': 'Омск',
#     'Соня': 'Москва',
#     'Дима': 'Челябинск',
#     'Алина': 'Красноярск',
#     'Егор': 'Пермь'
# }
#
# UTC_OFFSET = {
#     'Санкт-Петербург': 3,
#     'Москва': 3,
#     'Самара': 4,
#     'Новосибирск': 7,
#     'Екатеринбург': 5,
#     'Нижний Новгород': 3,
#     'Казань': 3,
#     'Челябинск': 5,
#     'Омск': 6,
#     'Ростов-на-Дону': 3,
#     'Уфа': 5,
#     'Красноярск': 7,
#     'Пермь': 5,
#     'Воронеж': 3,
#     'Волгоград': 4,
#     'Краснодар': 3,
#     'Калининград': 2
# }
#
#
# def what_time(friend):
#     utc_time = dt.datetime.utcnow()
#     city = DATABASE[friend]
#     return (utc_time + dt.timedelta(hours=UTC_OFFSET[city])).strftime('%H:%M')
#
#
#
# print(what_time('Соня'))

# import requests
# url = 'http://wttr.in/'
# cities = {'poznan': 'Poznan',
#           'gdansk': 'Gdansk'
# }
# weather_parameters = {
#     '0': '',
#     'T': '',  # добавьте параметр запроса `T`, чтобы вернулся чёрно-белый текст
#     'M': '',
#     'lang': 'ru'
# }
# url = url + cities[input()] +'?'
# response = requests.get(url, params=weather_parameters)  # выполните HTTP-запрос
# print(response.text)

# import requests
# cities = [
#     'Омск',
#     'Калининград',
#     'Челябинск',
#     'Владивосток',
#     'Красноярск',
#     'Москва',
#     'Екатеринбург'
# ]
# def make_url(city):
#     # в URL задаём город, в котором узнаем погоду
#     return f'http://wttr.in/{city}'
# def make_parameters():
#     params = {
#         'format': 2,  # погода одной строкой
#         'M': ''  # скорость ветра в "м/с"
#     }
#     return params
# def what_weather(city):
#     # Напишите тело этой функции.
#     # Не изменяйте остальной код!
#     try:
#         response = requests.get(make_url(city), params=make_parameters())
#     except requests.ConnectionError:
#         print('<сетевая ошибка>')
#     except response.status_code != 200:
#         print('<ошибка на сервере погоды>')
#     return response.text
# print('Погода в городах:')
# for city in cities:
#     print(city, what_weather(city))


# min_required_area = 40 # минимальная требуемая площадь
# max_affordable_price = 190000 # максимально допустимая арендная ставка
# third_ring_radius = 6.7 # максимальное расстояние от центра
#
# open_hours_number = 18 # количество рабочих часов в сутки
# traffic2visitors_average_ratio = 1 / 225 # средняя доля посетителей от числа прохожих
# traffic2visitors_pessimistic_ratio = 1 / 300 # минимальная доля посетителей от числа прохожих
# visitors2purchases_average_ratio = 0.1 # средняя доля покупателей от числа посетителей
# visitors2purchases_pessimistic_ratio = 0.05 # минимальная доля покупателей от числа посетителей
# average_order_value = 21000 # средняя стоимость покупки
# average_order_value_pessimistic = 20000 # минимальная стоимость покупки
# trade_margin = 0.2 # наценка
# days_in_months = 30 # количество рабочих дней в месяц
#
# # множитель для расчёта прибыльности в среднем сценарии
# income_multiplier_average = (open_hours_number *
#                              traffic2visitors_average_ratio *
#                              visitors2purchases_average_ratio *
#                              average_order_value *
#                              trade_margin *
#                              days_in_months)
#
# # множитель для расчёта прибыльности в пессимистичном сценарии
# income_multiplier_pessimistic = (open_hours_number *
#                                  traffic2visitors_pessimistic_ratio *
#                                  visitors2purchases_pessimistic_ratio *
#                                  average_order_value_pessimistic *
#                                  trade_margin *
#                                  days_in_months)
#
# number_of_employees = 2 # количество продавцов
# employee_salary = 50000 # зарплата продавца
# tax_multiplier = 1.43 # множитель для расчёта зарплаты с налогами
#
# # зарплатная часть расходов
# addition_to_expenses = number_of_employees * employee_salary * tax_multiplier
#
# # минимальная ожидаемая прибыль
# min_expected_profits = 500000
#
# import pandas
# realty_df = pandas.read_csv('yandex_realty_data.csv')
#
# filtered_objects_area = []
# filtered_objects_price = []
# filtered_objects_traffic = []
# filtered_objects_address = []
# filtered_objects_profits = []
#
# for index in range(len(realty_df)):
#     if (realty_df['floor'][index] == 1 and
#         realty_df['area'][index] >= min_required_area and
#         realty_df['price'][index] <= max_affordable_price and
#         realty_df['commercial_type'][index] in ['FREE_PURPOSE', 'RETAIL'] and
#         realty_df['distance'][index] <= third_ring_radius and
#         realty_df['already_taken'][index] == 0 and
#         realty_df['competitors'][index] <= 1):
#         filtered_objects_area.append(realty_df['area'][index])
#         filtered_objects_price.append(realty_df['price'][index])
#         filtered_objects_traffic.append(realty_df['traffic'][index])
#         filtered_objects_address.append(realty_df['address'][index])
#         filtered_objects_profits.append(realty_df['traffic'][index] *
#         income_multiplier_average - (realty_df['price'][index] +
#         addition_to_expenses))
#
# for index in range(len(filtered_objects_profits)):
#     if filtered_objects_profits[index] > min_expected_profits:
#         print(filtered_objects_price[index])
#         print(filtered_objects_traffic[index])
#         print(filtered_objects_address[index])
#         print(filtered_objects_profits[index])
#         print(filtered_objects_traffic[index] * income_multiplier_pessimistic -
#         (filtered_objects_price[index] + addition_to_expenses))
#         print('----------')


# import pandas
# import seaborn
#
# data = pandas.read_csv('support_data.csv')
#
# # названия сегментов и интервалов
# segments_old = ['Segment 0', 'Segment 1', 'Segment 2']
# segments_new = ['Потенциальные клиенты', 'Обычные клиенты', 'VIP-клиенты']
# intervals = ['До внедрения роботов', 'После внедрения роботов']
#
# intervals_column = list(data['interval'])
# segments_column = list(data['segment']) # ваш код здесь
# score_column = list(data['score']) # ваш код здесь

# # средние оценки
# mean_scores = []
# for segment in segments_old:
#
#     # допишите код
#     before_score, before_counter, after_counter, after_score = 0, 0, 0, 0
#     for index in range(len(data)):
#         if segments_column[index] == segment:
#             if intervals_column[index] == 'До внедрения роботов':
#                 before_score += score_column[index]
#                 before_counter += 1  # допишите код
#             if intervals_column[index] == 'После внедрения роботов':
#                 after_score += score_column[index]
#                 after_counter += 1
#
#         # допишите код
#
#     segment_scores = [before_score / before_counter, after_score / after_counter]  # допишите код
#     mean_scores.append(segment_scores)
#
# seaborn.heatmap(mean_scores, xticklabels=intervals, yticklabels=segments_new, annot=True, cmap='RdYlGn')

# duration_column = list(data['duration'])
#
# mean_duration = []
#
# # внешний цикл по трём сегментам
# for segment in segments_old:
#     interval_scores = []
#     # вложенный цикл по двум периодам
#     for interval in intervals:
#         duration = 0
#         counter = 0
#         # вложенный цикл по строкам
#         for index in range(len(data)):
#             if (segments_column[index] == segment and
#                 intervals_column[index] == interval):
#                 duration += duration_column[index]
#                 counter += 1
#         interval_scores.append(duration / counter)
#     mean_duration.append(interval_scores)
#
# seaborn.heatmap(mean_duration, xticklabels=intervals, yticklabels=segments_new, annot=True, cmap='RdYlGn')

# import pandas
# import seaborn
#
# data = pandas.read_csv('support_data.csv')
#
# score_column = list(data['score'])
# intervals_column = list(data['interval'])
# promo_column = list(data['promo'])
#
# # список всех оценок
# scores = list(range(11))
#
# # ваш код здесь
# promo_count, score_count =0, 0
# for i in range(len(data)):
#     if (intervals_column[i] == 'До внедрения роботов' and
#         promo_column[i] == 1):
#         promo_count += 1
#     if score_column[i] in scores:
#         score_count += 1
# average_promo_count = promo_count / score_count
#
# seaborn.barplot(x=scores, y=average_promo_count)

# games_compactor_on = games[games['compactor'] == True]
# games_compactor_off = games[games['compactor'] == False]

# def add_element(collection):
#     collection.append(0)
#
# some_list = [1,2,3]
# add_element(some_list)
# print(some_list)
#
# some_tuple = (1,2,3)
# add_element(some_tuple)
# print(some_tuple)

# a = int(1 000 000)
# print
# print(635/71/391==635/71/391)
# print(635/(71/391))
# print((635/71)/391)

# import statistics
#
# ls = 1, 5, 2, 7, 1, 9, 3, 8, 5, 9
#
# mean = sum(ls) / len(ls)
# print(mean, statistics.mean(ls))
#
# variance = sum((x - mean) ** 2 for x in ls) / (len(ls) - 1)
# print(variance, statistics.variance(ls))
#
# stdev = variance ** (1 / 2)
# print(stdev, statistics.stdev(ls))

# print(int(input()) + int(input()))

# n = int(input())
# a = [int(i) for i in input().split()]
# b = [int(i) for i in input().split()]
# for i in range(n):
# 	print(a[i], b[i], sep=' ', end=' ')

# n, arr, k = int(input()), [int(i) for i in input().split()], int(input())
# result = []
# current_sum = sum(arr[0:k])
# result.append(current_sum / k)
# for i in range(0, n - k):
#     current_sum -= arr[i]
#     current_sum += arr[i+k]
#     result.append(current_sum / k)
#
# print(*result)


# for i in range(10):
#     n1 = 400 + i * 10 + i
#     n2 = i * 10 + 5
#     print(n1, n2) if 41400+ i * 10 == n1 * n2 else None

# s = 0
# string = input()
# text = input()
# for i in range(len(string)):
#     n = text.count(string[i])
#     s += n
# print(s)

# string = input()
# text = input()
# counter = 0
# for i in text:
#     if i in string:
#         counter += 1
# print(counter)

# with open('input.txt', 'r') as file, open('output.txt', 'w') as out:
#     nums = map(int, file.readline().split())
#     text = str(sum(nums))
#     out.write(text)

# with open('input.txt', 'r') as file, open('output.txt', 'w') as out:
#     nums = map(int, file.readline().split())
#     text = str(sum(nums))
#     print(text, file=out)

# n = int(input())
# numbers = [int(i) for i in input().split()]
# s = int(input())
# def foo(n, numbers, s):
#     for i in range(n):
#         for j in range(i+1, n):
#             if numbers[i] + numbers[j] == s:
#                 return numbers[i], numbers[j]
#     return None, ''
# [print(i, end=' ') if i != None else print('None') for i in foo(n, numbers, s)]

# n = int(input())
# numbers = [int(i) for i in input().split()]
# s = int(input())
#
#
# def twosum_with_sort(n, num, s):
#     num.sort()
#     left = 0
#     right = n - 1
#     while left < right:
#         current_sum = num[left] + num[right]
#         if current_sum == s:
#             return num[left], num[right]
#         elif current_sum < s:
#             left += 1
#         else:
#             right -= 1
#     return None, ''
#
#
# [print(i, end=' ') if i != None else print('None') for i in twosum_with_sort(n, numbers, s)]

# функция twosum_extra_ds(numbers, X):
#     # Создаём вспомогательную структуру данных с быстрым поиском элемента.
#     previous = set()
#
#     для каждого A из numbers:
#         Y = X - A
#         если Y уже лежит в previous, то:
#             вернуть A, Y
#         иначе:
#             добавить A в previous
#
#     # Если ничего не нашлось в цикле, значит, нужной пары элементов в массиве нет.
#     вернуть None, None
