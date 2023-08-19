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
    except Exception as ex:
        print(ex)
        print("Что-то пошло не так")


def main():
    get_weather(tok)


if __name__ == '__main__':
    main()