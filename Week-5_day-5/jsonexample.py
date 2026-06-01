import json

student = {
    "id": 1,
    "name": "prinsi",
    "marks": 90
}

# WRITE JSON
with open("student.json", "w") as f:
    json.dump(student, f, indent=2)

# READ JSON
with open("student.json", "r") as f:
    data = json.load(f)

print(data)
print(data["name"])