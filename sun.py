import datetime as dt
import requests

endpoint = "https://api.sunrisesunset.io/json"

def get_suntime(lat,lng):

    now = dt.datetime.now()
    date = now.date()

    params ={
        "lat": lat,
        "lng": lng,
        'timezone': "Asia/Kolkata",
        "date": date,
        "time_format":"24"
    }

    response = requests.get(url=endpoint,params=params)
    response = response.json()

    sunrise = response["results"]['sunrise']
    sunrise = sunrise.split()
    sunrise = sunrise[0].split(":")
    sunrise = f"{sunrise[0]}:{sunrise[1]}"

    sunset = response["results"]["sunset"]
    sunset = sunset.split()
    sunset = sunset[0].split(":")
    sunset = f"{sunset[0]}:{sunset[1]}"


    return sunrise, sunset


