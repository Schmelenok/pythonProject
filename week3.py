# a, b = int(input()), int(input())
# counter = 0
# for i in range(a, b+1):
#     if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
#         counter += 1
# print(counter)

# full = int(input())
# total = 0
# for i in range(full):
#     n = int(input())
#     total += n
# print(total)

# from math import log
# n = int(input())
# x = 0
# for i in range(1, n+1):
#     x = x + 1/i
# x = x -log(n)
# print(x)
#
# b, t = int(input()), 0
# for i in range(1, b+1):
#     if i ** 2 % 10 == 2 or i ** 2 % 10 == 5 or i ** 2 % 10 == 8:
#         t += i
# print(t)

# n, p = int(input()), 1
# for i in range(1, n+1):
#     p *= i
# print(p)

# p = 1
# for i in range(10):
#     num = int(input())
#     if num != 0:
#         p *= num
# print(p)

# n, t = int(input()), 0
# for i in range(1, n+1):
#     if n % i == 0 :
#         t += i
# print(t)

# n, x = int(input()), 0
# for i in range(1, n+1):
#     if i % 2 == 0:
#         x = x - i
#     else:
#         x = x + i
# print(x)

# n, max1, premax = int(input()), 0, 0
# for i in range(n):
#     num = int(input())
#     if num > max1:
#         premax = max1
#         max1 = num
#     elif num < max1 and num > premax:
#         premax = num
# print(max1, premax, sep='\n')

# flag, counter = True, 0
# for i in range(10):
#     num = int(input())
#     if num % 2 != 0:
#         flag = False
#         counter += 1
# if flag == True and counter == 0:
#     print('YES')
# else:
#     print('NO')

# n, a, b = int(input()), 1, 1
# if n == 1:
#     print(a)
# if n == 2:
#     print(a, b, sep=' ')
# if n > 2:
#     print(a, b, sep=' ', end=' ')
#     for i in range(3, n+1):
#         f = a + b
#         print(f, sep=' ', end=' ')
#         a = b
#         b = f
#
# n, a, b = int(input()), 1, 1
# for i in range(n):
#     print(a, end=' ')
#     a, b = b, a + b

# num = int(input())
# while num % 7 == 0:
#     print(num)
#     num = int(input())


# price, coins = int(input()), 0
# while price >= 25:
#     coins = coins + 1
#     price = price - 25
# while price >= 10:
#     coins = coins + 1
#     price = price - 10
# while price >= 5:
#     coins = coins + 1
#     price = price - 5
# while price >= 1:
#     coins = coins + 1
#     price = price - 1
# print(coins)

# n = int(input())
# k = 0
# for i in (25, 10, 5, 1):
#     while n // i > 0:
#         k += 1
#         n -= i
# print(k)

# num = 12345
# product = 1
# while num != 0:
#     last_digit = num % 10
#     product = product * last_digit
#     num = num // 10
# print(product)

# num = int(input())
# mi = ma = num % 10
# while num != 0:
#     last_digit = num % 10
#     if last_digit >= ma:
#         ma = last_digit
#     if last_digit < mi:
#         mi = last_digit
#     num = num // 10
# print('Максимальная цифра равна', ma)
# print('Минимальная цифра равна', mi)

# n, s, c, p= int(input()), 0, 0, 1
# digit = l = n % 10
# while n != 0:
#     digit = n % 10
#     s += digit
#     p *= digit
#     c += 1
#     n //= 10
# print(s, c, p, s/c, digit, digit+l, sep='\n')

# n = int(input())
# while n > 9:
#     l = n % 10
#     n //= 10
# print(l)

# num, flag = int(input()), 'YES'
# last = num % 10
# while num != 0:
#     oper_digit = num % 10
#     if oper_digit < last:
#         flag = 'NO'
#     last = oper_digit
#     num = num // 10
# print(flag)

# n = int(input())
#
# flag = 'YES'
# s = n % 10
# while n != 0:
#     n1 = n % 10
#     if s > n1:
#         flag = 'NO'
#     s = n1
#     n = n // 10
# print(flag)

# for i in range(10):
#     print(i, end='*')
#     if i > 6:
#         break

# n = 10
# while n > 0:
#     n -= 1
#     if n == 2:
#         continue
#     print(n, end='*')
# import time

# n = int(input())
# counter = 0
# for i in range(2, n+1):
#     if n % i == 0:
#         counter += 1
# print(counter)    #need to add the timer for big numbers

# n = int(input())
# for i in range(1, n+1):
#     if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
#         continue
#     print(i)

# n = int(input())
# while n != 0:
#     last = n % 10
#     if last == 7:
#         print('Число', n, 'содержит цифру 7')
#         break
#     n //= 10
# else:
#     print('Число', n, 'не содержит цифру 7')

# count = 0
# p = 1
# for i in range(10):
#     x = int(input())
#     if x >= 0:
#         p *= x
#         count = count + 1
# if count > 0:
#     print(count)
#     print(p)
# else:
#     print('NO')

# mx = -1000000
# s = 0
# counter = 0
# for i in range(10):
#     x = int(input())
#     if x < 0:
#         s = s + x
#     else:
#         counter += 1
#     if mx < x < 0:
#         mx = x
# if counter != 10:
#     print(s)
#     print(mx)
# else:
#     print('NO')
#

# n = int(input())
# counter = 0
# max_digit = -1
# while n != 0:
#     digit = n % 10
#     if digit % 3 == 0 and digit >= max_digit:
#         max_digit = digit
#         counter +=1
#     n = n // 10
# if counter != 0:
#     print(max_digit)
# else:
#     print('NO')

# n = int(input())
# while n > 9:
#     n //= 10
# print(n)

# for i in range(1, 4):
#     for j in range(3, 5):
#         print(i + j, end='')

# n = int(input())
# for i in range(1, n+1):
#     for j in range(5):
#         print(i, end=' ')
#     print()

# n = int(input())
# for i in range(1, n+1):
#     for j in range(1, 10):
#         print(i, '+', j, '=', i+j)
#     print()

# n = int(input())
# for i in range(n//2+1):
#     for j in range(i+1):
#         print('*', end=' ')
#     print()
# for i in range(n//2,0,-1):
#     for j in range(i):
#         print('*', end=' ')
#     print()

# n = int(input())
# for i in range(n+1):
#     for j in range(i):
#         print(i, end='')
#     print()

# total = 0
# for x in range(1, 66):
#     for y in range(1, 61):
#         if 12 * x + 13 * y == 777:
#             total += 1
#             print('x =', x, 'y =', y)
# print('Общее количество натуральных решений =', total)

# total = 0
# for n in range(1, 15):
#     for k in range(1, 14):
#         for m in range(1, 13):
#             if 28 * n + 30 * k + 31 * m == 365:
#                 total += 1
#                 print('n =', n, 'k =', k, 'm =', m)
# print('Общее количество натуральных решений =', total)

# total = 0
# for n in range(1, 11):
#     for k in range(1, 21):
#         for m in range(1, 101):
#             if 10 * n + 5 * k + 0.5 * m == 100 and n + k + m == 100:
#                 total = total + 1
#                 print('n =', n, 'k =', k, 'm =', m)
#
# print('Общее количество натуральных решений =', total)

# for a in range(3, 151):
#     for b in range(a, 151):
#         for c in range(b, 151):
#             for d in range(c, 151):
#                 for e in range(d, 151):
#                     if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
#                         print(a, b, c, d, e)
#                     if e ** 5 > a ** 5 + b ** 5 + c ** 5 + d ** 5:
#                         break

# n, c = int(input()), 1
# for i in range(n+1):
#     for j in range(i):
#         print(c, end='')
#         c += 1
#     print()
#
# n = int(input())
# for i in range(n+1):
#     for j in range(1, i+1):
#         print(j, end='')
#     for k in range(i-1, 0, -1):
#         print(k, end='')
#     print()

# a, b, max_s, num = int(input()), int(input()), 0, 0
# for i in range(a, b+1):
#     s = 0
#     for j in range(1, i+1):
#         if i % j == 0:
#             s += j
#     if s >= max_s:
#         max_s = s
#         num = i
# print(num, max_s)

# n, c = int(input()), 0
# for i in range(1, n+1):
#     c = 0
#     for j in range(1, i+1):
#         if i % j == 0:
#             c += 1
#     print(i, '+' * c, sep='')

# n, s = int(input()), 0
# while n > 9:
#     while n != 0:
#         s += n % 10
#         n //= 10
#     n = s
#     s = 0
# print(n)

# n, s = int(input()), 0
# for i in range(1, n+1):
#     p = 1
#     for j in range(1, i+1):
#         p *= j
#     s += p
# print(s)

# a, b, c, num = int(input()), int(input()), 0, 0
# for i in range(a, b+1):
#     c = 0
#     for j in range(1, i+1):
#         if i % j == 0:
#             c += 1
#     if c == 2:
#         print(i)

# s = '01234567891011121314151617'
# print(len(s))
# print(s[25])
# for i in range(0, len(s), 5):
#     print(s[i], end='')

# text = str(input())
# for c in range(-1, -len(text)-1, -1):
#     print(text[c])

# s = ''
# for i in range(3):
#     text = str(input())
#     s = s + text[0]
# print(s)

# a, b, c = str(input()), str(input()), str(input())
# print(b[0], a[0], c[0], sep='')

# number = str(input())
# s = 0
# for c in number:
#     c = int(c)
#     s += c
# print(s)

# number = str(input())
# for i in range(10):
#     if str(i) in number:
#         print('Цифра')
#         break
# else:
#     print('Цифр нет')

# text, c, z = str(input()), 0, 0
# for i in text:
#     if i == '*':
#         c += 1
#     if i == '+':
#         z += 1
# print(f'Символ + встречается {z} раз')
# print(f'Символ * встречается {c} раз')

# text, c = str(input()), 0
# for i in range(0, len(text)-1):
#     if text[i] == text[i+1]:
#         c += 1
# print(c)

# text, s, g = str(input()), 0, 0
# for i in text:
#     if i in ('ауоыиэяюёеАУОЫИЭЯЮЁЕ'):
#         g += 1
#     if i in ('бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'):
#         s += 1
# print(f'Количество гласных букв равно {g}')
# print(f'Количество согласных букв равно {s}')

# number, s = int(input()), ''
# while number != 0:
#     s += str(number % 2)
#     number //= 2
# print(s[::-1])

# s = 'abcdefg'
# print(s[::-3])

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[:12])

# text = str(input())
# if text[:] == text[::-1]:
#     print('YES')
# else:
#     print('NO')

# text = str(input())
# print(text[2])
# print(text[-2])
# print(text[:5])
# print(text[:-2])
# print(text[::2])
# print(text[1::2])
# print(text[::-1])
# print(text[::-2])

# text = str(input())
# if len(text) % 2 == 0:
#     first = text[:int((len(text))/2)]
#     second = text[int((len(text))/2):]
# else:
#     first = text[:int((len(text))//2+1)]
#     second = text[int((len(text))//2+1):]
# print(second+first)

# text = input()
# second = len(text) - len(text)//2
# print(text[second:]+text[:second])

# text = input()
# if 'хорош' in text.lower():
#     print('YES')
# else:
#     print('NO')

# text, c = input(), 0
# for _ in text:
#     if _ in 'abcdefghijklmnopqrstuvwxyz':
#         c += 1
# print(c)

# s = 'aabbAAccDDaa aa aA'
# s = s.lower()
# print(s.count('a'))

# c = input().count(' ')
# if c == 0:
#     print(1)
# else:
#     print(c+1)

# s = input().lower()
# print(f'Аденин: {s.count("а")}', f'Гуанин: {s.count("г")}', f'Цитозин: {s.count("ц")}', f'Тимин: {s.count("т")}', sep='\n')

# n, counter = int(input()), 0
# for _ in range(n):
#     c = input().count('11')
#     if c >= 3:
#         counter += 1
# print(counter)

# text, c = input(), 0
# for _ in text:
#     if _ in '0123456789':
#         c += 1
# print(c)

# text = input()
# if text.endswith('.com') or text.endswith('.ru'):
#     print('YES')
# else:
#     print('NO')

# text, maxcounter = input(), 0
# for j in text:
#     counter = text.count(j)
#     if counter >= maxcounter:
#         maxcounter = counter
#         maxchar = j
# print(maxchar)

# text = input()
# if text.count('f') >= 2:
#     print(text.find('f'), text.rfind('f'))
# elif text.count('f') == 1:
#     print(text.find('f'))
# else:
#     print('NO')
#
# s = input()
# if 'f' in s:
#     print(s.find('f'), end=' ')
#     if s.rfind('f') != s.find('f'):
#         print(s.rfind('f'))
# else: print('NO')

# text = input()
# print(text[:(text.find('h'))], text[(text.rfind('h')+1):], sep='')

# a = int(input())
# b = int(input())
# for i in range(a, b+1):
#     print(chr(i), end=' ')

# txt = str(input())
# for i in txt:
#     print(ord(i), end=' ')

# n = int(input())
# txt = str(input())
# for i in txt:
#     a = ord(i)-n
#     if a < 97:
#         a += 26
#     print(chr(a), end='')

# numbers = [2, 4, 6, 8, 10]
# languages = ['Python', 'C#', 'C++', 'Java']
# print(numbers)
# print(*languages, sep='')
# print(languages)

# n, l = int(input()), list()
# for i in range(97, 97+n):
#     l.append(chr(i))
# print(l)

# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
# print(primes[17])

# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
# print(len(numbers))
# print(numbers[-1])
# print(numbers[::-1])
# if 5 and 17 in numbers:
#     print('YES')
# else:
#     print('NO')
# del numbers[0], numbers[-1]
# print(numbers)

# l = list()
# for i in range(int(input())):
#     l.append(input())
# print(*l)

# l = list()
# for i in range(1, 27):
#     l.append((chr(96+i))*i)
# print(l)

# l, n = list(), int(input())
# for i in range(1, n//2+1):
#     if n % i == 0:
#         l.append(i)
# l.append(n)
# print(l)

# l, n, y, x = list(), int(input()), int(input()), 0
# for i in range(n-1):
#     x = int(input())
#     y += x
#     l.append(y)
#     y = x
# print(l)

# l = list()
# for i in range(int(input())):
#     l.append(input())
# del l[1::2]
# print(l)

# in_list = list()
# for i in range(int(input())):
#     in_list.append(input())
# k = int(input())
# for i in in_list:
#     if k <= len(i):
#         print(i[k-1], end='')
#     else:
#         continue

# in_list = list()
# for i in range(int(input())):
#     in_list.extend(input())
# print(in_list)

# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# for i in range(len(numbers)):
#     numbers[i] = numbers[i]**2
# print(sum(numbers))

# inlist, outlist = list(), list()
# for i in range(int(input())):
#     x = int(input())
#     inlist.append(x)
#     outlist.append(x ** 2 + 2 * x + 1)
# print(*inlist, sep='\n')
# print()
# print(*outlist, sep='\n')

# inlist = list()
# for i in range(int(input())):
#     inlist.append(int(input()))
# for j in inlist:
#     if j != max(inlist) and j != min(inlist):
#         print(j, sep='\n')

# inlist = list()
# for i in range(int(input())):
#     n = input()
#     if n not in inlist:
#         inlist.append(n)
# print(*inlist, sep='\n')

# inlist, slist = list(), list()
# n = int(input())
# for _ in range(n):
#     inlist.append((input()))
# s = int(input())
# for _ in range(s):
#     slist.append((input()))
# for i in inlist:
#     counter = 0
#     for j in slist:
#         if j.lower() in i.lower():
#             counter += 1
#     if counter == s:
#         print(i)

# inlist, slist = list(), list()
# n = int(input())
# for _ in range(n):
#     inlist.append((input()))
# s = int(input())
# for _ in range(s):
#     slist.append((input()))
# for i in inlist:
#     flag = True
#     for j in slist:
#         if j.lower() not in i.lower():
#             flag = False
#             break
#     if flag:
#         print


# outlist1, outlist2, outlist3, outlist4 = list(), list(), list(), list()
# # for _ in range(int(input())):
# #     inlist.append((int(input())))
# inlist = [16,10,1,2,3,4,5,0,0,0,0,7,8,9,-8,-9,0]
# for i in inlist:
#     if i < 0:
#         outlist1.append(i)
#     if i == 0:
#         outlist2.append(i)
#     if i > 0:
#         outlist3.append(i)
#     outlist4 = outlist1+outlist2+outlist3
# print(*outlist4, sep='\n')
# del outlist3, outlist2, outlist1

# У лукоморья дуб зеленый златая цепь на дубе том


# print(*(input().split()), sep='\n')
# C:\Windows\System32\calc.exe

# for i in input().split():
#     i = int(i)
#     print('+'*i)

# 192.168.0.3

# for i in input().split('.'):
#     i = int(i)
#     flag = 'ДА'
#     if i < 0 or i > 255:
#         flag = 'НЕТ'
#         break
# print(flag)

# txt, n = input(), input()
# print(n.join(txt))

# counter = 0
# txt = input().split()
# for i in range(len(txt)):
#     for z in range(i+1, (len(txt))):
#         if txt[i] == txt[z]:
#             counter +=1
# print(counter)

# numbers = [8, 9, 10, 11]
# # numbers.insert(1, 17)
# numbers[1] = 17
# numbers.extend([4, 5, 6])
# del numbers[0]
# numbers = numbers * 2
# numbers.insert(3, 25)
# print(numbers)

# txt = input().split()
# for j in range(len(txt)):
#     txt[j] = int(txt[j])
# a = txt.index(min(txt))
# b = txt.index(max(txt))
# txt[a], txt[b] = max(txt), min(txt)
# print(*txt)

# txt, counter = input().split(), 0
# for i in txt:
#     if i.lower() == 'a' or i.lower() == 'an' or i.lower() == 'the':
#         counter += 1
# print(f'Общее количество артиклей: {counter}')

# txt = input().lower().split()
# print(txt.count('an')+txt.count('a')+txt.count('the'))

# txt, stringlist = input(), list()
# txt = txt[1:]
# for i in range(int(txt)):
#     st = input()
#     if '#' in st:
#         st = str(st[:(int(st.index('#')))].rstrip())
#         stringlist.append(st)
#     else:
#         stringlist.append(st)
# print(*stringlist, sep='\n')

# l= input().split()
# for j in range(len(l)):
#     l[j] = int(l[j])
# l.sort()
# print(*l)
# l.sort(reverse=True)
# print(*l)
#
# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
# new_keywords = [ i for i in keywords if len(i) >= 5]
# print(new_keywords)

# palindromes = [i for i in range(100, 1000) if str(i)[::1] == str(i)[::-1]]
# print(palindromes)

# kva = [i**2 for i in range(1, int(input())+1)]
# print(*[j for j in kva], sep='\n')

# s = input().split()
# print(*[int(i)**3 for i in s])

# print(*[j for j in input() if j.isdigit()], sep='')

# print(*[int(j)**2 for j in input().split() if (int(j) ** 2) % 2 == 0 and (int(j) **  2) % 10 != 4])



#
# [27, 79, 71, 71, 58, 48, 88, 88, -16, 78, 96, 76, 56, 92, 1, 32, -17, 36, 88, -61, 97, -37, -84, 50, 47, 94, -6, 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91, 44, 25, 79, 97, 0, -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, -44, -56, -41, 38, 16, 70, 17, -17, -24, -83, -74, -73, 11, -26, 63, -75, -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39, 38, -55, 7, -11, -26, -62, -84]
# a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
# n = len(a)
#
# for i in range(n - 1):
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:                  # если порядок элементов пары неправильный
#             a[j], a[j + 1] = a[j + 1], a[j]  # меняем элементы пары местами
#
# print('Отсортированный список:', a)

# a = [78, -32, 5, 39, 58, -5]
# n = len(a)
# for i in range(n - 1):
#     mi = a.index(max(a[:n - i]))
#     a[mi], a[-i-1] = a[-i-1], a[mi]
# print(a)

# a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
# n = len(a)
# # for i in range(1, n):
#     elem = a[i]  # первый элемент из неотсортированной части списка
#     j = i
#     while j >= 1 and a[j - 1] > elem:
#         a[j] = a[j - 1]                               #сортировка вставкой
#         j -= 1
#     a[j] = elem
#
#
# print('Отсортированный список:', a)