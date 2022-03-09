# a=int(input())
# if a%4==0 and a%100>0 or a%400==0:
#     print('Високосный')
# else:
#     print('Обычный')

# a=int(input())
# b=int(input())
# c=int(input())
# p=float((a+b+c)/2)
# s=float((p*(p-a)*(p-b)*(p-c))**(1/2))
# print(s)

# a = int(input())
# if -15 < a <= 12 or 14 < a < 17 or a >= 19:
#     print('True')
# else:
#     print('False')

# a = float(input())
# b = float(input())
# znak = str(input())
# if b == 0 and (znak == '/' or znak == 'mod' or znak == 'div'):
#     print('Деление на 0!')
# else:
#     if znak == '+':
#         print((a) + (b))
#     elif znak == '-':
#         print((a) - (b))
#     elif znak == 'pow':
#         print((a) ** (b))
#     elif znak == '*':
#         print((a) * (b))
#     elif znak == '/':
#         print((a) / (b))
#     elif znak == 'mod':
#         print((a) % (b))
#     elif znak == 'div':
#         print((a) // (b))


# forma=str(input())
# if forma =='треугольник':
#     a = float(input())
#     b = float(input())
#     c = float(input())
#     p = float((a + b + c) / 2)
#     s = float((p*(p-a)*(p-b)*(p-c))**(1/2))
#     print(s)
# elif forma =='прямоугольник':
#     a = float(input())
#     b = float(input())
#     s = float(a * b)
#     print(s)
# elif forma == 'круг':
#     r = float(input())
#     s = float(3.14*(r**2))
#     print(s)


# a, b, c = int(input()), int(input()), int(input())
# if a<=b<=c:
#     print(c)
#     print(a)
#     print(b)
# elif a<=c<=b:
#     print(b)
#     print(a)
#     print(c)
# elif b<=a<=c:
#     print(c)
#     print(b)
#     print(a)
# elif c<=b<=a:
#     print(a)
#     print(c)
#     print(b)
# elif c<=a<=b:
#     print(b)
#     print(c)
#     print(a)
# else: #b<c<a
#     print(a)
#     print(b)
#     print(c)


#not count
# n = str(input())
# print(n)
# print(int(n))
# print(int(n[-1]))
# print(int(n[-2:]))
# if int(n[-1]) == 1 and int(n[-2:]) != 11:
#     q = ''
#     print(int(n), 'программист' + q)
# elif int(n[-1]) == 2 and int(n[-2:]) != 12:
#     q = 'а'
#     print(int(n), 'программист' + q)
# elif int(n[-1]) == 3 and int(n[-2:]) != 13:
#     q = 'а'
#     print(int(n), 'программист' + q)
# elif int(n[-1]) == 4 and int(n[-2:]) != 14:
#     q = 'а'
#     print(int(n), 'программист' + q)
# else:
#     q = 'ов'
#     print(int(n), 'программист' + q)
#not

# a = str(input())
# s1 = int(a[0])+int(a[1])+int(a[2])
# s2 = int(a[3])+int(a[4])+int(a[5])
# if s1 == s2:
#     print('Счастливый')
# else:
#     print('Обычный')
