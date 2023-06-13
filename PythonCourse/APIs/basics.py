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

