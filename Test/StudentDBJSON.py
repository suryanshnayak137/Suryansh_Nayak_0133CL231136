
import json

students = [
    {"name": "Rahul",  "age": 20, "city": "Mumbai",  "marks": 85},
    {"name": "Alok",  "age": 21, "city": "Delhi",   "marks": 72},
    {"name": "Aryan",  "age": 19, "city": "Pune",    "marks": 90},
]

with open("students.json", "w") as f:
    json.dump(students, f, indent=4)

print("students.json created successfully.\n")

try:
    with open("students.json", "r") as f:
        data = json.load(f)

    print("Students with marks > 75:")
    for s in data:
        if s["marks"] > 75:
            print(f"  Name: {s['name']} | Age: {s['age']} "
                  f"| City: {s['city']} | Marks: {s['marks']}")

except FileNotFoundError:
    print("Error: students.json not found!")