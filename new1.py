import webbrowser
import Play_mp3
import requests

url = input("podaj adres strony")
webbrowser.open(url)
filename = "Kalimba.mp3"
Play_mp3.play(filename)

daty = ["20200101", "20210202", "20220303"]

for data in daty:
    url1 = "http://archive.org/wayback/available?url=" + url + "&timestamp=" + str(data)
    response = requests.get(url1)
    d = response.json()
    page = d["archived_snapshots"]["closest"]["url"]
    webbrowser.open(page)

