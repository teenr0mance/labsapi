import requests
import math

YANDEX_API_KEY = "0d997e8f-b415-4fd0-91b1-c9547916c893"

def get_coordinates(address):
    url = "https://geocode-maps.yandex.ru/1.x/"
    params = {
        "geocode": address,
        "format": "json",
        "apikey": YANDEX_API_KEY
    }
    
    response = requests.get(url, params=params)
    data = response.json()

    try:
        coordinates = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()
        lon, lat = float(coordinates[0]), float(coordinates[1])
        return lon, lat
    except (KeyError, IndexError):
        print("Не удалось найти координаты для адреса:", address)
        return None

# Функция для вычисления расстояния между двумя точками по декартовой метрике
def lonlat_distance(a, b):
    degree_to_meters_factor = 111 * 1000  # 111 километров в метрах
    a_lon, a_lat = a
    b_lon, b_lat = b
    
    radians_latitude = math.radians((a_lat + b_lat) / 2.)
    lat_lon_factor = math.cos(radians_latitude)
    

    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meters_factor
    
    distance = math.sqrt(dx * dx + dy * dy)
    
    return distance

def main():
    home_address = "Уфа, улица Коммунистическая, 109"
    university_address = "Уфа, улица Заки Валиди, 32"
    
    home_coords = get_coordinates(home_address)
    university_coords = get_coordinates(university_address)
    
    if home_coords and university_coords:
        distance = lonlat_distance(home_coords, university_coords)
        print(f"Расстояние между вашим домом и университетом: {distance / 1000:.2f} км")
    else:
        print("Не удалось вычислить расстояние из-за ошибки при получении координат.")

if __name__ == "__main__":
    main()
