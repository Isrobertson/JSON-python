import json

data = {}
#limit = 0

#temporary data
data['isrobertson'] = {'name': 'Ian',
                       'address': 'NA',
                       'Phone': '123456789'}

# creates and sorts data into json file
with open("temporary_data.json", 'w') as json_data:
    json.dump(data, json_data, indent=4, sort_keys=True)
