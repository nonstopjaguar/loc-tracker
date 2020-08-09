import requests
import json
from win32com.client import Dispatch
import gmplot
import webbrowser
import os

def speak(str1):
	speak=Dispatch(("SAPI.SpVoice"))
	speak.Speak(str1)

res=requests.get('https://ipinfo.io/')

data=res.json()

location=data['loc'].split(",")

latitude=location[0]

longitude=location[1]

city=data['city']
country=data['country']

print("latitude: {}".format(latitude))
speak("latitude: {}".format(latitude))

print("longitude: {}".format(longitude))
speak("longitude: {}".format(longitude))

print("City: {}".format(city))
speak("City: {}".format(city))


print("Country: {}".format(country))
speak("Country: {}".format(country))

gmap=gmplot.GoogleMapPlotter(latitude,longitude,15)

gmap.draw("GoogleMap.html")

speak("GoogleMap.html file is created")

path=os.path.abspath('GoogleMap.html')

url='file://'+path

webbrowser.open(url)

speak("SHAZAM!....")
