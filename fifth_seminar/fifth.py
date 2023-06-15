# ✔Создайте функцию-генератор. ✔Функция генерирует N простых чисел, начиная с числа 2.
# ✔Для проверки числа на простоту используйте правило:
# «число является простым, если делится нацело только на единицу и на себя».


# ✔ Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного
# генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт»
# без перехода на новую строку.



# nums = ((f"{x} * {y} = {x*y}") for x in range(1, 11) for y  in range(1, 11))
#
# for i in nums:
#     print(i)


# print(*((f"{x} * {y} = {x*y}") for x in range(1, 11) for y  in range(1, 11)), sep= '\n')

def multy_table(size):
    for i in range(1, 11):
        for j in range(1, size // 2 + 1):
            print(f"{j} x {i} = {i * j}", end=" " * (15 - len(f"{j} x {i} = {i * j}")))

        print()
    print()
    for i in range(1, 11):
        for j in range(size // 2 + 1, size + 1):
            print(f"{j} x {i} = {i * j}", end=" " * (15 - len(f"{j} x {i} = {i * j}")))
        print()

# print(*((f"{x} * {y} = {x*y}   {x+5} * {y} = {(x+5)*y}   ") for x in range(1, 6) for y  in range(1, 11)  ), sep= '\n')
print('\n\n'.join(('\n'.join('\t\t'.join(f'{i:^3} x {j:^3} = {i * j:^3}' for i in range(i[0], i[1])) for j in range(2, 11)) for i in [(2,6), (6,10)])), sep='')