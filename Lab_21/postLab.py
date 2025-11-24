import requests

class APIClient:
    def __init__(self):
        self.base_url="https://jsonplaceholder.typicode.com"

    def fetch_posts(self):
        url=f"{self.base_url}/posts"
        response=requests.get(url)

        if response.status_code==200:
            print("Posts fetched successfully.")
            return response.json()
        else:
            print(f"Error fetching posts: {response.status_code}")
            return None

    def create_post(self,title,body,user_id):
        url=f"{self.base_url}/posts"
        new_post={
            "title": title,
            "body": body,
            "userId": user_id
        }
        response=requests.post(url,json=new_post)
        if response.status_code == 201:
            print("Post created successfully.")
            return response.json()
        else:
            print(f"Error creating post: {response.status_code}")
            return None

client=APIClient()

posts=client.fetch_posts()
if posts:
    print("\nFirst 5 Posts:")
    for p in posts[:5]:
        print(f"- {p['title']}")

new_post=client.create_post("My API Post", "This is a body.", 1)
if new_post:
    print("\nCreated Post:")
    print(new_post)