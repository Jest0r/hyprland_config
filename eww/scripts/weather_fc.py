#!/usr/bin/env python

# import urllib.request
# import requests
import json
from sys import exit
from urllib3 import disable_warnings, PoolManager
from datetime import datetime

# this is an awkward mix of urllib, urllib3 and requests, this has to change!

disable_warnings()

api = "60a3d75a015f27a60754b7c7c5a02da0"
city = "Erding,DE"
# lon = 11.903
# lat = 48.283
fc_url = "https://api.openweathermap.org/data/2.5/forecast?units=metric&appid="
weather_url = "https://api.openweathermap.org/data/2.5/weather?units=metric&appid="
icon_base_url = "https://openweathermap.org/img/wn/"
img_path = "resources/weather.png"
# full_url = f"{url}{api}&lon={lon}&lat={lat}"
full_url = f"{fc_url}{api}&q={city}"

testfile = "resources/forecast_tst.json"
use_test_file = True

# kelvin = -273.15
time_format = "%H:%M"

# get weather data
http = PoolManager()


if use_test_file:
    with open(testfile) as fp:
        content = json.load(fp)
else:
    r = http.request("GET", full_url)
    if r.status != 200:
        print('(label :text "-unknown error-")')
        exit(1)
    content = r.json()
    r.release_conn()

# city and day length
city = f"{content['city']['name']}, {content['city']['country']}"
sunrise = datetime.fromtimestamp(content["city"]["sunrise"])
sunset = datetime.fromtimestamp(content["city"]["sunset"])


print(
    f" {city}.  {datetime.strftime(sunrise, time_format)},  {datetime.strftime(sunset, time_format)}"
)

for fc in content["list"][:3]:
    print(f"{datetime.fromtimestamp(fc['dt'])}")
    print(fc)


# print(json.dumps(content, indent=3))


# r = http.request("GET", icon_url, preload_content=False)

# with open(img_path, "wb") as fp:
#     while True:
#         data = r.read()
#         if not data:
#             break
#         fp.write(data)


# print(
#    f'(box :class "weatherw" (label :text "{int(temp_c)}°C") (image :image-width 32 :image-height 32 :path "{img_path}"))'
# )
