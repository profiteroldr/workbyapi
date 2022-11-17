import requests

api = "89f43f1f20b6e6c6e3a602d47906405b"

base_url = "https://api.openweathermap.org/data/2.5/weather?"

sehir_ismi = input("Sehir ismi giriniz: ")

url = base_url + "appid=" + api + "&q=" + sehir_ismi

gelen_veri = requests.get(url)
gelen_veri_json = gelen_veri.json()

if (gelen_veri_json["cod"] != "404"):

    temp = gelen_veri_json["main"]["temp"]
    description = gelen_veri_json["weather"][0]["description"]
    pressure = gelen_veri_json["main"]["pressure"]
    country = gelen_veri_json["sys"]["country"]

    print("temp: " + str(float(temp) - 273.14))
    print("description: " + str(description)) # print("description: " , description) şeklinde yazılabilir. + şareti koyarsak str değerine çevirmemiz gerekmektedir.
    print("pressure: " + str(pressure)) # print("pressure: " , pressure) şeklinde yazılabilir. + şareti koyarsak str değerine çevirmemiz gerekmektedir.
    print("country: " + str(country)) # print("country: " , country) şeklinde yazılabilir. + şareti koyarsak str değerine çevirmemiz gerekmektedir.

else:
    print("Böyle bir şehir bulunamadı!")