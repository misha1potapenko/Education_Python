import datetime

import requests
from config import tok
from pprint import pprint


def get_weather(tok):
    try:
        city = 'Воронеж'
        my_city = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={tok}")
        my_city_from_json = my_city.json()
        lat = my_city_from_json[0]["lat"]
        lon = my_city_from_json[0]["lon"]
        r = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={tok}"
                         f"&units=metric&lang=ru")
        data = r.json()
        pprint(data)
        show_city = data['city']['name']
        sunrise = datetime.datetime.fromtimestamp(data['city']['sunrise'])
        sunset = datetime.datetime.fromtimestamp(data['city']['sunset'])
        weather = data['list'][0]['dt_txt']
        for i in range(40):
            print(data['list'][i]['dt_txt'])
            print(data['list'][i]['weather'][0]['description'])
        print(f"Город: {show_city} Восход солнца: {sunrise} Заход солнца: {sunset}\n"
              f" Прогноз на {weather}")


    except Exception as ex:
        print(ex)
        print("Что-то пошло не так")


def main():
    get_weather(tok)


if __name__ == '__main__':
    main()