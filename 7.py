import requests

YANDEX_API_KEY = "0d997e8f-b415-4fd0-91b1-c9547916c893"

def get_district(address):
    url = "https://geocode-maps.yandex.ru/1.x/"
    params = {
        "geocode": address,
        "format": "json",
        "apikey": YANDEX_API_KEY
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()

        feature = data.get('response', {}).get('GeoObjectCollection', {}).get('featureMember', [])
        if feature:
            district = feature[0].get('GeoObject', {}).get('metaDataProperty', {}).get('GeocoderMetaData', {}).get('AddressDetails', {}).get('Country', {}).get('AdministrativeArea', {}).get('SubAdministrativeArea', {}).get('SubAdministrativeAreaName')
            if district:
                return district
        return "Не удалось найти район"
    except Exception as e:
        return f"Ошибка: {str(e)}"

address = input("Введите адрес для поиска района: ")
district = get_district(address)
print(f"Район: {district}")
