def get_southernmost_city(cities):
    southernmost_city = None
    southernmost_latitude = float('inf')  
    
    # Обрабатываем каждый город в списке
    for city in cities:
        name, lat, lon = city.split(',')

        lat = float(lat.strip())
        
        if lat < southernmost_latitude:
            southernmost_latitude = lat
            southernmost_city = name.strip()
    
    return southernmost_city


cities_input = input("Введите города и их координаты (в формате 'Город, широта, долгота'), разделённые запятой: ")
cities = cities_input.split(",")  # Разделяем ввод на список

# Определяем самый южный город
southernmost = get_southernmost_city(cities)

# Выводим результат
if southernmost:
    print(f"Самый южный город: {southernmost}")
else:
    print("Нет данных для анализа.")
