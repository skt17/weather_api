# app={"coord":{"lon":83.7303,"lat":21.2157},
# "weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],
# "base":"stations","main":{"temp":29.22,"feels_like":34.24,"temp_min":29.22,"temp_max":29.22,"pressure":1000,"humidity":75,"sea_level":1000,"grnd_level":983},"visibility":10000,"wind":{"speed":2,"deg":236,"gust":2.2},"clouds":{"all":100},"dt":1629896235,"sys":{"country":"IN","sunrise":1629850011,"sunset":1629895680},
# "timezone":19800,"id":0,"name":"Kubedega","cod":200}
# print(app["weather"][0]["main"])
# print(app["main"]["temp"])
import json
ab='{"abc":"uu"}'
b=json.loads(ab)
print(type(b))