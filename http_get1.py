import requests

url = "http://localhost:1880/int-post"

datax = "ichwan"

r = requests.post(url, data = datax)

print r

print r.text
