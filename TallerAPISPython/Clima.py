import requests
import datetime

def getInfo(url):
    response = requests.get(url)

    if (response.status_code == 200):
        return response.json()
    else:
        print(response.status_code)
        return "Error"

ciudad = input("Introduce una ciudad para conocer su información meteorológica: ")
url = "https://api.openweathermap.org/data/2.5/weather?q="+ciudad+"&mode=json&units=metric&lang=es&appid=253a8b307ccaf56879da89134f578e12"
response = getInfo(url)
if (response != "Error"):
    #clave:valor
    print("Ciudad:", response["name"])

    #clave:diccionario
    print("Longitud:", response["coord"]["lon"])
    print("Latitud:", response["coord"]["lat"])

    print("Temperatura:",response["main"]["temp"])
    print("Humedad:", response["main"]["humidity"])
    print("Temperatura mínima:", response["main"]["temp_min"])
    print("Temperatura máxima:", response["main"]["temp_max"])

    unixTimeSunrise = response["sys"]["sunrise"]
    unixTimeSunset = response["sys"]["sunset"]

    dateTimeSunrise = datetime.datetime.fromtimestamp(unixTimeSunrise)
    dateTimeSunset = datetime.datetime.fromtimestamp(unixTimeSunset)

    print("La salida del sol es:", dateTimeSunrise.strftime("%H:%M:%S"))
    print("La puesta del sol es:", dateTimeSunset.strftime("%H:%M:%S"))

    for dato in response["weather"]:
        print("Descipción del día:",dato["description"])

    print("Velocidad del viento:",response["wind"]["speed"])

else:
    print(response)
