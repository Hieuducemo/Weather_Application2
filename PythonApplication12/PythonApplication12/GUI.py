from tkinter import *
from WeatherAPI import WeatherAPI
import requests 
from datetime import datetime
import json
#This function assumes that the input timestamp is in UTC, so it converts it to the equivalent time in the UTC timezone.
def time_format_for_location(utc_with_tz):
        local_time = datetime.utcfromtimestamp(utc_with_tz)
        return local_time.time()
"""The text describes a class called "GUI", which is used to create a graphical user interface for a weather application.
The class has a constructor that initializes the window, sets its dimensions, title, and background image"""
class GUI():
     def __init__(self, root):
        #Initialize Window
        self.root = root
        self.root.geometry("1200x750")
        self.root.resizable(0, 0)
        self.root.title("Weather Application")
        #background
        self.background_image = PhotoImage(file='janna.png')
        self.background_image = self.background_image.subsample(1)
        self.background_label = Label(root, image=self.background_image, bg='white')
        self.background_label.place(relx=0.5, rely=0.5, anchor=CENTER)
        #Add label
        self.city_head = Label(root, text='Enter City Name', font='Arial 12 bold', bg='white')
        self.city_head.pack(pady=10) #make label transparent
        #take the value in the textbox
        self.city_value = StringVar()
        self.inp_city = Entry(root, textvariable=self.city_value, width=24, font='Arial 14 bold', bg='white')
        self.inp_city.pack()
        city_name = self.city_value.get()
        #button, when click the button, method check_weather will run
        self.button = Button(root,command= self.check_weather, text="Check Weather", font="Arial 10", bg='#2196f3', fg='white', activebackground="#1e88e5", padx=5, pady=5)
        self.button.pack(pady=20)

        self.weather_now = Label(root, text="The Weather is:", font='Arial 12 bold', bg='white')
        self.weather_now.pack(pady=10)

        self.tfield = Text(root, width=46, height=10, bg='white')
        self.tfield.pack()
    
     def check_weather(self):
        city_name=self.city_value.get()
        #Enter you api key, copies from the OpenWeatherMap dashboard
        weather_api = WeatherAPI("dd4d20110ab6f647cb8cace44511634c", "http://api.openweathermap.org/data/2.5/weather?q=")
        api_key = str(weather_api.getAPI())
        url_web = str(weather_api.getURL())
         # API url
        weather_url = url_web + city_name + '&appid=' + api_key 
         # Get the response from fetched url
        response = requests.get(weather_url)
         # changing response from json to python readable
        weather_info = response.json()
        self.tfield.delete("1.0", "end") #to clear the text field for every new output

        #as per API documentation, if the cod is 200, it means that weather data was successfully fetched
        if weather_info['cod'] == 200:
           kelvin = 273 # value of kelvin
           temp = int(weather_info['main']['temp'] - kelvin)
           #-----------Storing the fetched values of weather of a city
           feels_like_temp = int(weather_info['main']['feels_like']-kelvin)
           pressure=weather_info['main']['pressure']
           humidity = weather_info['main']['humidity']
           wind_speed = weather_info['wind']['speed'] * 3.6
           sunrise = weather_info['sys']['sunrise']
           sunset = weather_info['sys']['sunset']
           timezone = weather_info['timezone']
           cloudy = weather_info['clouds']['all']
           description = weather_info['weather'][0]['description']
           sunrise_time = time_format_for_location(sunrise + timezone)
           sunset_time = time_format_for_location(sunset + timezone)
 
           #assigning Values to our weather varaible, to display as output
        
           weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}\nFeels like in (Celsius): {feels_like_temp}\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
        else:
           weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"
 
 
    
        self.tfield.insert(INSERT, weather)   #to insert or send value in our Text Field to display output

       