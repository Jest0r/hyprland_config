#!/usr/bin/env python

# import urllib.request
# import requests
# import json
from sys import exit
from urllib3 import disable_warnings, PoolManager

# this is an awkward mix of urllib, urllib3 and requests, this has to change!

disable_warnings()

api = "60a3d75a015f27a60754b7c7c5a02da0"
city = "Erding,DE"
lon = 28.28
lat = 11.9
url = "https://api.openweathermap.org/data/2.5/weather?units=metric&appid="
icon_base_url = "https://openweathermap.org/img/wn/"
img_path = "resources/weather.png"
# kelvin = -273.15

# full_url = f"{url}{api}&lon={lon}&lat={lat}"
full_url = f"{url}{api}&q={city}"

http = PoolManager()

r = http.request("GET", full_url)
if r.status != 200:
    print('(label :text "-unknown error-")')
    exit(1)

content = r.json()
temp_c = content["main"]["temp"]
icon_id = content["weather"][0]["icon"]
icon_url = f"{icon_base_url}{icon_id}.png"


r = http.request("GET", icon_url, preload_content=False)

with open(img_path, "wb") as fp:
    while True:
        data = r.read()
        if not data:
            break
        fp.write(data)

r.release_conn()


# urllib3
# r = requests.get(icon_url)
# if r.status_code == 200:
#    i = Image.open(StringIO(r.content.))
#    i.save(img_path)
#    print(r.content)
#    r.raw.decode_content = True
#    print(img)

print(
    f'(box :class "weatherw" (label :text "{int(temp_c)}°C") (image :image-width 32 :image-height 32 :path "{img_path}"))'
)
