import requests
url='https://jsonplaceholder.typicode.com/posts'
response=requests.get(url)
if response.status_code == 200:#200-means success any other number is error
    posts=response.json()#json to list/dictionary
    print("Fetched Posts:")
    for post in posts[:5]:  # Print the first 5 posts
        print(f"Title: {post['title']}")
else:
    print(f"Failed to retrieve posts. Status code: {response.status_code}")
