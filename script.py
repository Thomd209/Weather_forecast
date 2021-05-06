from tkinter import *
import requests
import os

root = Tk()
root.title("Weather forecast")

title = Label(text="Weather forecast", font=("Arial", 24))
title.place(relx=0.375, rely=0.025)

city_lib = Label(text="Enter the city where you want to know the weather:", font=("Arial", 12))
city_lib.place(relx=0.015, rely=0.1)

city_ent = Entry(width=20)
city_ent.place(relx=0.015, rely=0.15)


def is_city_ent_empty():
    if city_ent.get() == "":
        return True
    else:
        return False


def is_weather_response_json(response):
    if response.text[0] == '{':
        return True
    else:
        return False


def insert_weather_data(response):
    f = open("weather.html", "w")
    f.write(response.text)
    f.close()


def check_weather():
    if is_city_ent_empty():
        city_ent.insert(0, "You didn't entry a city")
    else:
        city_name = city_ent.get()
        api_key = ""
        response_format = "html"
        weather_response = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&mode={response_format}")

        if is_weather_response_json(weather_response):
            city_ent.delete(0, END)
            city_ent.insert(0, "City not found")
        else:
            insert_weather_data(weather_response)
            os.startfile("weather.html")


btn_check_weather = Button(text="Check the weather", bg="black", fg="white", font=("Arial", 12), command=check_weather)
btn_check_weather.place(relx=0.015, rely=0.2)

root.mainloop()
