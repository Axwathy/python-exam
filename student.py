students = [
    {"id": 1, "name": "Rajesh"},
    {"id": 2, "name": "Rahul"},
    {"id": 3, "name": "Sruthi"}
]

search_id = int(input("Enter Student ID: "))
found = False
for student in students:
    if student["id"] == search_id:
        print("Student Name:", student["name"])
        found = True
        break
if not found:
    print("Student not found")