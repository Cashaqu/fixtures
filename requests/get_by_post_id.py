import requests

url = 'http://localhost:8000/posts?id=1'
response = requests.get(url)
print(response.json())
print("Error:", response.status_code)