import requests
import json

# получаем данные
response = requests.get('https://i-shop.by/data/products.json.gz')

# сохраняем данные в HTML-файл  (на всякий случай)  и присваиваем переменную
with open('iphone_data.html', 'w', encoding='UTF-8') as file:
    file.write(response.text)

with open('iphone_data.html', encoding='UTF-8') as file:
    src = file.read()

# преобразуем в json - файл
data = json.loads(src)

# вытягиваем данные из вложенных словарей и сохраняем в новый  удобный список из словарей
final_data = []
for c in range(len(data)):
    final_data.append({
        'основная модель': data[c]['name'],
        'цена модели: ': data[c]['price'],
    })
    if len(data[c]["variants"]) >= 1:
        for q in range(len("variants") - 2):
            final_data.append(
                {'модель': data[c]["variants"][q]['name'],
                 'старая цена': data[c]["variants"][q]['old_price'],
                 'новая цена': data[c]["variants"][q]['price']
                 }
            )

# данные  о ценах  и моделях  хранятся в файле "new_data.json"
with open('new_data.json', 'w', encoding='UTF-8') as f:
    json.dump(final_data, f, indent=4, ensure_ascii=False)
