import json
import string

# my = set(json.load(open('censor.json')))
# print(my)

import json


with open('words.json') as f:
    templates = json.load(f)
list_censor = []
for i in templates:
    list_censor.append(i['word'])
    # print(i['word'])

with open('censor_.json', 'w', encoding='utf-8') as e:
    json.dump(list_censor, e)


# for section, commands in templates.items():
#     print(section)
#     print('\n'.join(commands))
