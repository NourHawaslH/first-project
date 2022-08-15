import tkinter as tk
import requests
import time

def getweather(canvas):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city +"&appid=5a18667e23839f0d073dd3fb691ea727"
    json_data = requests.get(api).json()
    condition = json_data["weather"][0]["main"]
    temp = int(json_data["main"]["temp"] - 273.15)
    min_temp = int(json_data["main"]["temp_min"] - 273.15)
    max_temp = int(json_data["main"]["temp_max"] - 273.15)
    pressure = json_data["main"]["pressure"]
    humidity = json_data["main"]["humidity"]
    wind = json_data["wind"]["speed"]
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data["sys"]["sunrise"] -21600 ))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data["sys"]["sunset"] -21600))

    final_info = condition + "\n" + str(temp) + "°c"
    final_data = "\n" + "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(
        max_temp) + "°C" + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(
        humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text=final_info)
    label2.config(text=final_data)


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(canvas, justify='center', width=20, font=t)
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()
canvas.mainloop()

label1.config(text = final_info)
label2.config(text = final_data)
textfield.bind("<return", getweather)




canvas = tk.tk()
canvas.geometry ("600x500")
canvas.title("weather app")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.entry(canvas, font = t )
textfield.pack(pady = 20)
textfield.focus()

label1 = tk.label(canvas, font = t)
label1.pack()
label2 = tk .label(canvas, font = f)
label2.pack()

canvas.mainloop()




