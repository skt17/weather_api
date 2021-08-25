import http.client
from twilio.rest import Client
import json
conn = http.client.HTTPSConnection("api.openweathermap.org")
payload = ''
headers = {}
conn.request("GET", "/data/2.5/weather?zip=768104,in&units=metric&appid=04e6331f0fda22c605ad7676cd5e3cbd\
", payload, headers)
res = conn.getresponse()
data = res.read()
data=json.loads(data.decode("utf-8"))
# Somu :- 
weather_info=data["weather"][0]["main"]
temp=data["main"]["temp"]


client=Client("AC3ec22f2178e0b85386a9b33a0904f7d9",
            "98851a9e4355c9170c8786db50c7f772")
msg=client.messages.create(to="whatsapp:+919178776712",
                            from_="whatsapp:+14155238886",
                            body=f"Tempreture is {temp}\nThe weather is {weather_info}"
                            )
