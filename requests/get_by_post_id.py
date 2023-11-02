import requests

url = 'http://localhost:8000/posts/3'
response = requests.get(url)

for post in [response.json()]:
    print(post['title'])
    for comment in post['comments']:
        print(comment)
    print('\n')
