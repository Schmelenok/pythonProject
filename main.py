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
