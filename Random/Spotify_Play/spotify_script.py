import requests, time, os

url = "https://accounts.spotify.com/api/token"

#data

data = {
    "grant_type":"client_credentials",
    "client_id": "046fbd8330bc450daf14b6eed745bb7f",
    "client_secret":"69b6e2f362af40dc9ccf9da0642d7d35"
}

headers ={
    "Content-Type":"application/x-www-form-urlencoded"
}


token = "BQCqHpK6d5n6ItDqXatG_DcUywZ-uwVZQELhv0QDw5ij9rGleNnOn5wiu7YD70bUDuEqHmFjd9ziwGJCFADbsZDLwfVAbpfa1nGzkW-0QPqA3CC2wMTf_uAk6ta6CKHy25tVdr8jLqw"

def get_token() -> str:
    response = requests.post(url,data=data,headers=headers)

    t = response.json()['access_token']
    print(f"Token is: {t} ")
    return t

def write_token(t):
    filename = "token_file_" + str(t[-5:])
    # current_dir = os.path.dirname(os.path.abspath(filename))
    print(os.getcwd())
    print(f"filename: {filename}")

if token == "":
    token = get_token()


write_token(token)
linmanuelmiranda_id = "4aXXDj9aZnlshx7mzj3W1N?si=X_7rrVCuRxmrKK-Tun_dnA"

