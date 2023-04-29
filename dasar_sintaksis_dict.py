users = {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "sincere@april.biz",
    "address": {
      "street": "Kulas Light",
      "suite": "Apt. 556",
      "city": "Gwenborough",
      "zipcode": "92998-3874",
      "geo": {
        "lat": "-37.3159",
        "lng": "81.1496"
      }
    }
}

print(users)
print(users["id"])
print(users["name"])
print(users["username"])
print(users["email"])
print(users["address"])
print(users["address"]["geo"])
print(users["address"]["geo"]["lat"])
print(type(users))

print('\nubah dict ke json')
import json
result = json.dumps(users)
print(result)
print(type(result))
