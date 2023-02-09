import requests
class WeatherAPI():
    def __init__(self, api_key, url):
        self.api_key = api_key
        self.url = url
    def getAPI(self):
        return self.api_key
    def getURL(self):
        return self.url
   
