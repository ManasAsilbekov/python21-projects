import requests

url = 'https://bipbap.ru/wp-content/uploads/2017/04/priroda_kartinki_foto_03.jpg'

res = requests.get(url)
print(res.content)
name = "photos/photo1.jpg"

with open(name, "wb") as file:
    file.write(res.content)