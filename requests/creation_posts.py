import requests
import json

# URL запроса
url = "http://localhost:8000/posts"

# Количество записей, которые нужно добавить в базу данных
num_posts = 10

# Считаем JSON-объекты, которые будут отправлены в запросе
data_list = []
for i in range(num_posts):
    data = {"title": str(f"Title_{i}"), "content": str(f"Content_{i}")}
    data_list.append(data)

for i in range(num_posts):
    response = requests.post(url, headers={'Content-Type': 'application/json'}, data=json.dumps(data_list[i]))
    if response.status_code != 201:
        print(f"Ошибка при отправке запроса {response.status_code}")
    else:
        print(f"Запись {i + 1} из {num_posts} успешно добавлена")
