import requests

url = "https://www.fast2sms.com/dev/wallet"

headers = {
    'authorization': "cyPmERQdGApYWKN9fU0VnLzZeSJqiwtsIrgCHl3u2av4bjXokBflh3VKeJSI9jyvObAkU6adPgBZ1EzH",
    }

response = requests.request("POST", url, headers=headers)

print(response.text)