import requests

url = 'http://localhost:8000/posts'
response = requests.get(url)

for post in response.json():
    print(post['title'])
    for comment in post['comments']:
        print(comment)
    print('\n')