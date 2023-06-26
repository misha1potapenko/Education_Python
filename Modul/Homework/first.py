def _leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True


def my_date(date: str):
    day, month, year = list(map(int, date.split('.')))
    flag = None

    if 1 <= year <= 9999 and 1 <= month < 13 and 1 <= day <= 31:
        if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
            flag = True
        elif month in [4, 6, 9, 11] and 1 <= day <= 30:
            flag = True
        else:
            flag = _leap_year(year) and day <= 29

    return f'\n\tКорректность даты - {flag}\n'



if __name__ == '__main__':
    print(my_date('25.12.1986'))
    print(my_date('29.2.2023'))
    print(my_date('29.2.2020'))
    print(my_date('32.3.2020'))
