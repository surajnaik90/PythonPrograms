import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

#Handling exception: Use in-built function 'raise_for_status' of requests module itself
#For example: Make an error in the URL below
#response = requests.get(url="http://api.open-notify.org/issnow.json")
#response.raise_for_status(); #You'll see the error for this as URL above is incorrect

print(response)
print(response.status_code)

data = response.json()
print(data)

location = data["iss_position"]
print(location)

longitude = location["longitude"]
print(longitude)

latitude = location["latitude"]
print(latitude)

#Create a tuple
iss_position = (latitude,longitude)
print(iss_position)

#Check the position in here: https://www.latlong.net/