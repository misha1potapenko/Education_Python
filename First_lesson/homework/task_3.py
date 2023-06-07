# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.

from random import randint

num = int(randint(0, 1001))
print("Загаданное число", num)
count = 10
comp_number = 500

print("Число компьютера", comp_number)
while count > 0:
    if comp_number == num:
        print("Угадал")
        break
    elif comp_number < num:
        print("Меньше")
        print("Число компьютера", comp_number)
        comp_number = int(comp_number + (comp_number/2))
        count -= 1
        continue
    elif comp_number > num:
        print("Больше")
        print("Число компьютера", comp_number)
        comp_number = int(comp_number - (comp_number/2))
        count -= 1
        continue





