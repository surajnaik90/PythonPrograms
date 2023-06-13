# Understanding APIs in Python

## Status Codes: https://httpstatuses.io/

### Simple API - International Space Station - http://open-notify.org/Open-Notify-API/ISS-Location-Now/

http://api.open-notify.org/iss-now.json

Returns the response in the below format:

{
  "message": "success", 
  "timestamp": UNIX_TIME_STAMP, 
  "iss_position": {
    "latitude": CURRENT_LATITUDE, 
    "longitude": CURRENT_LONGITUDE
  }
}

### Install JSON Viewer Awesome in Chrome

Example:
{
    "message": "success",
    "iss_position": {
        "latitude": "-11.2965", 
        "longitude": "125.5408"
    },
    "timestamp": 1686650238
}

### To know the ISS position : https://www.latlong.net/