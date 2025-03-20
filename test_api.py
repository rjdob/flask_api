import requests, json


data = {
  'Age': 42,
  'Account_Manager': 0,
  'Years': 7,
  'Num_Sites': 8
}

response = requests.post("http://127.0.0.1:5000/predict", data=data)


print(response.content)