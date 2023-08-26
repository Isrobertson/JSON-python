import json

data = {}
#limit = 0

#temporary data
data['isrobertson'] = {'name': 'Ian',
                       'address': 'NA',
                       'Phone': '123456789'}

#testing
print(data)

with open("temporary_data.json", 'w') as json_data:
    json.dump(data, json_data)
