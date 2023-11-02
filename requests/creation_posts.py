import requests
import json


url = 'http://localhost:8000/posts'
num_posts = 10
data_list = []

for i in range(num_posts):
    data = {'title': str(f'Title_{i}'), 'content': str(f'Content_{i}')}
    data_list.append(data)

for i in range(num_posts):
    response = requests.post(url, data=json.dumps(data_list[i]))
    if response.status_code != 201:
        print(f'Error creating post {i+1}: {response.status_code}')

print('Posts added')