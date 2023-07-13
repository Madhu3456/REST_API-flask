import requests

url = "http://127.0.0.1:5000/"

'''Test put request'''

response = requests.put(url+'video/1',{"name":"Hollywood Movies","likes":10000,"views":1209800})
print(response.json())

'''Test get requests'''

response = requests.get(url + 'video/1')
print(response.json())

'''Test update requests'''

response = requests.patch(url+'video/1' , {"name": "Bollywood Movies"})
print(response.json())

'''Test Delete Request'''

response = requests.delete(url+'video/1')
print(response)