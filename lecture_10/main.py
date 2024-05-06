import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.post(url,
                         json={"title": "foo",}, 
                         headers={"Content-Type": "application/json"}
                         )

print(response.headers)
