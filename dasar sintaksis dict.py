users = {
    "id" : 1,
    "name" : "Muhammad Ihsan",
    "username" : "muhammadihsan",
    "email" : "muhammadihsan3011@gmail.com",
    "address" : {
        "Jalan" : "Mangu-Nogosari",
        "Kelurahan/Desa" : "Potronayan",
        "Kecamatan" : "Nogosari",
        "Kota/Kabupaten" : "Boyolali",
        "Provinsi" : "Central Java",
        "Country" : "Indonesia"
    }
}

print(users)
print(users["id"])
print(users["name"])
print(users["username"])
print(users["email"])
print(users["address"])

print(users)
print(type(users))
print("\nUbah dict ke JSON")
import json
result = json.dumps(users)
print(type(result))
print(result)

with open('result.json', 'w') as file:
    json.dump(users, file)

    