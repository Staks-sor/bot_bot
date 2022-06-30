from config.config_token import WETHER_TOKEN
import requests
import datetime
import pytz


def open_wether(city, WETHER_TOKEN):

    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WETHER_TOKEN}&units=metric&lang=ru"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно, не пойму что там за погода!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(
            data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])
        moscow = pytz.timezone("Europe/Moscow")

        return f"Московское время: {datetime.datetime.now(moscow).strftime('%Y-%m-%d %H:%M')}\n" \
               f"Погода в городе: {city}\n Температура: {cur_weather}C° {wd}\n" \
               f"Влажность: {humidity}%\n Давление: {pressure} мм.рт.ст\n Ветер: {wind} м/с\n" \
               f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n" \
               f"***Хорошего дня!***"

    except:
        return Exception('нету такого города')


def main():
    city = ("Введите город: ")
    open_wether(city, WETHER_TOKEN)


if __name__ == '__main__':
    main()
