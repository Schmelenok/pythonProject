def compare_by_second(point):
    return point[1]


def compare_by_sum(point):
    return point[0] + point[1]



points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]

print(sorted(points, key=compare_by_second))   # сортируем по второму значению кортежа
print(sorted(points, key=compare_by_sum))      # сортируем по сумме кортежа