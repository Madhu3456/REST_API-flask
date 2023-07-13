import requests

url = "http://127.0.0.1:5000/"

response = requests.put(url+'video/1',{"name":"Hollywood Movies","likes":10000,"views":1209800})
print(response.json())