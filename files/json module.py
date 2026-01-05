import json

student = {
    "student1": {
        "name": "Test",
        "age": 22,
        "gender": "M",
        "email": "test@test.com",
    },
    "student2": {
        "name": "Test2",
        "age": 22,
        "gender": "M",
        "email": "test2@test.com",
    },
    "student3": {
        "name": "Test3",
        "age": 22,
        "gender": "M",
        "email": "test3@test.com",
    }
}

# Dump
with open("student.json", "w") as fh:
    json.dump(student, fh, indent=4)

# Load
with open("student.json", "r") as fh:
    content = json.load(fh)

print(content)
print(type(content))