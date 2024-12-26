import folium

# Создаем карту Москвы
moscow_map = folium.Map(location=[55.751244, 37.618423], zoom_start=11)

# Координаты стадионов(по заданию)
stadiums_location = {
    "Лужники": "37.554191,55.715551",
    "Спартак": "37.440262,55.818015",
    "Динамо": "37.559809,55.791540",
}


for stadium, coords in stadiums_location.items():
    lon, lat = map(float, coords.split(','))
    folium.Marker(location=[lat, lon], popup=stadium).add_to(moscow_map)

# Сохраняем карту в HTML
moscow_map.save("Moscow_stadiums_map.html")

print("Карта успешно создана! Откройте файл Moscow_stadiums_map.html")
