# ✔ Решить задачи, которые не успели решить на семинаре.
# ✔ Напишите функцию для транспонирования матрицы
# ✔ Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.
# ✔ Возьмите задачу о банкомате из семинара 2. Разбейте её
# на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.


# ✔ Напишите функцию для транспонирования матрицы

matrix = [[1, 4, 7],
        [2, 5, 8],
        [3, 6, 9]]



def for_reverse_matrix(matrix):
    mat = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            mat[j][i] = matrix[i][j]

    for r in mat:
        print(r)

for_reverse_matrix(matrix)