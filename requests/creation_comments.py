import requests
import random

num_comments = 20

url_comments = 'http://localhost:8000/posts/{id}/comments'
url_posts = 'http://localhost:8000/posts/'

response = requests.get(url_posts)

ids = [post['id'] for post in response.json()]

for i in range(num_comments):
    post_id = random.choice(ids)
    content = f'Random_comment_{i}'
    data = {
        'post_id': post_id,
        'content': content
    }
    response = requests.post(url_comments.replace('{id}', str(post_id)), json=data)
    if response.status_code != 201:
        print(f'Error creating comment {i+1}: {response.status_code}')

print(f'Comments added')
