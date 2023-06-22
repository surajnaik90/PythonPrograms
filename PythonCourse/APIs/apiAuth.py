# Use this site: https://openweathermap.org/ 

import requests

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"

weather_params = {

    "lat" : 14.661000,
    "lon" : 74.304604,
    "appid" : jdfkljsdklfjsdjflsd
}

response = requests.get(OWM_Endpoint,params=weather_params)
response.raise_for_status()

data = response.json()
print(data)