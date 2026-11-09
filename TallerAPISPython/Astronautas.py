import requests
import datetime

def getInfo(url):
    response = requests.get(url)

    if (response.status_code == 200):
        return response.json()
    else:
        print(response.status_code)
        return "Error"

url = "http://api.open-notify.org/astros.json"
response = getInfo(url)

if (response != "Error"):
    print("Número de astronautas en el espacio:", response["number"])
    for astronauta in response["people"]:
        print("Astronauta:", astronauta["name"])
else:
    print(response)