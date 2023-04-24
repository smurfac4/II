import json
import re

# входные данные в формате JSON
input_json ='''
[
    {"en": "Male", "es": "Macho"},
    {"en": "Female", "es": "Hembra"},
    {"en": "Population", "es": "Poblacion"}
]
'''

# парсим входные данные из JSON (преобразование в объект с которым можно работать)
data = json.loads(input_json)

# преобразуем каждую запись в формат CSV
for item in data:

    # ищем текст в кавычках в каждом значении словаря и заменяем на формат CSV

    csv_record = re.sub(r'"(.*?)"', # поиск подстроки заклеченной в кавычки, включая пустые строки
                        r'"\1"', #замена  подстроки на себя же без кавычек
                        f'"{item["en"]}";"{item["es"]}"') # то что будем обрабатывать
    # выводим результат
    print(csv_record)