
students_and_institutions = [
    {"type": "school", "number_of_students": 100},
    {"type": "college", "number_of_students": 75},
    {"type": "school", "number_of_students": 120},
    {"type": "vocational school", "number_of_students": 50},
    {"type": "school", "number_of_students": 90},
    {"type": "vocational school", "number_of_students": 60}
]

total_students_in_schools = 0

for institution in students_and_institutions:
    if institution["type"] == "school":
        total_students_in_schools += institution["number_of_students"]

print("Total number of students in schools:", total_students_in_schools)
