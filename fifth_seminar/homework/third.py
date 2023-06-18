# ✔Создайте функцию генератор чисел Фибоначчи (см. Википедию).


def fibonachi(num):
    fib = []
    for i in range(1, num):
        if i == 1:
            fib.append(i)
        elif i == 2:
            fib.append(i)
        else:
            fib.append(fib[i-3] + fib[i-2])
    return fib


print(fibonachi(12))



