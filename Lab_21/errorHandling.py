import requests
url='https://jsonplaceholder.typicode.com/posts/1000'
response=requests.get(url)
if response.status_code == 200:
    post=response.json()
    print("Fetched Post:", post)
else:
    print(f"Error: {response.status_code} - {response.reason}")
