import requests
url='https://jsonplaceholder.typicode.com/posts'

new_post = {
    "title": "My New Post",
    "body": "This is the content of my new post.",
    "userId": 1
}
response=requests.post(url,json=new_post)
if response.status_code == 201:#200-means success any other number is error
    created_post=response.json()
    print("Created Post:")
    print(f"Title: {created_post['title']}")
    print(f"Body: {created_post['body']}")
else:
    print(f"Failed to create post. Status code: {response.status_code}")

