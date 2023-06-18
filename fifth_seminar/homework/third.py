# ✔Создайте функцию генератор чисел Фибоначчи (см. Википедию).



def fibonachi(num):
    fib = []
    for i in range(num):
        if i == 1:
            fib.append(i)
        if i == 2:
            fib.append(i)
        else:
            fib.append(fib[i-1] + fib[i-2] )
