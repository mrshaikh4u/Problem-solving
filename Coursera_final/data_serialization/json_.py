import json
people = []
people.append({
    "name": "Sabrina Green",
    "username": "sgreen",
    "phone": {
        "office": "802-867-5309",
        "cell": "802-867-5310"
    },
    "department": "IT Infrastructure",
    "role": "Systems Administrator"
})
people.append(
    {
    "name": "Eli Jones",
    "username": "ejones",
    "phone": {
        "office": "684-348-1127"
    },
    "department": "IT Infrastructure",
    "role": "IT Specialist"
})

with open('people.json', 'w') as people_json:
    json.dump(people, people_json, indent=2)


with open("people.json","r") as people_json_2:
    people_obj = json.load(people_json_2)

print(type(people_obj))
print(people_obj[0].get('name'))

# test = "hello world"
# test_1 = [1,"232",1.2]
# with open("hello.json","w") as hello_json:
#     json.dump(test_1,hello_json,indent=2)



