import requests


response = requests.get("https://online.vitalsource.com/reader/books/200-DCARGC-21-EN-SG-E/pageid/399")

if response.status_code == 200:
    print(response.text)