import json
import csv

#test read .csv file
with open('in/testsheet 1.csv', 'r') as read_csv_data:
    reader = csv.reader(read_csv_data)
    headers = next(reader) # Read the header row in csv file

    csvData = []
    for row in reader:
        record = {}
        for i, value in enumerate(row):
            record[headers[i]] = value
        csvData.append(record)

print(csvData)

choice = input('would you like to create a .json file? (y / n) ')

if choice == 'y' or choice == 'Y':
    print('ok.')
elif choice == 'n' or choice == 'N':
    print('goodbye.')
else:
    print('error')


data = {}
#limit = 0

#temporary data
data['isrobertson'] = {'name': 'Ian',
                       'address': 'NA',
                       'Phone': '123456789'}

# creates and sorts data into json file
with open("test.json", 'w') as json_data:
    json.dump(data, json_data, indent=4)
