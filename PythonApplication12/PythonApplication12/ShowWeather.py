"""
from WeatherAPI import WeatherAPI
import json
from tkinter import *
class show_weather():
  #  def show(city_name):
     
     weather_api = WeatherAPI("dd4d20110ab6f647cb8cace44511634c", "http://api.openweathermap.org/data/2.5/weather?q=")
     api_key = weather_api.getAPI
     url_web=  weather_api.getURL
     weather_url = url_web+city_name+'&appid='+api_key 
     response = requests.get(weather_url)
     weather_info = response.json()
     tfield.delete("1.0", "end")
     if weather_info['cod'] == 200:
        kelvin = 273 # value of kelvin
        temp = int(weather_info['main']['temp'] - kelvin)           #converting default kelvin value to Celcius
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']
       
        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)
        weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}\nFeels like in (Celsius): {feels_like_temp}\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
     else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"
     tfield.insert(INSERT, weather)   #to insert or send value in our Text Field to display output"""