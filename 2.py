import folium

path_points = [
    [55.751244, 37.618423],  # Москва
    [55.715551, 37.554191],  # Лужники
    [55.818015, 37.440262],  # Спартак
    [55.791540, 37.559809]   # Динамо
]


path_map = folium.Map(location=path_points[0], zoom_start=11)

for i in range(len(path_points) - 1):
    folium.PolyLine([path_points[i], path_points[i + 1]], color="blue", weight=2.5).add_to(path_map)

# Вычисляем среднюю точку пути
mid_index = len(path_points) // 2
mid_point = path_points[mid_index]

# Добавляем метку на средней точке пути
folium.Marker(location=mid_point, popup="Средняя точка пути").add_to(path_map)

path_map.save("Path_map.html")

print("Карта с маршрутом и средней точкой создана! Откройте файл Path_map.html")
