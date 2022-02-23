import requests

url = "https://goolnk.com/api/v1/shorten"

target_url = input("enter url: ")
url_values = target_url.strip("https://").split(".", maxsplit=1)
payload = f"url=https%3A%2F%2F{url_values[1]}%2F"
headers = {"Content-Type": "application/x-www-form-urlencoded"}
response = requests.request("POST", url, headers=headers, data=payload)

data = response.json()
print("shortend version -->", data["result_url"])
