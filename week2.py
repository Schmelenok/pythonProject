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


# n = str(input())
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


# a = str(input())
# s1 = int(a[0])+int(a[1])+int(a[2])
# s2 = int(a[3])+int(a[4])+int(a[5])
# if s1 == s2:
#     print('Счастливый')
# else:
#     print('Обычный')

# i = 0
# while i < 5:
#     print('*')
#     if i % 2 == 0:
#         print('**')
#     if i > 2:
#         print('***')
#     i = i + 1

# s=0
# i=int(input())
# while i!=0:
#     s=s+i
#     i=int(input())
# print(s)

# a, b = int(input()), int(input())
# if a == b:
#    d = a
# else:
#     d = min (a, b)
#     while d < min(a, b) * max(a, b) and d % a != 0 or d % b != 0:
#         d = d + 1
# print(d)

# a, b = int(input()), int(input())
# # d=a
# while d%a!=0 or d%b!=0:
#     d+=1
# print(d)

# while True:
#     a = int(input())
#     if a<10:
#         continue
#     if a>100:
#         break
#     print(a)

# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# for i in range(c, (d + 1)):                              #first string
#     print('\t', end=''); print(i, end='')
# print()
# for j in range(a, (b + 1)):                              #string
#     print(j, end='')
#     for z in range(c, (d + 1)):                          #row
#         print('\t', end=''); print(z * j, end='')
#     print()


# a, b = int(input()), int(input())
# s=0
# c=0
# for i in range(a, (b+1)):
#     if i % 3 == 0:
#         s=s+i
#         c=c+1
# print(s/c)

# genome = input()
# c=0
# for i in genome:
#     c=c+1
# p=((genome.lower().count('g')+genome.lower().count('c'))/c)*100
# print(p)

# s = 'abcdefghijk'
# s=s[3:6]
# print(s)
# s = 'abcdefghijk'
# s=s[:6]
# print(s)
# s = 'abcdefghijk'
# s=s[3:]
# print(s)
# s = 'abcdefghijk'
# s=s[::-1]
# print(s)
# s = 'abcdefghijk'
# s=s[-3:]
# print(s)
# s = 'abcdefghijk'
# s=s[:-6]
# print(s)
# s = 'abcdefghijk'
# s=s[-1:-10:-2]
# print(s)

# Кодирование осуществляется следующим образом:
# s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются на этот символ и количество его повторений в этой позиции строки.
#
# Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.

# не решил!!!!!!!!!!!!!!!
# inp = 'aabb'
# c = 1
# print(len(inp))
# for i in range(1, len(inp)):
#     if inp[i - 1] == inp[i]:
#         c = c + 1
#
#     if inp[i - 1] != inp[i]:
#         c = 1
#         print(inp[i - 1] + str(c), end='')
# не решил!!!!!!!!!!!!!!!!!!

# students = ['Ivan', 'Masha', 'Sasha']
# students += ['Olga']
# print(len(students))
# students += 'Olga'
# print(len(students))
# print(students)

# a = [1, 2, 3]
# b = a
# print(b)
#
# a[1] = 10
# print(b)
#
# b[0] = 20
# print(b)
#
# a = [5, 6]
# print(b)

# l = [int(i) for i in input().split()]
# print(l)
# s=0
# for i in range(0, len(l)):
#     s=l[i]+s
# print(s)

# l = [int(i) for i in input().split()]
# if len(l) == 1:
#     print(*l)
# else:
#     l.append(l[0])
#     l.insert(0,l[-2])
#     f=[]
#     for i in range(1, (len(l)-1)):
#         s=l[i-1]+l[i+1]
#         f.append(s)
#     print(*f)

# решение от бога
# lst = [int(i) for i in input().split()]
# for i in range(len(lst)):
#     if len(lst) == 1:
#         print(lst[0])
#     else:
#         print(lst[i - 1] + lst[(i + 1) % len(lst)], end=' ')

# l = [int(i) for i in input().split()]
# l.sort()
# for i in range((len(l)-1)):
#     if l[i-1] == l[i]:
#         print(l[i],end=' ')


# def f(n):
#     return n * 10 + 5
#
# print(f(f(f(10))))

# fib = lambda x : 1 if x <= 2 else fib(x - 1) + fib(x - 2)
# fib(31)

# print('a', 'b', 'c', sep='*')
# print('d', 'e', 'f', sep='**', end='')
# print('g', 'h', 'i', sep='+', end='%')
# print('j', 'k', 'l', sep='-', end='\n')
# print('m', 'n', 'o', sep='/', end='!')
# print('p', 'q', 'r', sep='1', end='%')
# print('s', 't', 'u', sep='&', end='\n')
# print('v', 'w', 'x', sep='%')
# print('y', 'z', sep='/', end='!')



