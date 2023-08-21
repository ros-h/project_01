import random
import datetime
# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
#Решение 1:
#Сложить округленное до минут время 3 песен
#генерируем список из 3 рандомных чисел от 0 до 8
total_time = 0
total_time += round(my_favorite_songs[1][1])
total_time += round(my_favorite_songs[3][1])
total_time += round(my_favorite_songs[8][1])
print('Три песни звучат', total_time, 'минут')

#Решение 2 - пункты С и D
#Плюс генерируются рандомные значения песен - пункт С
songs = random.choices(my_favorite_songs, k=3)

# Переводим длительность песен в datatime
total_time = datetime.timedelta(seconds = 0)
for num in songs:
    str_tt = str(num[1]).split('.', 2)
    delta = datetime.timedelta(minutes = int(str_tt[0]), seconds = int(str_tt[1]))
    total_time += + delta
print(f"Три песни звучат {total_time} минут")


# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
#Решение 1
tt = 0
tt += round(my_favorite_songs_dict['A Sorta Fairytale'])
tt += round(my_favorite_songs_dict['Staying\' Alive'])
tt += round(my_favorite_songs_dict['Nowhere to Run'])
print(f"Три песни звучат {tt} минут")

#Решение 2 - с модулями random и datatime
rand_songs = random.choices(list(my_favorite_songs_dict.items()), k=3) #В идеале нужно добавить проверку на повтор значений
total = datetime.timedelta(seconds = 0)
for el in rand_songs:
    str_t = str(el[1]).split('.', 2)
    delta = datetime.timedelta(minutes = int(str_t[0]), seconds = int(str_t[1]))
    total = total + delta
print(f"Три песни звучат {total} минут")

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 