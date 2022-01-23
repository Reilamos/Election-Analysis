# @TODO: Your code here
pet = {
    "name": "Dino",
    "age": "5",
    "hobbies": [
        "eating candy",
        "crushing rocks",
        "messing with Fred"
    ],
    "wake_ups":{
        "mon": "6:00",
        "Tues": "6.30"
    }
}

pring(f"Name: {pet['name']}")
print(f"Age: {pet['age']}")
print(f"Hobby: {pet['hobbies'][0]}")

print(f"Hobby: {pet['wake_ups']['mon']}")