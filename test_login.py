import requests

url = "http://127.0.0.1:5000/login"

data = {
    "username": "admin",
    "password": "invalidpassword"
}

response = requests.post(url, data=data)

print("Status:", response.status_code)
print("Response:", response.text)