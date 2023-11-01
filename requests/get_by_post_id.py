import requests
import json

response = requests.get('http://localhost:8000/posts/1')
for post in response.json():
    print(post)