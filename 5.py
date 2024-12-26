import requests

YANDEX_GEOCODE_API_KEY = "0d997e8f-b415-4fd0-91b1-c9547916c893"
YANDEX_SEARCH_API_KEY = "6c058cdf-afa0-40e6-8d9f-740452796714"

def geocode_address(address):
    """Преобразование адреса в координаты (широта и долгота)"""
    geocode_url = "https://geocode-maps.yandex.ru/1.x/"
    geocode_params = {
        "geocode": address,
        "format": "json",
        "apikey": YANDEX_GEOCODE_API_KEY
    }
    response = requests.get(geocode_url, params=geocode_params).json()
    
    try:
        lat, lon = response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()
        return float(lat), float(lon)
    except (KeyError, IndexError):
        print("Не удалось найти координаты для указанного адреса.")
        return None, None

def find_nearest_pharmacy(lat, lon):
    """Поиск ближайшей аптеки по координатам"""
    search_url = "https://search-maps.yandex.ru/v1/"
    search_params = {
        "text": "аптека",
        "ll": f"{lon},{lat}", 
        "type": "biz",
        "apikey": YANDEX_SEARCH_API_KEY,
        "spn": "0.1,0.1", 
    }
    response = requests.get(search_url, params=search_params).json()

    try:
        nearest_pharmacy = response['features'][0]
        pharmacy_name = nearest_pharmacy['properties']['CompanyMetaData']['name']
        pharmacy_address = nearest_pharmacy['properties']['CompanyMetaData']['address']
        return pharmacy_name, pharmacy_address
    except (KeyError, IndexError):
        print("Не удалось найти аптеку рядом.")
        return None, None

def main():
    # Вводим адрес с клавиатуры
    address = input("Введите адрес: ")

    lat, lon = geocode_address(address)
    
    if lat is not None and lon is not None:
        pharmacy_name, pharmacy_address = find_nearest_pharmacy(lat, lon)
        
        if pharmacy_name:
            print(f"Ближайшая аптека: {pharmacy_name}")
            print(f"Адрес: {pharmacy_address}")
        else:
            print("Аптека не найдена.")
    else:
        print("Ошибка при получении координат.")

if __name__ == "__main__":
    main()
