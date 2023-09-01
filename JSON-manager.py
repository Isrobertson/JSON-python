import json
import csv

#read csv file
with open('in/testsheet 1.csv', 'r') as read_csv_data:
    reader = csv.reader(read_csv_data)
    headers = next(reader) # Read the header row in csv file

    csvData = []
    for row in reader:
        record = {}
        for i, value in enumerate(row):
            record[headers[i]] = value
        csvData.append(record)

testData = {}
testData['clients'] = csvData # this works!

# writes data into json file
with open("out/test.json", 'w') as json_data:
    json.dump(testData, json_data, indent=4)
