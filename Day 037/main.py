import requests
import datetime

USERNAME = "steventwj"
TOKEN = "5hvMgwDpNqG6xVs4"

pixela_endpoint = "https://pixe.la/v1/users"
users_params = {
    "token": f"{TOKEN}",
    "username": f"{USERNAME}",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=users_params)
# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_params = {
#     "id": "graph1",
#     "name": "Coding Graph",
#     "unit": "hours",
#     "type": "float",
#     "color": "momiji",
# }

# headers = {
#     "X-USER-TOKEN": TOKEN
# }

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)

# graph_insert_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
# graph_insert_params = {
#     "date": f"{yesterday.strftime('%Y%m%d')}",
#     "quantity": "2.8"
# }

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_insert_endpoint, json=graph_insert_params, headers=headers)
# print(response.text)

# graph_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
# graph_update_params = {
#     "quantity": "3.5",
# }

# response = requests.put(url=graph_update_endpoint, json=graph_update_params, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{yesterday.strftime('%Y%m%d')}"
# delete_params = {
#     "quantity": "3.5",
# }

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)