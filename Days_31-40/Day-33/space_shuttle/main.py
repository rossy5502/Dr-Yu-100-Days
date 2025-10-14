import requests
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
MY_LAT=52#255856
MY_LONG=-0#817586
time_now=datetime.now()

def send_email(msg):
    msg = MIMEText(msg)
    msg["Subject"] = "Space shuttle"
    msg["From"] = "you@example.com"
    msg["To"] = "someone@example.com"

    with smtplib.SMTP("localhost", 8025) as server:
        server.send_message(msg)

    print(f"SUCCESS :Email sent \n {msg}!")
    # for the stmp to work on local server run the below prompt first
    # py -m aiosmtpd -n -l localhost:8025

def space_shuttle_position():
    '''
    This function will return the longitude and latitude of the space shuttle
    '''
    response = requests.get('http://api.open-notify.org/iss-now.json')
    data = response.json()  # this will produce a jason dictionary similar to python dictionary
    longitude = data['iss_position']['longitude']
    latitude = data['iss_position']['latitude']
    return (longitude, latitude)


print(space_shuttle_position())


def weather_api():
    '''
    This function will return the sunrise and sunset times in utc 24hours format
    works out the time of sunrise and sunset based on the latitude and longitude of the user not the space shuttle
    '''
    try:
        lat_value=float(MY_LAT)
        lng_value=float(MY_LONG)
    except ValueError:
        lat_value=MY_LAT
        lng_value=MY_LONG

    params={
        "lat":lat_value,
        "lng":lng_value,
        "formatted":0
    }

    response=requests.get('https://api.sunrise-sunset.org/json',params=params)
    response.raise_for_status()
    data=response.json()
    sunrise=data['results']['sunrise']
    sunset=data['results']['sunset']
    return sunrise,sunset
sunrise,sunset=weather_api()
sunrise_1=int(sunrise.split("T")[1].split(":")[0])
sunset_1=int(sunset.split("T")[1].split(":")[0])
time_now_hour=time_now.hour
def is_night():
    if time_now_hour >= sunset_1 or time_now_hour <= sunrise_1:
        return True
    else:
        return False
def compare_position():
    longitude, latitude = space_shuttle_position()
    # Convert to float first, then to int for comparison
    if MY_LAT-5<=float(latitude)<=MY_LAT+5 and MY_LONG-5<=float(longitude)<=MY_LONG+5:
        return True
    return False
if compare_position():
    if is_night():
        send_email("The space shuttle is above you!")
    else:
        send_email("The space shuttle is above you but it is not night")
else:
    send_email("The space shuttle is not above you!")

#if user want to check every 60 seconds use the while loop above if compare_position() and use
# time.sleep(60) to wait for 60 seconds





