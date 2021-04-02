import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes":10, "name": "tim", "views": 42069},
        {"likes":100, "name": "tom", "views": 50},
        {"likes":40, "name": "dennis", "views": 300},
        {"likes":15, "name": "other", "views": 6000000}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

# input()
# response = requests.delete(BASE + "video/0")
# print(response)
# input()
# response = requests.get(BASE + "video/2")
# print(response.json())