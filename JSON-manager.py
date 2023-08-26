import json

# test data
for x in range(10):
    student = "student" + str(x)
    data = [{"Student": student, "marks":10, "status": "Fall"}]

#testing
for x in range(10):
    print(data)

def write_json(data, filename="1_new_json_data.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
