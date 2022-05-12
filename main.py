import ssl
from tkinter import *

import certifi
import phonenumbers
from geopy import location
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
import geopy.geocoders
from datetime import datetime
import pytz

window = Tk()
window.title("Phone Number Tracker")
window.geometry("365x584+400+100")
window.resizable(False, False)
ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx


def track():
    enter_number1 = enter_number.get()
    number = phonenumbers.parse(enter_number1)

    # country
    locate = geocoder.description_for_number(number, 'en')
    country.config(text=locate)

    # operator like Idea, airtel, jio and many other
    operator = carrier.name_for_number(number, "en")
    sim.config(text=operator)

    # Phone TimeZone
    time = timezone.time_zones_for_number(number)
    zone.config(text=time)

    # Longitude and latitude
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(locate)

    lng = location.longitude
    lat = location.latitude
    longitude.config(text=lng)
    latitude.config(text=lat)

    # Time showing in phone
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M:%p")
    clock.config(text=current_time)


# logo
logo = PhotoImage(file="logo image.png")
Label(window, image=logo).place(x=240, y=70)

Heading = Label(window, text="TRACK NUMBER", font=("arial", 15, "bold"))
Heading.place(x=90, y=110)

# Entry
Entry_back = PhotoImage(file="search png.png")
Label(window, image=Entry_back).place(x=20, y=190)

entry = StringVar()
enter_number = Entry(window, textvariable=entry, width=22, bd=0, font=("arial", 20), justify="center")
enter_number.place(x=48, y=223)

# Button
Search_image = PhotoImage(file="search.png")
search = Button(image=Search_image, borderwidth=0, cursor="hand2", bd=0, font=("arial", 16), command=track)
search.place(x=35, y=300)

# bottom
Box = PhotoImage(file="bottom png.png")
Label(window, image=Box).place(x=-2, y=355)

country = Label(window, text="Country: ", bg="#57adff", fg="black", font=("arial", 15, "bold"))
country.place(x=25, y=400)

sim = Label(window, text="SIM: ", bg="#57adff", fg="black", font=("arial", 15, "bold"))
sim.place(x=150, y=400)

zone = Label(window, text="TimeZone: ", bg="#57adff", fg="black", font=("arial", 15, "bold"))
zone.place(x=25, y=450)

clock = Label(window, text="Phone Time: ", bg="#57adff", fg="black", font=("arial", 15, "bold"))
clock.place(x=150, y=450)

longitude = Label(window, text="Longitude: ", bg="#57adff", fg="black", font=("arial", 15, "bold"))
longitude.place(x=25, y=500)

latitude = Label(window, text="Latitude: ", bg="#57adff", fg="black", font=("arial", 15, "bold"))
latitude.place(x=150, y=500)

window.mainloop()
