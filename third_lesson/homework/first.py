# ✔ Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

my_list = [3, 5, 7, 11, 5, 7, 77, 88, 99]
result_list = []
step = 0
for i in my_list:
    for j in my_list:
        if i == j:
            step += 1
        if step == 2:
            result_list.append(i)
print(result_list)
