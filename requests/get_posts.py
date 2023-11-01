import requests

url = ('http://localhost:8000/posts')
response = requests.get(url)

for post in response.json():
    print(post)
