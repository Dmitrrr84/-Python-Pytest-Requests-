import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '7948229fe2c7e71c962d2224826ce8cc'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "dmitrrr@mail.ru",
    "password": "999666TpV"
}
body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "Джигурдец1",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}
body_change = {
    "pokemon_id": "26966",
    "name": "Джигурдиссимо",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}
body_pokeboll = {
    "pokemon_id": "26966"
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

response_pokeboll = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeboll)
print(response_pokeboll.text)

message = response_change.json()['message']
message = response_pokeboll.json()['message']