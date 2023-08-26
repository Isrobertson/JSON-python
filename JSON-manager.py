import json

# test data (needs fixing)
for x in range(10):
    student = "student" + str(x)
    data = [{"Student": student, "marks":10, "status": "Fall"}]

#testing
for x in range(10):
    print(data)

# fix later
def write_json(data, filename="1_new_json_data.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
