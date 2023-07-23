# 📌Функция получает на вход текст вида:
# “1-й четверг ноября”, “3я среда мая” и т.п.
# 📌Преобразуйте его в дату в текущем году.
# 📌Логируйте ошибки, если текст не соответсвует формату.

# from datetime import datetime
#
#
# def my_date(str_date: str):
#     parse_date = str_date.split()
#     dict_for_day = {'пон': 'Monday', 'вто': 'Tuesday', 'сре': 'Wednesday',
#                     'чет': 'Thursday', 'пят': 'Friday', 'суб': 'Saturday', 'вос': 'Sunday'}
#     dict_for_month = {
#         'янв': 'January', 'фев': 'February', 'мар': 'March', 'апр': 'April',
#         'мая': 'May', 'июн': 'June', 'июл': 'July', 'авг': 'August',
#         'сен': 'September', 'окт': 'October', 'ноя': 'November', 'дек': 'December'}
#     if parse_date[1][:3] in dict_for_day:
#         date_day = dict_for_day[parse_date[1][:3]]
#     if parse_date[2][:3] in dict_for_month:
#         month = dict_for_month[parse_date[2][:3]]
#     day = parse_date[0][:1]
#     string_date = date_day + " " + month + " " + "2023"
#
#     text_date = datetime.strptime(string_date, '%A %B %Y')
#     print(text_date)
#
#
# my_date('3я среда мая')
#
#
# import datetime
# date_time_str = '2018-06-29 08:15:27.243860'
# date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
# print('Дата:', date_time_obj.date())
# print('Время:', date_time_obj.time())
# print('Дата и время:', date_time_obj)


'''
Задание №4
Функция получает на вход текст вида: “1-й четверг ноября”, “3-
я среда мая” и т.п.
Преобразуйте его в дату в текущем году.
Логируйте ошибки, если текст не соответсвует формату.
'''

import logging
from datetime import datetime, date


logging.basicConfig(filename='Task4.log',
                    filemode='w',
                    encoding='utf-8',
                    format='{asctime} {levelname:<8} функция "{funcName}()" строка {lineno:>3d} : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

months = {'янв': 1, 'фев': 2,'мар': 3,'апр': 4,'мая': 5,'июн': 6,'июл': 7,'авг': 8,'сен': 9,'окт': 10,'ноя': 11,'дек': 12}
weekdays = {'пон': 1, 'вто': 2,'сре': 3,'чет': 4,'пят': 5,'суб': 6,'вос': 7}

def parse_date(text: str):
    '''Переводим текст в объект дату'''
    try:
        year = datetime.now().year                     # 2023
        count, weekday_, month_ = text.split()            # 3-я среда мая - текстовый формат
        month = months[month_[:3]]                       # 5 - число
        weekday = weekdays[weekday_[:3]] - 1             # 2 - число
        count = int(count[0])
    except Exception as exc:
        logger.info(f'{count}-й  {weekday_}  {month_} {year} =  ошибка: {exc}')

    count_week = 0
    for day in range(1, 31 + 1):
        rezult = date(year=year, month=month, day=day)
        if rezult.weekday() == weekday:
            count_week += 1
            if count_week == count:
                logger.info(f'{count}-й(ое) {weekday_} {month_} {year} = {rezult} ')
                return rezult




if __name__ == '__main__':
    print('1-й понедельник мая:', parse_date('1-й понедельник мая'))
    print('2-й четверг ноября:', parse_date('2-й четверг ноября'))
    print('1-я среда мая:', parse_date('1-я среда мая'))