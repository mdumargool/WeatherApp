import win32com.client as wincom
import requests
import json

city=input("Enter City Name : \n")
url=f"https://api.weatherapi.com/v1/current.json?Key=fe24b97da15f40e9b1340243241107&q={city}"
r=requests.get(url)
# this is print all about kolkata weather.
# print(r.text)
w_dic=json.loads(r.text)
# this is printing only temperature.
temperature=w_dic["current"]["temp_c"]
speaker = wincom.Dispatch("SAPI.SpVoice")
print(temperature)
speaker.Speak(temperature)