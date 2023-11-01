import requests


url = 'http://localhost:8000/posts/'
response = requests.get(url)
ids = [post['id'] for post in response.json()]

for id in ids:
    url = f'http://localhost:8000/posts/{id}'
    response = requests.delete(url)
    if response.status_code != 204:
        print(f'Error deleting post {id}: {response.text}')
    else:
        print(f'Post {id} deleted successfully', response.status_code)