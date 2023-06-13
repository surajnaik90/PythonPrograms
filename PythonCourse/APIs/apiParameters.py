#Program to get the sun rise and sun set time 
# Use this API to pass parameters: https://sunrise-sunset.org/api

import requests

MY_LATTITUDE = 14.661000
MY_LONGITUDE = 74.304604

#Create a python dictionary: Note - parameter names are as per the API spec
parameters = {
    "lat": MY_LATTITUDE,
    "lng": MY_LONGITUDE
}

# verify=False because to fix: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: 
# unable to get local issuer certificate (_ssl.c:997)
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters, verify=False)

#URL would be:  https://api.sunrise-sunset.org/json?lat=14.661000&lng=74.304604

data = response.json();

print(data)

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise)