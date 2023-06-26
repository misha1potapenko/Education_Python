# Функции для сериализации объектов в JSON поддерживают несколько
# дополнительных параметров. Они позволяют сделать полученные объекты более
# удобочитаемыми для пользователя. Разберём на примере функции dumps. Но стоит
# помнить, что функция dump обладает такими же параметрами с тем же смыслом.
# import json
# my_dict = {
#     "id": 123,
#     "name": "Clementine Bauche",
#     "username": "Cleba",
#     "email": "cleba@corp.mail.ru",
#     "address": {
#     "street": "Central",
#     "city": "Metropolis",
#     "zipcode": "123456"
#     },
#     "phone": "+7-999-123-45-67"
# }
# res = json.dumps(my_dict, indent=2, separators=(',', ':'),
#                  sort_keys=True)
#
# print(res)


import json

my_dict = {
    "first_name": "Джон",
    "last_name": "Смит",
    "hobbies": ["кузнечное дело", "программирование",
                "путешествия"],
    "age": 35,
    "children": [
        {
            "first_name": "Алиса",
            "age": 5
        },
        {
            "first_name": "Маруся",
            "age": 3
        }
    ]
}
print(f'{type(my_dict) = }\n{my_dict = }')
with open('new_user.json', 'w', encoding='utf-8') as f:
    json.dump(my_dict, f)

with open('new_user.json', 'r', encoding='utf-8') as f:
    new_dict = json.load(f)
print(f'{new_dict = }')
