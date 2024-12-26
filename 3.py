import requests

YANDEX_GEOCODE_API_KEY = "759b6c75-274f-4700-a5ee-d9a1458a91c3"

def get_satellite_image(coords, filename="satellite.png"):
    url = f"https://static-maps.yandex.ru/1.x/"
    params = {
        "ll": f"{coords[1]},{coords[0]}",
        "z": 16,
        "size": "650,450",
        "l": "sat",
        "apikey": YANDEX_GEOCODE_API_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Снимок сохранён: {filename}")
    else:
        print("Не удалось получить снимок.")

get_satellite_image((55.715551, 37.554191))